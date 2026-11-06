"""Focused checks for the nominal sector-interaction reconstruction."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd
from scipy.stats import chi2, t as student_t


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "analysis" / "07_heterogeneidad_sectorial.py"
spec = importlib.util.spec_from_file_location("heterogeneidad_sectorial", SCRIPT_PATH)
assert spec is not None and spec.loader is not None
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class HeterogeneidadSectorialTests(unittest.TestCase):
    def test_construct_sample_keeps_only_valid_core_observations(self) -> None:
        panel = pd.DataFrame(
            [
                {"country_code": "BE", "sector_code": "C", "year": 2021, "core_complete": "Yes", "labour_productivity_keur": 10.0, "ai_any_pct": 5.0},
                {"country_code": "BE", "sector_code": "G", "year": 2023, "core_complete": "No", "labour_productivity_keur": 20.0, "ai_any_pct": 6.0},
                {"country_code": "FI", "sector_code": "M", "year": 2024, "core_complete": "Yes", "labour_productivity_keur": 0.0, "ai_any_pct": 7.0},
            ]
        )

        sample = module.construct_sample(panel)

        self.assertEqual(sample.index.tolist(), [0])
        self.assertEqual(sample["entity"].tolist(), ["BE_C"])
        self.assertEqual(sample["country_year"].tolist(), ["BE_2021"])
        self.assertAlmostEqual(sample.loc[0, "log_productivity"], np.log(10.0))

    def test_sector_contrasts_use_full_covariance_for_interaction_slope(self) -> None:
        params = pd.Series(
            {"ai_any_pct": 0.10, "ai_any_pct_x_sector_G": 0.05}, dtype=float
        )
        covariance = pd.DataFrame(
            [[0.04, 0.01], [0.01, 0.09]],
            index=params.index,
            columns=params.index,
        )

        contrasts = module.sector_contrasts(params, covariance, ["C", "G"], clusters=10)

        c_row = contrasts.loc[contrasts["sector_code"] == "C"].iloc[0]
        g_row = contrasts.loc[contrasts["sector_code"] == "G"].iloc[0]
        self.assertAlmostEqual(c_row["beta_per_1pp"], 0.10)
        self.assertAlmostEqual(c_row["clustered_se"], 0.20)
        self.assertAlmostEqual(g_row["beta_per_1pp"], 0.15)
        self.assertAlmostEqual(g_row["clustered_se"], np.sqrt(0.15))
        self.assertAlmostEqual(g_row["z_stat"], 0.15 / np.sqrt(0.15))
        self.assertAlmostEqual(g_row["wald_chi2"], (0.15 / np.sqrt(0.15)) ** 2)
        self.assertAlmostEqual(g_row["effect_10pp_pct"], 100 * np.expm1(1.5))

    def test_sector_contrasts_report_asymptotic_wald_inference_contract(self) -> None:
        params = pd.Series({"ai_any_pct": 0.20}, dtype=float)
        covariance = pd.DataFrame([[0.01]], index=params.index, columns=params.index)

        contrasts = module.sector_contrasts(params, covariance, ["C"], clusters=10)

        self.assertEqual(
            contrasts.columns.tolist(),
            [
                "sector_code",
                "beta_per_1pp",
                "clustered_se",
                "z_stat",
                "wald_chi2",
                "p_value",
                "p_adjust_holm",
                "effect_10pp_pct",
                "contrast",
            ],
        )
        row = contrasts.iloc[0]
        self.assertAlmostEqual(row["z_stat"], 2.0)
        self.assertAlmostEqual(row["wald_chi2"], 4.0)
        self.assertAlmostEqual(row["p_value"], chi2.sf(4.0, df=1))
        self.assertNotAlmostEqual(row["p_value"], 2 * student_t.sf(2.0, df=9))

    def test_holm_adjustment_preserves_order_ties_and_nan(self) -> None:
        raw_p_values = pd.Series([0.04, 0.01, np.nan, 0.01, 0.03, 0.50, 0.20, 0.80, 0.04])

        adjusted = module.holm_adjust_pvalues(raw_p_values)

        expected = pd.Series(
            [0.24, 0.09, np.nan, 0.09, 0.21, 1.0, 0.80, 1.0, 0.24],
            name="p_adjust_holm",
        )
        pd.testing.assert_series_equal(adjusted, expected)

    def test_existing_output_requires_explicit_force(self) -> None:
        output = Path("outputs/modelos_panel_sectorial_v0_1/heterogeneidad_sectorial.csv")

        with patch.object(Path, "exists", return_value=True):
            with self.assertRaisesRegex(FileExistsError, "Refusing to overwrite"):
                module.validate_output_path(output, force=False)
            module.validate_output_path(output, force=True)


if __name__ == "__main__":
    unittest.main()
