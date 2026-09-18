#!/usr/bin/env python3
"""Pruebas de robustez de panel para IA y productividad laboral aparente.

Las estimaciones son asociativas. El script usa linearmodels.AbsorbingLS para
absorber efectos fijos y reporta errores estándar agrupados por entidad
país-sector.

Escenarios incluidos:
- balanced_unweighted: muestra balanceada central, sin ponderar.
- core_unbalanced_unweighted: muestra central completa, sin exigir balance.
- balanced_employment_weighted: muestra balanceada ponderada por personas ocupadas.
- balanced_trim_p01_p99: muestra balanceada excluyendo extremos p1-p99 de productividad.

El objetivo no es elegir el resultado más conveniente, sino evaluar sensibilidad
de signo, magnitud y significatividad frente a decisiones razonables de muestra y
ponderación.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from linearmodels.iv import AbsorbingLS


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
    "M1_country_sector_year_FE": ["country_code", "sector_code", "year"],
    "M2_entity_year_FE": ["entity", "year"],
    "M3_entity_countryyear_FE": ["entity", "country_year"],
}

SCENARIOS = {
    "balanced_unweighted": {
        "label": "Muestra balanceada, sin ponderar",
        "sample": "balanced",
        "weights": None,
        "trim": None,
    },
    "core_unbalanced_unweighted": {
        "label": "Muestra central completa, sin ponderar",
        "sample": "core",
        "weights": None,
        "trim": None,
    },
    "balanced_employment_weighted": {
        "label": "Muestra balanceada, ponderada por empleo",
        "sample": "balanced",
        "weights": "persons_employed_ge10",
        "trim": None,
    },
    "balanced_trim_p01_p99": {
        "label": "Muestra balanceada, sin extremos p1-p99 de productividad",
        "sample": "balanced",
        "weights": None,
        "trim": (0.01, 0.99),
    },
}


def load_panel(input_path: Path) -> pd.DataFrame:
    if input_path.suffix.lower() == ".csv":
        data = pd.read_csv(input_path)
    else:
        data = pd.read_excel(input_path, sheet_name="Panel")

    data = data[data["labour_productivity_keur"] > 0].copy()
    data["log_productivity"] = np.log(data["labour_productivity_keur"])
    data["entity"] = data["country_code"].astype(str) + "_" + data["sector_code"].astype(str)
    data["country_year"] = data["country_code"].astype(str) + "_" + data["year"].astype(str)
    return data


def scenario_sample(data: pd.DataFrame, scenario: dict[str, object]) -> pd.DataFrame:
    if scenario["sample"] == "balanced":
        sample = data[(data["core_complete"] == "Yes") & (data["balanced_entity"] == "Yes")].copy()
    elif scenario["sample"] == "core":
        sample = data[data["core_complete"] == "Yes"].copy()
    else:
        raise ValueError(f"Unknown sample selector: {scenario['sample']}")

    trim = scenario["trim"]
    if trim is not None:
        low_q, high_q = trim
        low = sample["labour_productivity_keur"].quantile(float(low_q))
        high = sample["labour_productivity_keur"].quantile(float(high_q))
        sample = sample[(sample["labour_productivity_keur"] >= low) & (sample["labour_productivity_keur"] <= high)].copy()
        sample["trim_low_productivity_keur"] = low
        sample["trim_high_productivity_keur"] = high

    return sample


def estimate(
    data: pd.DataFrame,
    ai_variable: str,
    fixed_effects: list[str],
    weight_col: str | None = None,
) -> dict[str, float | int]:
    columns = list(dict.fromkeys(["log_productivity", ai_variable, "entity", *fixed_effects, *( [weight_col] if weight_col else [] )]))
    sample = data[columns].dropna().copy()
    if weight_col:
        sample = sample[sample[weight_col] > 0].copy()

    exog = pd.DataFrame({"const": 1.0, ai_variable: sample[ai_variable].astype(float)}, index=sample.index)
    absorb = sample[fixed_effects].astype("category")
    weights = sample[weight_col].astype(float) if weight_col else None

    model = AbsorbingLS(sample["log_productivity"].astype(float), exog, absorb=absorb, weights=weights)
    result = model.fit(cov_type="clustered", clusters=sample["entity"], debiased=True)
    ci = result.conf_int().loc[ai_variable]
    beta = float(result.params[ai_variable])

    return {
        "beta_per_1pp": beta,
        "clustered_se": float(result.std_errors[ai_variable]),
        "t_stat": float(result.tstats[ai_variable]),
        "p_value": float(result.pvalues[ai_variable]),
        "ci95_low": float(ci.iloc[0]),
        "ci95_high": float(ci.iloc[1]),
        "effect_10pp_pct": float(100 * (np.exp(10 * beta) - 1)),
        "n": int(result.nobs),
        "clusters": int(sample["entity"].nunique()),
        "r2_absorbing_ls": float(result.rsquared),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/modelos_panel_v0_2"))
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    data = load_panel(args.input)

    spec_rows = []
    robustness_rows = []
    scenario_rows = []

    for scenario_name, scenario in SCENARIOS.items():
        sample = scenario_sample(data, scenario)
        weight_col = scenario["weights"]
        scenario_rows.append(
            {
                "scenario": scenario_name,
                "label": scenario["label"],
                "rows_before_ai_dropna": len(sample),
                "entities": sample["entity"].nunique(),
                "countries": sample["country_code"].nunique(),
                "sectors": sample["sector_code"].nunique(),
                "years": ",".join(str(int(x)) for x in sorted(sample["year"].dropna().unique())),
                "weighted": weight_col is not None,
                "weight_col": weight_col or "",
                "trim": str(scenario["trim"] or ""),
                "productivity_min_keur": sample["labour_productivity_keur"].min(),
                "productivity_max_keur": sample["labour_productivity_keur"].max(),
            }
        )

        for ai_variable, indicator in AI_LABELS.items():
            # Main robustness comparison: preferred M3 across scenarios.
            estimates = estimate(sample, ai_variable, SPECS["M3_entity_countryyear_FE"], weight_col=weight_col)
            robustness_rows.append(
                {
                    "scenario": scenario_name,
                    "scenario_label": scenario["label"],
                    "specification": "M3_entity_countryyear_FE",
                    "ai_variable": ai_variable,
                    "indicator": indicator,
                    "weighted": weight_col is not None,
                    **estimates,
                }
            )

            # Specification comparison only for the unweighted balanced base scenario.
            if scenario_name == "balanced_unweighted":
                for spec_name, fixed_effects in SPECS.items():
                    spec_estimates = estimate(sample, ai_variable, fixed_effects, weight_col=None)
                    spec_rows.append(
                        {
                            "scenario": scenario_name,
                            "scenario_label": scenario["label"],
                            "specification": spec_name,
                            "ai_variable": ai_variable,
                            "indicator": indicator,
                            **spec_estimates,
                        }
                    )

    scenarios = pd.DataFrame(scenario_rows)
    robustness = pd.DataFrame(robustness_rows)
    specs = pd.DataFrame(spec_rows)

    scenarios.to_csv(args.output_dir / "escenarios_robustez.csv", index=False)
    robustness.to_csv(args.output_dir / "robustez_m3.csv", index=False)
    specs.to_csv(args.output_dir / "comparacion_especificaciones_balanceada.csv", index=False)

    adoption = robustness[robustness["ai_variable"] == "ai_any_pct"].copy()
    adoption.to_csv(args.output_dir / "robustez_adopcion_general.csv", index=False)

    summary = (
        robustness.groupby(["ai_variable", "indicator"], as_index=False)
        .agg(
            scenarios=("scenario", "nunique"),
            beta_min=("beta_per_1pp", "min"),
            beta_max=("beta_per_1pp", "max"),
            significant_5pct=("p_value", lambda s: int((s < 0.05).sum())),
            significant_10pct=("p_value", lambda s: int((s < 0.10).sum())),
        )
    )
    summary.to_csv(args.output_dir / "resumen_robustez_m3.csv", index=False)


if __name__ == "__main__":
    main()
