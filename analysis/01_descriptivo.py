#!/usr/bin/env python3
"""Primer análisis descriptivo del panel IA-productividad de Eurostat.

Uso:
    python analysis/01_descriptivo.py --input data/processed/base_analitica_ia_productividad_ue27_v0_1.xlsx
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import pearsonr, spearmanr


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


def weighted_mean(values: pd.Series, weights: pd.Series) -> float:
    valid = values.notna() & weights.notna() & (weights > 0)
    if not valid.any():
        return float("nan")
    return float(np.average(values[valid], weights=weights[valid]))


def correlation_table(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for variable, label in AI_LABELS.items():
        sample = df[[variable, "log_productivity"]].dropna()
        pearson_r, pearson_p = pearsonr(sample[variable], sample["log_productivity"])
        spearman_r, spearman_p = spearmanr(sample[variable], sample["log_productivity"])
        rows.append(
            {
                "variable": variable,
                "indicador": label,
                "n": len(sample),
                "pearson_r": pearson_r,
                "pearson_p": pearson_p,
                "spearman_rho": spearman_r,
                "spearman_p": spearman_p,
            }
        )
    return pd.DataFrame(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/descriptivo_v0_1"))
    args = parser.parse_args()

    tables_dir = args.output_dir / "tables"
    figures_dir = args.output_dir / "figures"
    tables_dir.mkdir(parents=True, exist_ok=True)
    figures_dir.mkdir(parents=True, exist_ok=True)

    panel = pd.read_excel(args.input, sheet_name="Panel")
    balanced = pd.read_excel(args.input, sheet_name="Muestra_balanceada")
    balanced["log_productivity"] = np.log(balanced["labour_productivity_keur"])

    analysis_vars = ["labour_productivity_keur", "log_productivity", *AI_LABELS.keys()]
    descriptive = (
        balanced[analysis_vars]
        .describe(percentiles=[0.25, 0.5, 0.75])
        .T.reset_index(names="variable")
        .rename(columns={"25%": "p25", "50%": "median", "75%": "p75"})
    )

    year_rows = []
    for year, group in balanced.groupby("year", sort=True):
        row = {
            "year": int(year),
            "n": len(group),
            "entities": group[["country_code", "sector_code"]].drop_duplicates().shape[0],
            "productivity_mean_keur": group["labour_productivity_keur"].mean(),
            "productivity_median_keur": group["labour_productivity_keur"].median(),
            "productivity_employment_weighted_keur": weighted_mean(
                group["labour_productivity_keur"], group["persons_employed_ge10"]
            ),
        }
        for variable in AI_LABELS:
            row[f"{variable}_mean"] = group[variable].mean()
        year_rows.append(row)
    by_year = pd.DataFrame(year_rows)

    by_sector = (
        balanced.groupby(["sector_code", "sector_name"], as_index=False)
        .agg(
            n=("year", "size"),
            countries=("country_code", "nunique"),
            productivity_mean_keur=("labour_productivity_keur", "mean"),
            productivity_median_keur=("labour_productivity_keur", "median"),
            ai_any_mean_pct=("ai_any_pct", "mean"),
            ai_workflow_mean_pct=("ai_workflow_pct", "mean"),
            ai_production_mean_pct=("ai_production_pct", "mean"),
            ai_logistics_mean_pct=("ai_logistics_pct", "mean"),
            ai_marketing_mean_pct=("ai_marketing_pct", "mean"),
            ai_security_mean_pct=("ai_security_pct", "mean"),
        )
        .sort_values("ai_any_mean_pct", ascending=False)
    )

    corr = correlation_table(balanced)
    corr_matrix = balanced[["log_productivity", *AI_LABELS.keys()]].corr(method="pearson")
    corr_by_year_rows = []
    for year, group in balanced.groupby("year", sort=True):
        for variable, label in AI_LABELS.items():
            sample = group[[variable, "log_productivity"]].dropna()
            r, p = pearsonr(sample[variable], sample["log_productivity"])
            corr_by_year_rows.append(
                {"year": int(year), "variable": variable, "indicador": label, "n": len(sample), "pearson_r": r, "p_value": p}
            )
    corr_by_year = pd.DataFrame(corr_by_year_rows)

    wide = balanced.pivot(index=["country_code", "sector_code"], columns="year")
    changes = pd.DataFrame(index=wide.index).reset_index()
    for variable in ["labour_productivity_keur", *AI_LABELS.keys()]:
        changes[f"delta_{variable}_2021_2024"] = wide[(variable, 2024)].values - wide[(variable, 2021)].values
    changes["delta_log_productivity_2021_2024"] = (
        np.log(wide[("labour_productivity_keur", 2024)].values)
        - np.log(wide[("labour_productivity_keur", 2021)].values)
    )

    change_rows = []
    for variable, label in AI_LABELS.items():
        x_col = f"delta_{variable}_2021_2024"
        sample = changes[[x_col, "delta_log_productivity_2021_2024"]].dropna()
        r, p = pearsonr(sample[x_col], sample["delta_log_productivity_2021_2024"])
        change_rows.append({"variable": variable, "indicador": label, "n": len(sample), "pearson_r": r, "p_value": p})
    change_corr = pd.DataFrame(change_rows)

    missing = pd.DataFrame(
        {
            "variable": ["labour_productivity_keur", *AI_LABELS.keys()],
            "missing_panel": [panel[v].isna().sum() for v in ["labour_productivity_keur", *AI_LABELS.keys()]],
            "missing_balanced": [balanced[v].isna().sum() for v in ["labour_productivity_keur", *AI_LABELS.keys()]],
        }
    )
    missing["coverage_panel_pct"] = 100 * (len(panel) - missing["missing_panel"]) / len(panel)
    missing["coverage_balanced_pct"] = 100 * (len(balanced) - missing["missing_balanced"]) / len(balanced)

    descriptive.to_csv(tables_dir / "estadisticas_descriptivas.csv", index=False)
    by_year.to_csv(tables_dir / "promedios_por_anio.csv", index=False)
    by_sector.to_csv(tables_dir / "promedios_por_sector.csv", index=False)
    corr.to_csv(tables_dir / "correlaciones_niveles.csv", index=False)
    corr_by_year.to_csv(tables_dir / "correlaciones_por_anio.csv", index=False)
    corr_matrix.to_csv(tables_dir / "matriz_correlaciones.csv")
    changes.to_csv(tables_dir / "cambios_2021_2024.csv", index=False)
    change_corr.to_csv(tables_dir / "correlaciones_cambios.csv", index=False)
    missing.to_csv(tables_dir / "cobertura.csv", index=False)

    sns.set_theme(style="whitegrid", context="notebook")
    palette = sns.color_palette("Blues", n_colors=len(AI_LABELS) + 2)[2:]

    fig, ax = plt.subplots(figsize=(10, 6))
    for color, (variable, label) in zip(palette, AI_LABELS.items()):
        ax.plot(by_year["year"], by_year[f"{variable}_mean"], marker="o", label=label, color=color)
    ax.set(title="Adopción y usos de IA en la muestra balanceada", xlabel="Año", ylabel="Empresas (%)")
    ax.set_xticks(by_year["year"])
    ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1), frameon=False)
    fig.tight_layout()
    fig.savefig(figures_dir / "adopcion_ia_por_anio.png", dpi=220, bbox_inches="tight")
    plt.close(fig)

    sector_plot = by_sector.sort_values("ai_any_mean_pct")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(sector_plot["sector_code"], sector_plot["ai_any_mean_pct"], color="#4472C4")
    ax.set(title="Adopción general de IA por sector, promedio 2021–2024", xlabel="Empresas que utilizan IA (%)", ylabel="Sector NACE")
    fig.tight_layout()
    fig.savefig(figures_dir / "adopcion_ia_por_sector.png", dpi=220, bbox_inches="tight")
    plt.close(fig)

    plot_2024 = balanced[balanced["year"] == 2024]
    fig, ax = plt.subplots(figsize=(9, 6))
    sns.scatterplot(
        data=plot_2024,
        x="ai_any_pct",
        y="labour_productivity_keur",
        hue="sector_code",
        size="persons_employed_ge10",
        sizes=(20, 240),
        alpha=0.72,
        ax=ax,
    )
    ax.set(title="IA y productividad laboral aparente, 2024", xlabel="Empresas que utilizan IA (%)", ylabel="Miles de euros por persona empleada")
    ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1), frameon=False, title="Sector / empleo")
    fig.tight_layout()
    fig.savefig(figures_dir / "ia_productividad_2024.png", dpi=220, bbox_inches="tight")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, cmap="RdBu_r", center=0, vmin=-1, vmax=1, annot=True, fmt=".2f", ax=ax)
    ax.set_title("Correlaciones: productividad e indicadores de IA")
    ax.set_xticklabels(["Log productividad", *AI_LABELS.values()], rotation=45, ha="right")
    ax.set_yticklabels(["Log productividad", *AI_LABELS.values()], rotation=0)
    fig.tight_layout()
    fig.savefig(figures_dir / "matriz_correlaciones.png", dpi=220, bbox_inches="tight")
    plt.close(fig)

    summary = {
        "panel_rows": int(len(panel)),
        "balanced_rows": int(len(balanced)),
        "balanced_entities": int(balanced[["country_code", "sector_code"]].drop_duplicates().shape[0]),
        "years": sorted(int(x) for x in balanced["year"].unique()),
        "countries": int(balanced["country_code"].nunique()),
        "sectors": int(balanced["sector_code"].nunique()),
        "strongest_level_correlation": corr.loc[corr["pearson_r"].abs().idxmax()].to_dict(),
        "strongest_change_correlation": change_corr.loc[change_corr["pearson_r"].abs().idxmax()].to_dict(),
    }
    (args.output_dir / "resumen.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    workbook_payload = {
        "summary": summary,
        "descriptive": descriptive.replace({np.nan: None}).to_dict(orient="records"),
        "by_year": by_year.replace({np.nan: None}).to_dict(orient="records"),
        "by_sector": by_sector.replace({np.nan: None}).to_dict(orient="records"),
        "correlations": corr.replace({np.nan: None}).to_dict(orient="records"),
        "correlations_by_year": corr_by_year.replace({np.nan: None}).to_dict(orient="records"),
        "change_correlations": change_corr.replace({np.nan: None}).to_dict(orient="records"),
        "coverage": missing.replace({np.nan: None}).to_dict(orient="records"),
    }
    (args.output_dir / "workbook_payload.json").write_text(
        json.dumps(workbook_payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
