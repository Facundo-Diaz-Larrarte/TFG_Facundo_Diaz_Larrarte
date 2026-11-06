"""Focused checks for T60's canonical one-way entity-cluster inference."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd
from scipy.stats import t as student_t


ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, relative_path: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


modelos_panel = load_module("modelos_panel_t60", "analysis/02_modelos_panel.py")
validacion_linearmodels = load_module(
    "validacion_linearmodels_t60", "analysis/03_validacion_linearmodels.py"
)


class CanonicalClusterInferenceTests(unittest.TestCase):
    def test_rank_deficient_fixed_effect_design_uses_effective_rank_for_cr1(self) -> None:
        sample = pd.DataFrame(
            [
                {
                    "entity": f"{country}_{sector}",
                    "country_year": f"{country}_{year}",
                    "ai_any_pct": float((1 if sector == "S1" else 2) * (year - 2019)),
                }
                for country in ("A", "B")
                for sector in ("S1", "S2")
                for year in (2020, 2021, 2022)
            ]
        )
        x, _ = modelos_panel.design_matrix(sample, "ai_any_pct", ["entity", "country_year"])
        y = 1.0 + 0.5 * sample["ai_any_pct"].to_numpy()
        clusters = sample["entity"].to_numpy()

        result = modelos_panel.clustered_ols(y, x, clusters)

        # The two disconnected country FE components make one nominal dummy redundant.
        self.assertEqual(x.shape, (12, 10))
        self.assertEqual(result["rank"], 9)
        self.assertEqual(result["inference_df"], 3)
        self.assertAlmostEqual(result["cr1_correction"], (4 / 3) * (11 / (12 - 9)))
        self.assertNotAlmostEqual(result["cr1_correction"], (4 / 3) * (11 / (12 - 10)))

    def test_p_values_and_confidence_intervals_use_cluster_minus_one_t_distribution(self) -> None:
        inference = modelos_panel.clustered_inference(beta=0.4, se=0.2, clusters=5)

        self.assertEqual(inference["inference_df"], 4)
        self.assertAlmostEqual(inference["t_stat"], 2.0)
        self.assertAlmostEqual(inference["p_value"], 2 * student_t.sf(2.0, df=4))
        critical_value = student_t.ppf(0.975, df=4)
        self.assertAlmostEqual(inference["ci95_low"], 0.4 - critical_value * 0.2)
        self.assertAlmostEqual(inference["ci95_high"], 0.4 + critical_value * 0.2)


class PreferredOutputOwnershipTests(unittest.TestCase):
    def test_linearmodels_validation_preserves_canonical_preferred_output_and_writes_comparison(self) -> None:
        canonical = pd.DataFrame(
            [
                {
                    "specification": "M3_entity_countryyear_FE",
                    "ai_variable": "ai_any_pct",
                    "indicator": "Adopción general",
                    "beta_per_1pp": 0.02,
                    "clustered_se": 0.01,
                }
            ]
        )
        validated = pd.DataFrame(
            [
                {
                    "estimator": "linearmodels.AbsorbingLS",
                    "specification": "M3_entity_countryyear_FE",
                    "ai_variable": "ai_any_pct",
                    "indicator": "Adopción general",
                    "beta_per_1pp": 0.021,
                    "clustered_se": 0.015,
                }
            ]
        )
        writes: dict[str, pd.DataFrame] = {}

        def capture_to_csv(frame: pd.DataFrame, path: Path, **_: object) -> None:
            writes[Path(path).name] = frame.copy()

        with (
            patch.object(Path, "exists", return_value=True),
            patch.object(validacion_linearmodels.pd, "read_csv", return_value=canonical),
            patch.object(pd.DataFrame, "to_csv", autospec=True, side_effect=capture_to_csv),
        ):
            validacion_linearmodels.build_comparison(Path("canonical-output"), validated)

        self.assertNotIn("modelo_preferido.csv", writes)
        self.assertIn("modelo_preferido_manual.csv", writes)
        self.assertIn("comparacion_modelo_preferido_linearmodels.csv", writes)
        comparison = writes["comparacion_modelo_preferido_linearmodels.csv"]
        self.assertAlmostEqual(comparison.loc[0, "se_abs_diff"], 0.005)
        self.assertFalse(comparison.loc[0, "same_beta_1e_10"])


if __name__ == "__main__":
    unittest.main()
