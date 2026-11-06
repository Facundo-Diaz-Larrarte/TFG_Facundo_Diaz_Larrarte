#!/usr/bin/env python3
"""Reconstruye la asociación nominal entre IA y productividad por sector.

Este análisis reproduce la especificación documentada para T19; no recupera
código original. Sus coeficientes son asociaciones descriptivas, no efectos
causales.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from linearmodels.iv import AbsorbingLS
from scipy.stats import chi2


SECTOR_ORDER = ["C", "G", "M", "H", "J", "N", "F", "L", "I"]
INTERPRETATION = (
    "Asociación descriptiva no causal; reconstrucción de la especificación "
    "documentada, no recuperación de código original."
)


def construct_sample(panel: pd.DataFrame) -> pd.DataFrame:
    """Build the documented core nominal-productivity estimation sample."""
    sample = panel[
        (panel["core_complete"] == "Yes")
        & (panel["labour_productivity_keur"] > 0)
    ].copy()
    sample["log_productivity"] = np.log(sample["labour_productivity_keur"])
    sample["entity"] = sample["country_code"].astype(str) + "_" + sample["sector_code"].astype(str)
    sample["country_year"] = sample["country_code"].astype(str) + "_" + sample["year"].astype(str)
    return sample


def holm_adjust_pvalues(p_values: pd.Series) -> pd.Series:
    """Return Holm-adjusted p-values, preserving input order and missing values."""
    raw_values = p_values.to_numpy(dtype=float)
    adjusted = np.full(len(raw_values), np.nan, dtype=float)
    valid_positions = np.flatnonzero(~np.isnan(raw_values))
    if len(valid_positions):
        sorted_positions = valid_positions[np.argsort(raw_values[valid_positions], kind="mergesort")]
        scaled = np.minimum(
            raw_values[sorted_positions] * (len(raw_values) - np.arange(len(sorted_positions))),
            1.0,
        )
        adjusted[sorted_positions] = np.maximum.accumulate(scaled)
    return pd.Series(adjusted, index=p_values.index, name="p_adjust_holm")


def sector_contrasts(
    params: pd.Series,
    covariance: pd.DataFrame,
    sectors: list[str],
    clusters: int,
) -> pd.DataFrame:
    """Calculate sector slopes from the interaction covariance matrix (w'Vw)."""
    rows: list[dict[str, float | str]] = []
    base_name = "ai_any_pct"
    for sector in sectors:
        weights = pd.Series(0.0, index=params.index)
        weights.loc[base_name] = 1.0
        if sector != "C":
            weights.loc[f"ai_any_pct_x_sector_{sector}"] = 1.0
        beta = float(weights @ params)
        variance = float(weights @ covariance @ weights)
        se = float(np.sqrt(max(variance, 0.0)))
        z_stat = beta / se if se > 0 else np.nan
        wald_chi2 = z_stat**2 if np.isfinite(z_stat) else np.nan
        p_value = float(chi2.sf(wald_chi2, df=1)) if np.isfinite(wald_chi2) else np.nan
        rows.append(
            {
                "sector_code": sector,
                "beta_per_1pp": beta,
                "clustered_se": se,
                "z_stat": z_stat,
                "wald_chi2": wald_chi2,
                "p_value": p_value,
                "effect_10pp_pct": float(100 * np.expm1(10 * beta)),
                "contrast": "w'Vw: ai_any_pct + sector interaction (C base)",
            }
        )
    contrasts = pd.DataFrame(rows)
    contrasts.insert(
        contrasts.columns.get_loc("p_value") + 1,
        "p_adjust_holm",
        holm_adjust_pvalues(contrasts["p_value"]),
    )
    return contrasts


def estimate_sector_interactions(sample: pd.DataFrame) -> pd.DataFrame:
    """Estimate absorbed country-sector and country-year FE interactions."""
    sectors = [sector for sector in SECTOR_ORDER if sector in set(sample["sector_code"])]
    if "C" not in sectors:
        raise ValueError("Sector C is required as the interaction base category.")

    interaction_names = [f"ai_any_pct_x_sector_{sector}" for sector in sectors if sector != "C"]
    model_columns = ["log_productivity", "ai_any_pct", "entity", "country_year", "sector_code"]
    model_data = sample[model_columns].dropna().copy()
    if model_data.empty:
        raise ValueError("No complete observations remain for the sector-interaction model.")

    exog = pd.DataFrame(
        {"const": 1.0, "ai_any_pct": model_data["ai_any_pct"].astype(float)},
        index=model_data.index,
    )
    for sector, interaction_name in zip((s for s in sectors if s != "C"), interaction_names):
        exog[interaction_name] = model_data["ai_any_pct"].astype(float) * (
            model_data["sector_code"] == sector
        ).astype(float)

    model = AbsorbingLS(
        model_data["log_productivity"].astype(float),
        exog,
        absorb=model_data[["entity", "country_year"]].astype("category"),
    )
    result = model.fit(cov_type="clustered", clusters=model_data["entity"], debiased=True)
    clusters = int(model_data["entity"].nunique())
    contrasts = sector_contrasts(result.params, result.cov, sectors, clusters)
    sector_names = (
        sample[["sector_code", "sector_name"]]
        .drop_duplicates("sector_code")
        .set_index("sector_code")["sector_name"]
    )
    contrasts.insert(1, "sector_name", contrasts["sector_code"].map(sector_names))
    contrasts["n"] = int(result.nobs)
    contrasts["clusters"] = clusters
    contrasts["outcome"] = "log(labour_productivity_keur), nominal"
    contrasts["predictor"] = "ai_any_pct (percentage points)"
    contrasts["fixed_effects"] = "country-sector and country-year absorbed fixed effects"
    contrasts["covariance"] = "clustered by country-sector entity; debiased"
    contrasts["analysis_type"] = "association/reconstruction; non-causal; not original-code recovery"
    contrasts["interpretation"] = INTERPRETATION
    return contrasts


def validate_output_path(output: Path, force: bool) -> None:
    """Reject replacement unless the caller explicitly requests it."""
    if output.exists() and not force:
        raise FileExistsError(f"Refusing to overwrite existing output: {output}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path("data/processed/panel_analitico.csv"))
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("outputs/modelos_panel_sectorial_v0_1/heterogeneidad_sectorial.csv"),
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="replace an existing target output; default is to refuse replacement",
    )
    args = parser.parse_args()

    validate_output_path(args.output, force=args.force)
    if not args.input.exists():
        raise FileNotFoundError(f"Input file not found: {args.input}")

    panel = pd.read_csv(args.input)
    results = estimate_sector_interactions(construct_sample(panel))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    results.to_csv(args.output, index=False)

    print("Nominal sector-interaction association reconstruction complete (not causal; not original-code recovery).")
    print(f"Wrote {args.output}")
    print(results.to_string(index=False))


if __name__ == "__main__":
    main()
