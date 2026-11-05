#!/usr/bin/env python3
"""Report SBS break-status coverage and M3 sensitivity without altering the panel."""

from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path
from types import ModuleType

import pandas as pd


SOURCE_KEY = ["geo", "nace_r2", "time", "size_emp", "indic_sbs"]
PANEL_KEY = ["country_code", "sector_code", "year"]


def aggregate_sbs_break_flags(source: pd.DataFrame) -> pd.DataFrame:
    """Map raw SBS ``status=b`` flags to country-sector-year observations."""
    raw = source.copy()
    raw["_is_break"] = raw["status"].fillna("").eq("b")
    raw["_av_break"] = raw["_is_break"] & raw["indic_sbs"].eq("AV_MEUR")
    raw["_emp_break"] = raw["_is_break"] & raw["indic_sbs"].eq("EMP_NR")

    flags = (
        raw.groupby(["geo", "nace_r2", "time"], as_index=False)
        .agg(
            av_break=("_av_break", "any"),
            emp_break=("_emp_break", "any"),
            raw_flagged_rows=("_is_break", "sum"),
        )
        .rename(columns={"geo": "country_code", "nace_r2": "sector_code", "time": "year"})
    )
    flags["year"] = pd.to_numeric(flags["year"], errors="raise").astype(int)
    flags["sbs_break"] = flags["av_break"] | flags["emp_break"]
    return flags[PANEL_KEY + ["av_break", "emp_break", "sbs_break", "raw_flagged_rows"]].sort_values(PANEL_KEY).reset_index(drop=True)


def build_coverage(
    panel: pd.DataFrame, flags: pd.DataFrame, source_rows: int
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Attach derived flags in memory and return transparent coverage metrics."""
    annotated = panel.merge(flags, on=PANEL_KEY, how="left", validate="one_to_one")
    for column in ["av_break", "emp_break", "sbs_break"]:
        annotated[column] = annotated[column].eq(True)
    annotated["raw_flagged_rows"] = annotated["raw_flagged_rows"].fillna(0).astype(int)

    core = annotated[annotated["core_complete"].eq("Yes")].copy()
    flagged_core = core[core["sbs_break"]]
    metrics = [
        ("source_rows", source_rows),
        ("panel_rows", len(annotated)),
        ("core_rows", len(core)),
        ("flagged_panel_rows", int(annotated["sbs_break"].sum())),
        ("flagged_core_rows", len(flagged_core)),
        ("flagged_core_both_components", int((flagged_core["av_break"] & flagged_core["emp_break"]).sum())),
        ("flagged_core_value_added_only", int((flagged_core["av_break"] & ~flagged_core["emp_break"]).sum())),
        ("flagged_core_employment_only", int((~flagged_core["av_break"] & flagged_core["emp_break"]).sum())),
        ("flagged_core_raw_break_rows", int(flagged_core["raw_flagged_rows"].sum())),
        ("flagged_core_countries", int(flagged_core["country_code"].nunique())),
        ("flagged_core_country_codes", ",".join(sorted(flagged_core["country_code"].unique()))),
    ]
    return pd.DataFrame(metrics, columns=["metric", "value"]), annotated


def source_coverage(source: pd.DataFrame) -> pd.DataFrame:
    """Return source-level checks without hard-coding expected counts."""
    is_break = source["status"].fillna("").eq("b")
    break_rows = source[is_break]
    metrics = [
        ("source_unique_key_rows", int(source.drop_duplicates(SOURCE_KEY).shape[0])),
        ("raw_break_rows", int(is_break.sum())),
        ("raw_break_value_added_rows", int((break_rows["indic_sbs"] == "AV_MEUR").sum())),
        ("raw_break_employment_rows", int((break_rows["indic_sbs"] == "EMP_NR").sum())),
        ("raw_break_years", ",".join(str(int(year)) for year in sorted(break_rows["time"].unique()))),
    ]
    return pd.DataFrame(metrics, columns=["metric", "value"])


def load_robustness_module() -> ModuleType:
    path = Path(__file__).with_name("04_robustez_panel.py")
    spec = importlib.util.spec_from_file_location("robustez_panel", path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot import canonical robustness estimator from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-workbook", type=Path, required=True)
    parser.add_argument("--panel", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/modelos_panel_v0_2"))
    args = parser.parse_args()

    coverage_path = args.output_dir / "cobertura_flags_sbs.csv"
    sensitivity_path = args.output_dir / "sensibilidad_flags_sbs.csv"
    existing = [path for path in [coverage_path, sensitivity_path] if path.exists()]
    if existing:
        raise FileExistsError("Refusing to overwrite requested output(s): " + ", ".join(map(str, existing)))
    args.output_dir.mkdir(parents=True, exist_ok=True)

    source = pd.read_excel(args.source_workbook, sheet_name="Fuente_SBS")
    panel = pd.read_csv(args.panel) if args.panel.suffix.lower() == ".csv" else pd.read_excel(args.panel, sheet_name="Panel")
    flags = aggregate_sbs_break_flags(source)
    panel_coverage, annotated_panel = build_coverage(panel, flags, source_rows=len(source))
    coverage = pd.concat([source_coverage(source), panel_coverage], ignore_index=True)

    robustness = load_robustness_module()
    sensitivity = robustness.estimate_sbs_flag_sensitivity(annotated_panel)

    coverage.to_csv(coverage_path, index=False)
    sensitivity.to_csv(sensitivity_path, index=False)


if __name__ == "__main__":
    main()
