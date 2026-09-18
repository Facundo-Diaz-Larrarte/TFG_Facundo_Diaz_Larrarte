#!/usr/bin/env python3
"""Modelos preliminares de panel para IA y productividad laboral aparente.

Las estimaciones son asociativas. Los errores estándar se agrupan por entidad
país-sector. La especificación preferida incorpora efectos fijos país-sector y
país-año, que absorben heterogeneidad permanente y shocks macroeconómicos
comunes a los sectores de cada país en cada año.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import t as student_t


AI_LABELS = {
    "ai_any_pct": "Adopción general",
    "ai_ge2_pct": "Dos o más tecnologías",
    "ai_ge3_pct": "Tres o más tecnologías",
    "ai_workflow_pct": "Procesos y decisiones",
    "ai_production_pct": "Producción",
    "ai_logistics_pct": "Logística",
    "ai_marketing_pct": "Marketing y ventas",
    "ai_security_pct": "Seguridad informática",
}

SPECS = {
    "M1_pooled_FE": ["country_code", "sector_code", "year"],
    "M2_entity_year_FE": ["entity", "year"],
    "M3_entity_countryyear_FE": ["entity", "country_year"],
}


def design_matrix(df: pd.DataFrame, ai_variable: str, fixed_effects: list[str]) -> tuple[np.ndarray, list[str]]:
    parts = [pd.Series(1.0, index=df.index, name="const"), df[ai_variable].astype(float)]
    names = ["const", ai_variable]
    for fe in fixed_effects:
        dummies = pd.get_dummies(df[fe].astype(str), prefix=fe, drop_first=True, dtype=float)
        parts.append(dummies)
        names.extend(dummies.columns.tolist())
    matrix = pd.concat(parts, axis=1)
    return matrix.to_numpy(dtype=float), names


def clustered_ols(y: np.ndarray, x: np.ndarray, clusters: np.ndarray) -> dict[str, np.ndarray | float | int]:
    xtx_inv = np.linalg.pinv(x.T @ x)
    beta = xtx_inv @ x.T @ y
    resid = y - x @ beta
    meat = np.zeros((x.shape[1], x.shape[1]))
    unique_clusters = pd.unique(clusters)
    for cluster in unique_clusters:
        idx = clusters == cluster
        score = x[idx].T @ resid[idx]
        meat += np.outer(score, score)
    n, k = x.shape
    g = len(unique_clusters)
    correction = (g / (g - 1)) * ((n - 1) / (n - k)) if g > 1 and n > k else 1.0
    vcov = correction * xtx_inv @ meat @ xtx_inv
    se = np.sqrt(np.maximum(np.diag(vcov), 0))
    fitted = x @ beta
    ssr = float(np.sum(resid**2))
    tss = float(np.sum((y - y.mean()) ** 2))
    return {
        "beta": beta,
        "se": se,
        "resid": resid,
        "r2": 1 - ssr / tss if tss > 0 else np.nan,
        "n": n,
        "k": k,
        "clusters": g,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/modelos_panel_v0_1"))
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    if args.input.suffix.lower() == ".csv":
        panel = pd.read_csv(args.input)
        data = panel[(panel["core_complete"] == "Yes") & (panel["balanced_entity"] == "Yes")].copy()
    else:
        data = pd.read_excel(args.input, sheet_name="Muestra_balanceada")
    data = data[data["labour_productivity_keur"] > 0].copy()
    data["log_productivity"] = np.log(data["labour_productivity_keur"])
    data["entity"] = data["country_code"].astype(str) + "_" + data["sector_code"].astype(str)
    data["country_year"] = data["country_code"].astype(str) + "_" + data["year"].astype(str)

    rows = []
    for spec_name, fixed_effects in SPECS.items():
        for ai_variable, label in AI_LABELS.items():
            sample = data[["log_productivity", ai_variable, "entity", "country_year", "country_code", "sector_code", "year"]].dropna().copy()
            x, names = design_matrix(sample, ai_variable, fixed_effects)
            result = clustered_ols(sample["log_productivity"].to_numpy(), x, sample["entity"].to_numpy())
            idx = names.index(ai_variable)
            beta = float(result["beta"][idx])
            se = float(result["se"][idx])
            t_stat = beta / se if se > 0 else np.nan
            df_clusters = int(result["clusters"]) - 1
            p_value = 2 * student_t.sf(abs(t_stat), df=df_clusters) if df_clusters > 0 else np.nan
            ci_critical = student_t.ppf(0.975, df=df_clusters) if df_clusters > 0 else 1.96
            rows.append(
                {
                    "specification": spec_name,
                    "ai_variable": ai_variable,
                    "indicator": label,
                    "beta_per_1pp": beta,
                    "clustered_se": se,
                    "t_stat": t_stat,
                    "p_value": p_value,
                    "ci95_low": beta - ci_critical * se,
                    "ci95_high": beta + ci_critical * se,
                    "effect_10pp_pct": 100 * (np.exp(10 * beta) - 1),
                    "n": int(result["n"]),
                    "clusters": int(result["clusters"]),
                    "r2_including_fe": float(result["r2"]),
                }
            )

    results = pd.DataFrame(rows)
    results.to_csv(args.output_dir / "resultados_modelos_panel.csv", index=False)
    results[results["specification"] == "M3_entity_countryyear_FE"].to_csv(
        args.output_dir / "modelo_preferido.csv", index=False
    )

    specification = pd.DataFrame(
        [
            ["M1_pooled_FE", "País + sector + año", "Compara niveles controlando diferencias aditivas observables por efectos fijos."],
            ["M2_entity_year_FE", "País-sector + año", "Usa variación temporal dentro de cada entidad y shocks comunes de año."],
            ["M3_entity_countryyear_FE", "País-sector + país-año", "Absorbe heterogeneidad permanente y shocks macro/nominales específicos de cada país-año."],
        ],
        columns=["specification", "fixed_effects", "interpretation"],
    )
    specification.to_csv(args.output_dir / "especificaciones.csv", index=False)


if __name__ == "__main__":
    main()
