"""Focused checks for SBS break-flag coverage."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest

import pandas as pd


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "analysis" / "06_auditar_flags_sbs.py"
spec = importlib.util.spec_from_file_location("auditar_flags_sbs", SCRIPT_PATH)
assert spec is not None and spec.loader is not None
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class AggregateSbsBreakFlagsTests(unittest.TestCase):
    def test_maps_source_breaks_across_size_classes_and_components(self) -> None:
        source = pd.DataFrame(
            [
                {"geo": "CZ", "nace_r2": "C", "time": 2021, "size_emp": "10-19", "indic_sbs": "AV_MEUR", "status": "b"},
                {"geo": "CZ", "nace_r2": "C", "time": 2021, "size_emp": "20-49", "indic_sbs": "AV_MEUR", "status": ""},
                {"geo": "CZ", "nace_r2": "C", "time": 2021, "size_emp": "50-249", "indic_sbs": "EMP_NR", "status": "b"},
                {"geo": "CZ", "nace_r2": "C", "time": 2021, "size_emp": "GE250", "indic_sbs": "EMP_NR", "status": "b"},
                {"geo": "FI", "nace_r2": "F", "time": 2023, "size_emp": "10-19", "indic_sbs": "AV_MEUR", "status": ""},
            ]
        )

        flags = module.aggregate_sbs_break_flags(source)

        self.assertEqual(flags.to_dict("records"), [
            {
                "country_code": "CZ",
                "sector_code": "C",
                "year": 2021,
                "av_break": True,
                "emp_break": True,
                "sbs_break": True,
                "raw_flagged_rows": 3,
            },
            {
                "country_code": "FI",
                "sector_code": "F",
                "year": 2023,
                "av_break": False,
                "emp_break": False,
                "sbs_break": False,
                "raw_flagged_rows": 0,
            },
        ])

    def test_sensitivity_scenarios_keep_full_core_and_apply_the_two_exclusions(self) -> None:
        robustness_spec = importlib.util.spec_from_file_location(
            "robustez_panel", Path(__file__).resolve().parents[1] / "analysis" / "04_robustez_panel.py"
        )
        assert robustness_spec is not None and robustness_spec.loader is not None
        robustness = importlib.util.module_from_spec(robustness_spec)
        robustness_spec.loader.exec_module(robustness)
        panel = pd.DataFrame(
            [
                {"country_code": "CZ", "sector_code": "C", "year": 2021, "core_complete": "Yes", "labour_productivity_keur": 10, "sbs_break": True},
                {"country_code": "CZ", "sector_code": "C", "year": 2023, "core_complete": "Yes", "labour_productivity_keur": 11, "sbs_break": False},
                {"country_code": "FI", "sector_code": "F", "year": 2021, "core_complete": "Yes", "labour_productivity_keur": 12, "sbs_break": False},
                {"country_code": "FI", "sector_code": "F", "year": 2023, "core_complete": "Yes", "labour_productivity_keur": 13, "sbs_break": False},
            ]
        )

        samples = robustness.sbs_flag_sensitivity_samples(panel)

        self.assertEqual(len(samples["full_core"]), 4)
        self.assertEqual(len(samples["drop_flagged_core_rows"]), 3)
        self.assertEqual(len(samples["drop_entities_with_flagged_core"]), 2)
        self.assertEqual(samples["drop_entities_with_flagged_core"]["entity"].unique().tolist(), ["FI_F"])

    def test_coverage_counts_only_core_observations_without_changing_main_sample(self) -> None:
        panel = pd.DataFrame(
            [
                {"country_code": "CZ", "sector_code": "C", "year": 2021, "core_complete": "Yes"},
                {"country_code": "FI", "sector_code": "F", "year": 2023, "core_complete": "Yes"},
                {"country_code": "CZ", "sector_code": "G", "year": 2021, "core_complete": "No"},
            ]
        )
        flags = pd.DataFrame(
            [
                {"country_code": "CZ", "sector_code": "C", "year": 2021, "av_break": True, "emp_break": True, "sbs_break": True, "raw_flagged_rows": 2},
                {"country_code": "CZ", "sector_code": "G", "year": 2021, "av_break": False, "emp_break": True, "sbs_break": True, "raw_flagged_rows": 1},
            ]
        )

        coverage, annotated_panel = module.build_coverage(panel, flags, source_rows=5)

        self.assertEqual(len(annotated_panel), 3)
        self.assertEqual(annotated_panel["sbs_break"].tolist(), [True, False, True])
        results = dict(zip(coverage["metric"], coverage["value"]))
        self.assertEqual(results["source_rows"], 5)
        self.assertEqual(results["core_rows"], 2)
        self.assertEqual(results["flagged_core_rows"], 1)
        self.assertEqual(results["flagged_core_both_components"], 1)
        self.assertEqual(results["flagged_core_employment_only"], 0)


if __name__ == "__main__":
    unittest.main()
