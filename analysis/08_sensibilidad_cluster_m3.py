#!/usr/bin/env python3
"""Covariance sensitivity for canonical nominal-productivity M3.

This preserves the canonical M3 sample, regressors, unweighted estimator, and
absorbed country-sector and country-year fixed effects.  It compares its
one-way country-sector clustering with two-way clustering by country-sector
and country-year.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from linearmodels.iv import AbsorbingLS


INPUT_DEFAULT = Path("data/processed/panel_analitico.csv")
OUTPUT_DEFAULT = Path("outputs/inferencia_v0_1/sensibilidad_cluster_m3.csv")
AI_VARIABLE = "ai_any_pct"


def construct_sample(panel: pd.DataFrame) -> pd.DataFrame:
    """Construct the canonical M3 core sample with nominal log productivity."""
    sample = panel[
        (panel["core_complete"] == "Yes")
        & (panel["labour_productivity_keur"] > 0)
    ].copy()
    sample["log_productivity"] = np.log(sample["labour_productivity_keur"])
    sample["entity"] = sample["country_code"].astype(str) + "_" + sample["sector_code"].astype(str)
    sample["country_year"] = sample["country_code"].astype(str) + "_" + sample["year"].astype(str)
    return sample


def construct_design(sample: pd.DataFrame) -> pd.DataFrame:
    """Retain the single complete-case design used by both covariance fits."""
    columns = ["log_productivity", AI_VARIABLE, "entity", "country_year", "country_code"]
    design = sample[columns].dropna().copy()
    if design.empty:
        raise ValueError("No complete observations remain for canonical M3.")
    return design


def cluster_size_counts(design: pd.DataFrame, cluster_column: str) -> str:
    """Return realized group-size frequencies as ``observations:groups``."""
    group_sizes = design.groupby(cluster_column, observed=True).size()
    size_counts = group_sizes.value_counts().sort_index()
    return ";".join(f"{int(size)}:{int(count)}" for size, count in size_counts.items())


def estimate_m3(
    design: pd.DataFrame,
    cluster_columns: list[str],
    cluster_scheme: str,
) -> dict[str, float | int | str]:
    """Fit canonical M3 with the requested one- or two-way cluster covariance."""
    exog = pd.DataFrame(
        {"const": 1.0, AI_VARIABLE: design[AI_VARIABLE].astype(float)},
        index=design.index,
    )
    absorb = design[["entity", "country_year"]].astype("category")
    # linearmodels 7.0 two-way covariance requires numeric cluster labels.
    clusters = design[cluster_columns].apply(lambda column: pd.Categorical(column).codes)
    model = AbsorbingLS(design["log_productivity"].astype(float), exog, absorb=absorb)
    result = model.fit(cov_type="clustered", clusters=clusters, debiased=True)
    ci = result.conf_int().loc[AI_VARIABLE]

    return {
        "cluster_scheme": cluster_scheme,
        "covariance": "clustered; debiased=True",
        "cluster_dimensions": "+".join(cluster_columns),
        "beta_per_1pp": float(result.params[AI_VARIABLE]),
        "clustered_se": float(result.std_errors[AI_VARIABLE]),
        "t_stat": float(result.tstats[AI_VARIABLE]),
        "p_value": float(result.pvalues[AI_VARIABLE]),
        "ci95_low": float(ci.iloc[0]),
        "ci95_high": float(ci.iloc[1]),
        "n": int(result.nobs),
        "entity_clusters": int(design["entity"].nunique()),
        "country_year_clusters": int(design["country_year"].nunique()),
        "country_clusters": int(design["country_code"].nunique()),
        "entity_cluster_size_counts": cluster_size_counts(design, "entity"),
        "country_year_cluster_size_counts": cluster_size_counts(design, "country_year"),
        "country_cluster_size_counts": cluster_size_counts(design, "country_code"),
        "outcome": "log(labour_productivity_keur), nominal",
        "predictor": "ai_any_pct (percentage points)",
        "fixed_effects": "country-sector and country-year absorbed fixed effects",
        "weights": "unweighted",
    }


def estimate_sensitivity(panel: pd.DataFrame) -> pd.DataFrame:
    """Compare covariance estimators on the exact same canonical M3 design."""
    design = construct_design(construct_sample(panel))
    estimates = [
        estimate_m3(design, ["entity"], "one_way_entity"),
        estimate_m3(design, ["entity", "country_year"], "two_way_entity_country_year"),
    ]
    return pd.DataFrame(estimates)


def validate_output_path(output: Path, force: bool) -> None:
    """Reject replacement unless the caller explicitly requests it."""
    if output.exists() and not force:
        raise FileExistsError(f"Refusing to overwrite existing output: {output}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT_DEFAULT)
    parser.add_argument("--output", type=Path, default=OUTPUT_DEFAULT)
    parser.add_argument(
        "--force",
        action="store_true",
        help="replace an existing target output; default is to refuse replacement",
    )
    args = parser.parse_args()

    validate_output_path(args.output, force=args.force)
    if not args.input.exists():
        raise FileNotFoundError(f"Input file not found: {args.input}")

    results = estimate_sensitivity(pd.read_csv(args.input))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    results.to_csv(args.output, index=False)

    print("Canonical M3 covariance sensitivity complete (associative, not causal).")
    print(f"Wrote {args.output}")
    print(results.to_string(index=False))


if __name__ == "__main__":
    main()
