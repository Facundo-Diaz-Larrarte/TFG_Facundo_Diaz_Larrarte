#!/usr/bin/env python3
"""Robustez con productividad laboral deflactada por precios sectoriales.

Descarga de Eurostat ``nama_10_a64`` valor agregado bruto a precios corrientes
(CP_MEUR) y volúmenes encadenados (CLV20_MEUR) para los países, sectores y años
presentes en la base analítica. Con esos datos construye un deflactor
país-sector-año, normalizado a 2021=1 dentro de cada entidad país-sector, y lo
aplica a la productividad laboral aparente SBS.

La corrección es una aproximación: el numerador de productividad proviene de SBS
(empresas de 10+ ocupados), mientras que el deflactor proviene de cuentas
nacionales por industria para el sector agregado completo.
"""

from __future__ import annotations

import argparse
import json
import ssl
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from linearmodels.iv import AbsorbingLS


EUROSTAT_API = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nama_10_a64"
BASE_YEAR = 2021
UNITS = {
    "CP_MEUR": "gva_current_meur_na",
    "CLV20_MEUR": "gva_volume_2020_meur_na",
}

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


def build_url(unit: str, countries: list[str], sectors: list[str], years: list[int]) -> str:
    params: list[tuple[str, str]] = [
        ("format", "JSON"),
        ("lang", "en"),
        ("freq", "A"),
        ("unit", unit),
        ("na_item", "B1G"),
    ]
    params.extend(("nace_r2", sector) for sector in sectors)
    params.extend(("geo", country) for country in countries)
    params.extend(("time", str(year)) for year in years)
    return EUROSTAT_API + "?" + urllib.parse.urlencode(params)


def fetch_json(url: str) -> dict[str, Any]:
    # Eurostat certificates can fail in some local Windows Python installs. This
    # script downloads only public Eurostat JSON and does not transmit secrets.
    context = ssl._create_unverified_context()
    with urllib.request.urlopen(url, timeout=90, context=context) as response:
        return json.loads(response.read().decode("utf-8"))


def jsonstat_to_frame(data: dict[str, Any], value_name: str) -> pd.DataFrame:
    ids = data["id"]
    sizes = data["size"]
    dimensions = data["dimension"]
    values = {int(k): v for k, v in data.get("value", {}).items()}
    statuses = {int(k): v for k, v in data.get("status", {}).items()}

    multipliers: list[int] = []
    for pos in range(len(sizes)):
        multiplier = 1
        for later_size in sizes[pos + 1 :]:
            multiplier *= later_size
        multipliers.append(multiplier)

    dim_items: list[list[tuple[str, int]]] = []
    for dim in ids:
        index_map = dimensions[dim]["category"]["index"]
        dim_items.append(sorted(index_map.items(), key=lambda item: item[1]))

    rows: list[dict[str, Any]] = []
    for flat_index, value in values.items():
        row: dict[str, Any] = {value_name: value, f"{value_name}_status": statuses.get(flat_index, "")}
        remainder = flat_index
        for dim, size, multiplier, items in zip(ids, sizes, multipliers, dim_items):
            dim_index = remainder // multiplier
            remainder = remainder % multiplier
            if dim_index >= size:
                raise ValueError(f"Invalid JSON-stat index {flat_index} for dimension {dim}")
            row[dim] = items[dim_index][0]
        rows.append(row)
    return pd.DataFrame(rows)


def download_deflators(panel: pd.DataFrame, output_dir: Path) -> pd.DataFrame:
    countries = sorted(panel["country_code"].dropna().astype(str).unique().tolist())
    sectors = sorted(panel["sector_code"].dropna().astype(str).unique().tolist())
    years = sorted(int(y) for y in panel["year"].dropna().unique().tolist())

    frames: list[pd.DataFrame] = []
    for unit, value_name in UNITS.items():
        url = build_url(unit, countries, sectors, years)
        (output_dir / f"eurostat_nama_10_a64_{unit}_url.txt").write_text(url, encoding="utf-8")
        raw = fetch_json(url)
        frame = jsonstat_to_frame(raw, value_name)
        keep_cols = ["geo", "nace_r2", "time", value_name, f"{value_name}_status"]
        frames.append(frame[keep_cols])

    merged = frames[0]
    for frame in frames[1:]:
        merged = merged.merge(frame, on=["geo", "nace_r2", "time"], how="outer")

    merged = merged.rename(columns={"geo": "country_code", "nace_r2": "sector_code", "time": "year"})
    merged["year"] = merged["year"].astype(int)
    merged["na_deflator_cp_over_clv20"] = merged["gva_current_meur_na"] / merged["gva_volume_2020_meur_na"]

    base = merged[merged["year"] == BASE_YEAR][
        ["country_code", "sector_code", "na_deflator_cp_over_clv20"]
    ].rename(columns={"na_deflator_cp_over_clv20": "na_deflator_base"})
    merged = merged.merge(base, on=["country_code", "sector_code"], how="left")
    merged["na_deflator_norm_2021"] = merged["na_deflator_cp_over_clv20"] / merged["na_deflator_base"]
    return merged


