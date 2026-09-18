#!/usr/bin/env python3
"""Ejecuta la reproducción completa del análisis IA-productividad.

Desde la raíz del repositorio:

    python analysis/00_reproducir_todo.py

El script usa el mismo intérprete de Python que lo ejecuta, corre el análisis
descriptivo, los modelos preliminares y la validación con linearmodels. Al final
verifica la existencia de los productos clave y que los coeficientes del modelo
preferido coincidan entre la implementación manual y linearmodels.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "processed" / "panel_analitico.csv"
DESCRIPTIVE_OUTPUT = ROOT / "outputs" / "descriptivo_v0_1"
MODELS_OUTPUT = ROOT / "outputs" / "modelos_panel_v0_1"
ROBUSTNESS_OUTPUT = ROOT / "outputs" / "modelos_panel_v0_2"

EXPECTED_FILES = [
    DESCRIPTIVE_OUTPUT / "tables" / "promedios_por_anio.csv",
    DESCRIPTIVE_OUTPUT / "tables" / "promedios_por_sector.csv",
    DESCRIPTIVE_OUTPUT / "tables" / "correlaciones_niveles.csv",
    DESCRIPTIVE_OUTPUT / "tables" / "correlaciones_cambios.csv",
    DESCRIPTIVE_OUTPUT / "figures" / "adopcion_ia_por_anio.png",
    DESCRIPTIVE_OUTPUT / "figures" / "adopcion_ia_por_sector.png",
    DESCRIPTIVE_OUTPUT / "figures" / "matriz_correlaciones.png",
    MODELS_OUTPUT / "modelo_preferido.csv",
    MODELS_OUTPUT / "modelo_preferido_linearmodels.csv",
    MODELS_OUTPUT / "comparacion_modelo_preferido_linearmodels.csv",
    ROBUSTNESS_OUTPUT / "robustez_m3.csv",
    ROBUSTNESS_OUTPUT / "robustez_adopcion_general.csv",
    ROBUSTNESS_OUTPUT / "comparacion_especificaciones_balanceada.csv",
    ROBUSTNESS_OUTPUT / "resumen_robustez_m3.csv",
]


def run(script: str, *args: str) -> None:
    command = [sys.executable, str(ROOT / "analysis" / script), *args]
    print("$", " ".join(command))
    subprocess.run(command, cwd=ROOT, check=True)


def verify_outputs() -> None:
    missing = [path for path in EXPECTED_FILES if not path.exists()]
    if missing:
        missing_list = "\n".join(str(path.relative_to(ROOT)) for path in missing)
        raise SystemExit(f"Missing expected reproducibility outputs:\n{missing_list}")

    comparison = pd.read_csv(MODELS_OUTPUT / "comparacion_modelo_preferido_linearmodels.csv")
    if not comparison["same_beta_1e_10"].all():
        failed = comparison.loc[~comparison["same_beta_1e_10"], ["ai_variable", "beta_abs_diff"]]
        raise SystemExit(f"Manual and linearmodels coefficients differ:\n{failed.to_string(index=False)}")

    print("Reproducibility check OK: expected outputs exist and M3 coefficients match linearmodels.")


def main() -> None:
    if not INPUT.exists():
        raise SystemExit(f"Input file not found: {INPUT.relative_to(ROOT)}")

    run(
        "01_descriptivo.py",
        "--input",
        str(INPUT.relative_to(ROOT)),
        "--output-dir",
        str(DESCRIPTIVE_OUTPUT.relative_to(ROOT)),
    )
    run(
        "02_modelos_panel.py",
        "--input",
        str(INPUT.relative_to(ROOT)),
        "--output-dir",
        str(MODELS_OUTPUT.relative_to(ROOT)),
    )
    run(
        "03_validacion_linearmodels.py",
        "--input",
        str(INPUT.relative_to(ROOT)),
        "--output-dir",
        str(MODELS_OUTPUT.relative_to(ROOT)),
    )
    run(
        "04_robustez_panel.py",
        "--input",
        str(INPUT.relative_to(ROOT)),
        "--output-dir",
        str(ROBUSTNESS_OUTPUT.relative_to(ROOT)),
    )
    verify_outputs()


if __name__ == "__main__":
    main()
