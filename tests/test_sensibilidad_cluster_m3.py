"""Focused checks for the M3 clustering covariance sensitivity."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch

import pandas as pd


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "analysis" / "08_sensibilidad_cluster_m3.py"
spec = importlib.util.spec_from_file_location("sensibilidad_cluster_m3", SCRIPT_PATH)
assert spec is not None and spec.loader is not None
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class FakeResult:
    params = pd.Series({"const": 0.0, "ai_any_pct": 0.02})
    std_errors = pd.Series({"const": 0.0, "ai_any_pct": 0.01})
    tstats = pd.Series({"const": 0.0, "ai_any_pct": 2.0})
    pvalues = pd.Series({"const": 1.0, "ai_any_pct": 0.05})
    nobs = 4

    @staticmethod
    def conf_int() -> pd.DataFrame:
        return pd.DataFrame(
            {0: [-0.01, 0.00], 1: [0.01, 0.04]},
            index=["const", "ai_any_pct"],
        )


class FakeAbsorbingLS:
    calls: list[dict[str, object]] = []

    def __init__(self, dependent: pd.Series, exog: pd.DataFrame, absorb: pd.DataFrame) -> None:
        self.dependent = dependent.copy()
        self.exog = exog.copy()
        self.absorb = absorb.copy()

    def fit(self, **kwargs: object) -> FakeResult:
        FakeAbsorbingLS.calls.append(
            {
                "dependent": self.dependent,
                "exog": self.exog,
                "absorb": self.absorb,
                "fit_kwargs": kwargs,
            }
        )
        return FakeResult()


class SensibilidadClusterM3Tests(unittest.TestCase):
    def test_two_way_clustering_uses_same_m3_design_as_one_way_entity_clustering(self) -> None:
        panel = pd.DataFrame(
            [
                {"country_code": "BE", "sector_code": "C", "year": 2021, "core_complete": "Yes", "labour_productivity_keur": 10.0, "ai_any_pct": 5.0},
                {"country_code": "BE", "sector_code": "G", "year": 2021, "core_complete": "Yes", "labour_productivity_keur": 12.0, "ai_any_pct": 6.0},
                {"country_code": "BE", "sector_code": "C", "year": 2023, "core_complete": "Yes", "labour_productivity_keur": 11.0, "ai_any_pct": 7.0},
                {"country_code": "BE", "sector_code": "G", "year": 2023, "core_complete": "Yes", "labour_productivity_keur": 13.0, "ai_any_pct": 8.0},
                {"country_code": "FI", "sector_code": "C", "year": 2021, "core_complete": "No", "labour_productivity_keur": 14.0, "ai_any_pct": 9.0},
                {"country_code": "FI", "sector_code": "G", "year": 2021, "core_complete": "Yes", "labour_productivity_keur": 15.0, "ai_any_pct": None},
            ]
        )

        FakeAbsorbingLS.calls = []
        with patch.object(module, "AbsorbingLS", FakeAbsorbingLS):
            results = module.estimate_sensitivity(panel)

        self.assertEqual(results["cluster_scheme"].tolist(), ["one_way_entity", "two_way_entity_country_year"])
        self.assertEqual(results["n"].tolist(), [4, 4])
        self.assertEqual(results["entity_clusters"].tolist(), [2, 2])
        self.assertEqual(results["country_year_clusters"].tolist(), [2, 2])
        self.assertEqual(results["country_clusters"].tolist(), [1, 1])
        self.assertEqual(results["entity_cluster_size_counts"].tolist(), ["2:2", "2:2"])
        self.assertEqual(results["country_year_cluster_size_counts"].tolist(), ["2:2", "2:2"])
        self.assertEqual(results["country_cluster_size_counts"].tolist(), ["4:1", "4:1"])

        self.assertEqual(len(FakeAbsorbingLS.calls), 2)
        one_way, two_way = FakeAbsorbingLS.calls
        pd.testing.assert_series_equal(one_way["dependent"], two_way["dependent"])
        pd.testing.assert_frame_equal(one_way["exog"], two_way["exog"])
        pd.testing.assert_frame_equal(one_way["absorb"], two_way["absorb"])
        self.assertEqual(one_way["fit_kwargs"]["cov_type"], "clustered")
        self.assertTrue(one_way["fit_kwargs"]["debiased"])
        self.assertEqual(two_way["fit_kwargs"]["cov_type"], "clustered")
        self.assertTrue(two_way["fit_kwargs"]["debiased"])
        self.assertEqual(one_way["fit_kwargs"]["clusters"].columns.tolist(), ["entity"])
        self.assertEqual(two_way["fit_kwargs"]["clusters"].columns.tolist(), ["entity", "country_year"])
        pd.testing.assert_frame_equal(
            one_way["fit_kwargs"]["clusters"],
            two_way["fit_kwargs"]["clusters"][["entity"]],
        )

    def test_existing_output_requires_explicit_force(self) -> None:
        output = Path("outputs/inferencia_v0_1/sensibilidad_cluster_m3.csv")

        with patch.object(Path, "exists", return_value=True):
            with self.assertRaisesRegex(FileExistsError, "Refusing to overwrite"):
                module.validate_output_path(output, force=False)
            module.validate_output_path(output, force=True)


if __name__ == "__main__":
    unittest.main()