def estimate_m3(data: pd.DataFrame, dependent: str, ai_variable: str) -> dict[str, float | int]:
    columns = [dependent, ai_variable, "entity", "country_year"]
    sample = data[columns].dropna().copy()
    exog = pd.DataFrame({"const": 1.0, ai_variable: sample[ai_variable].astype(float)}, index=sample.index)
    absorb = sample[["entity", "country_year"]].astype("category")
    model = AbsorbingLS(sample[dependent].astype(float), exog, absorb=absorb)
    result = model.fit(cov_type="clustered", clusters=sample["entity"], debiased=True)
    beta = float(result.params[ai_variable])
    ci = result.conf_int().loc[ai_variable]
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
    parser.add_argument("--input", type=Path, default=Path("data/processed/panel_analitico.csv"))
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/modelos_panel_v0_3"))
    parser.add_argument("--processed-output", type=Path, default=Path("data/processed/panel_analitico_productividad_real.csv"))
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    args.processed_output.parent.mkdir(parents=True, exist_ok=True)

    panel = pd.read_csv(args.input)
    deflators = download_deflators(panel, args.output_dir)
    deflators.to_csv(args.output_dir / "deflactores_pais_sector_anio.csv", index=False)

    enriched = panel.merge(
        deflators,
        on=["country_code", "sector_code", "year"],
        how="left",
        validate="one_to_one",
    )
    enriched["value_added_real_2021_meur_ge10"] = enriched["value_added_meur_ge10"] / enriched["na_deflator_norm_2021"]
    enriched["labour_productivity_real_2021_keur"] = (
        enriched["labour_productivity_keur"] / enriched["na_deflator_norm_2021"]
    )
    enriched["real_productivity_available"] = np.where(
        enriched["labour_productivity_real_2021_keur"].notna(), "Yes", "No"
    )
    enriched.to_csv(args.processed_output, index=False)

    coverage = pd.DataFrame(
        [
            {
                "rows_panel": len(panel),
                "rows_with_deflator": int(enriched["na_deflator_norm_2021"].notna().sum()),
                "rows_core_complete": int((enriched["core_complete"] == "Yes").sum()),
                "rows_core_with_deflator": int(((enriched["core_complete"] == "Yes") & enriched["na_deflator_norm_2021"].notna()).sum()),
                "rows_balanced_with_deflator": int(((enriched["balanced_entity"] == "Yes") & enriched["na_deflator_norm_2021"].notna()).sum()),
                "entities_balanced_with_deflator": int(
                    enriched[(enriched["balanced_entity"] == "Yes") & enriched["na_deflator_norm_2021"].notna()]
                    .assign(entity=lambda df: df["country_code"].astype(str) + "_" + df["sector_code"].astype(str))["entity"]
                    .nunique()
                ),
            }
        ]
    )
    coverage.to_csv(args.output_dir / "cobertura_deflactores.csv", index=False)

    model_data = enriched[
        (enriched["core_complete"] == "Yes")
        & (enriched["balanced_entity"] == "Yes")
        & (enriched["labour_productivity_keur"] > 0)
        & (enriched["labour_productivity_real_2021_keur"] > 0)
    ].copy()
    model_data["entity"] = model_data["country_code"].astype(str) + "_" + model_data["sector_code"].astype(str)
    model_data["country_year"] = model_data["country_code"].astype(str) + "_" + model_data["year"].astype(str)
    model_data["log_productivity_nominal"] = np.log(model_data["labour_productivity_keur"])
    model_data["log_productivity_real_2021"] = np.log(model_data["labour_productivity_real_2021_keur"])

    rows: list[dict[str, Any]] = []
    for ai_variable, indicator in AI_LABELS.items():
        for dependent, dependent_label in [
            ("log_productivity_nominal", "Nominal, miles EUR corrientes por persona"),
            ("log_productivity_real_2021", "Real aproximada, precios sectoriales 2021"),
        ]:
            estimates = estimate_m3(model_data, dependent, ai_variable)
            rows.append(
                {
                    "specification": "M3_entity_countryyear_FE",
                    "dependent": dependent,
                    "dependent_label": dependent_label,
                    "ai_variable": ai_variable,
                    "indicator": indicator,
                    **estimates,
                }
            )

    results = pd.DataFrame(rows)
    results.to_csv(args.output_dir / "robustez_productividad_real_sectorial.csv", index=False)
    adoption = results[results["ai_variable"] == "ai_any_pct"].copy()
    adoption.to_csv(args.output_dir / "robustez_productividad_real_adopcion_general.csv", index=False)

    print("Sectoral real-productivity robustness OK")
    print(coverage.to_string(index=False))
    print(adoption[["dependent_label", "beta_per_1pp", "clustered_se", "p_value", "effect_10pp_pct", "n", "clusters"]].to_string(index=False))


if __name__ == "__main__":
    main()
