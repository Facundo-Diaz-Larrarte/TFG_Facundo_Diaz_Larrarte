#!/usr/bin/env python3
"""Valida los modelos de panel con una biblioteca econométrica estándar.

Este script replica las especificaciones preliminares de ``02_modelos_panel.py``
usando ``linearmodels.iv.AbsorbingLS`` para absorber efectos fijos de alta
dimensión y calcular errores estándar agrupados por entidad país-sector.

La comparación se usa como control de reproducibilidad. Es normal que los
errores estándar no coincidan exactamente con la implementación manual si la
biblioteca aplica una corrección de grados de libertad distinta.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from linearmodels.iv import AbsorbingLS
from linearmodels.panel import RandomEffects


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


def load_panel(input_path: Path) -> pd.DataFrame:
    if input_path.suffix.lower() == ".csv":
        panel = pd.read_csv(input_path)
        data = panel[panel["core_complete"] == "Yes"].copy()
    else:
        panel = pd.read_excel(input_path, sheet_name="Panel")
        data = panel[panel["core_complete"] == "Yes"].copy()

    data = data[data["labour_productivity_keur"] > 0].copy()
    data["log_productivity"] = np.log(data["labour_productivity_keur"])
    data["entity"] = data["country_code"].astype(str) + "_" + data["sector_code"].astype(str)
    data["country_year"] = data["country_code"].astype(str) + "_" + data["year"].astype(str)
    return data


def estimate_absorbing_ls(data: pd.DataFrame, ai_variable: str, fixed_effects: list[str]) -> dict[str, float | int]:
    columns = list(dict.fromkeys(["log_productivity", ai_variable, "entity", *fixed_effects]))
    sample = data[columns].dropna().copy()

    exog = pd.DataFrame({"const": 1.0, ai_variable: sample[ai_variable].astype(float)}, index=sample.index)
    absorb = sample[fixed_effects].astype("category")

    model = AbsorbingLS(sample["log_productivity"].astype(float), exog, absorb=absorb)
    result = model.fit(cov_type="clustered", clusters=sample["entity"], debiased=True)

    beta = float(result.params[ai_variable])
    se = float(result.std_errors[ai_variable])
    t_stat = float(result.tstats[ai_variable])
    p_value = float(result.pvalues[ai_variable])
    ci = result.conf_int().loc[ai_variable]

    return {
        "beta_per_1pp": beta,
        "clustered_se": se,
        "t_stat": t_stat,
        "p_value": p_value,
        "ci95_low": float(ci.iloc[0]),
        "ci95_high": float(ci.iloc[1]),
        "effect_10pp_pct": float(100 * (np.exp(10 * beta) - 1)),
        "n": int(result.nobs),
        "clusters": int(sample["entity"].nunique()),
        "r2_absorbing_ls": float(result.rsquared),
    }


def estimate_re_and_hausman(data: pd.DataFrame, ai_variable: str) -> dict[str, float | int]:
    sample = data[["log_productivity", ai_variable, "entity", "year"]].dropna().copy()
    sample["const"] = 1.0
    sample["ai_mean"] = sample.groupby("entity")[ai_variable].transform("mean")
    p_sample = sample.set_index(["entity", "year"])

    # Estimador de Efectos Aleatorios
    re_mod = RandomEffects(p_sample["log_productivity"], p_sample[["const", ai_variable]]).fit(
        cov_type="clustered", cluster_entity=True
    )
    # Contraste robusto de Hausman vía regresión auxiliar de Mundlak (1978) / Wooldridge (2010)
    mundlak_mod = RandomEffects(p_sample["log_productivity"], p_sample[["const", ai_variable, "ai_mean"]]).fit(
        cov_type="clustered", cluster_entity=True
    )
    wald = mundlak_mod.wald_test(formula="ai_mean = 0")

    return {
        "re_beta": float(re_mod.params[ai_variable]),
        "re_se": float(re_mod.std_errors[ai_variable]),
        "re_t_stat": float(re_mod.tstats[ai_variable]),
        "re_p_value": float(re_mod.pvalues[ai_variable]),
        "fe_within_beta": float(mundlak_mod.params[ai_variable]),
        "mundlak_hausman_stat": float(wald.stat),
        "mundlak_hausman_p": float(wald.pval),
        "reject_re_at_5pct": bool(wald.pval < 0.05),
        "n": int(re_mod.nobs),
        "entities": int(sample["entity"].nunique()),
    }


def build_comparison(output_dir: Path, validated: pd.DataFrame) -> None:
    preliminary_path = output_dir / "modelo_preferido.csv"
    if not preliminary_path.exists():
        return

    preliminary = pd.read_csv(preliminary_path)
    preferred = validated[validated["specification"] == "M3_entity_countryyear_FE"].copy()
    comparison = preliminary.merge(
        preferred,
        on=["specification", "ai_variable", "indicator"],
        suffixes=("_manual", "_linearmodels"),
    )
    comparison["beta_abs_diff"] = (comparison["beta_per_1pp_manual"] - comparison["beta_per_1pp_linearmodels"]).abs()
    comparison["se_abs_diff"] = (comparison["clustered_se_manual"] - comparison["clustered_se_linearmodels"]).abs()
    comparison["same_beta_1e_10"] = comparison["beta_abs_diff"] <= 1e-10
    comparison.to_csv(output_dir / "comparacion_modelo_preferido_linearmodels.csv", index=False)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/modelos_panel_v0_1"))
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    data = load_panel(args.input)

    # 1. AbsorbingLS para especificaciones de efectos fijos M1, M2 y M3
    rows = []
    for spec_name, fixed_effects in SPECS.items():
        for ai_variable, label in AI_LABELS.items():
            estimates = estimate_absorbing_ls(data, ai_variable, fixed_effects)
            rows.append(
                {
                    "estimator": "linearmodels.AbsorbingLS",
                    "specification": spec_name,
                    "ai_variable": ai_variable,
                    "indicator": label,
                    **estimates,
                }
            )

    results = pd.DataFrame(rows)
    results.to_csv(args.output_dir / "resultados_modelos_panel_linearmodels.csv", index=False)
    results[results["specification"] == "M3_entity_countryyear_FE"].to_csv(
        args.output_dir / "modelo_preferido_linearmodels.csv", index=False
    )
    build_comparison(args.output_dir, results)

    # 2. Estimación de Efectos Aleatorios (RE) y Test de Hausman
    re_rows = []
    for ai_variable, label in AI_LABELS.items():
        re_est = estimate_re_and_hausman(data, ai_variable)
        re_rows.append(
            {
                "ai_variable": ai_variable,
                "indicator": label,
                **re_est,
            }
        )
    re_df = pd.DataFrame(re_rows)
    re_df.to_csv(args.output_dir / "modelos_re_hausman.csv", index=False)


if __name__ == "__main__":
    main()
