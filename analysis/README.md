# Análisis reproducible v0.1 — IA y productividad sectorial en la UE-27

Este módulo reproduce el primer diagnóstico empírico de la base analítica construida con datos de Eurostat sobre adopción empresarial de inteligencia artificial y Structural Business Statistics (SBS).

## Fuente canónica de reproducción

La entrada reproducible principal es:

```text
data/processed/panel_analitico.csv
```

Los libros Excel versionados en `Facundo_Diaz_Larrarte_TFG/Datos/` conservan una versión cómoda para inspección y auditoría, pero el análisis se reproduce desde el CSV y los scripts de `analysis/`.

## Unidad de análisis

- Combinación país–sector–año.
- UE-27.
- Nueve secciones NACE: C, F, G, H, I, J, L, M y N.
- Años 2021, 2023 y 2024.
- Empresas con 10 o más personas ocupadas.
- Muestra balanceada preliminar: 209 entidades país–sector y 627 observaciones.

## Instalación

Desde la raíz del repositorio, en un entorno virtual:

```bash
python -m venv .venv
.venv/Scripts/python -m pip install --upgrade pip
.venv/Scripts/python -m pip install -r analysis/requirements.txt
```

En Windows PowerShell, la activación equivalente es:

```powershell
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r analysis/requirements.txt
```

## Reproducción completa

Comando canónico:

```bash
python analysis/00_reproducir_todo.py
```

Este comando ejecuta:

```bash
python analysis/01_descriptivo.py \
  --input data/processed/panel_analitico.csv \
  --output-dir outputs/descriptivo_v0_1

python analysis/02_modelos_panel.py \
  --input data/processed/panel_analitico.csv \
  --output-dir outputs/modelos_panel_v0_1

python analysis/03_validacion_linearmodels.py \
  --input data/processed/panel_analitico.csv \
  --output-dir outputs/modelos_panel_v0_1

python analysis/04_robustez_panel.py \
  --input data/processed/panel_analitico.csv \
  --output-dir outputs/modelos_panel_v0_2
```

Al final verifica que existan los productos clave y que los coeficientes de la especificación preferida coincidan entre la implementación manual y `linearmodels.AbsorbingLS`.

## Productos versionables

Se consideran productos reproducibles útiles para el TFG:

```text
outputs/descriptivo_v0_1/tables/*.csv
outputs/descriptivo_v0_1/figures/*.png
outputs/descriptivo_v0_1/resumen.json
outputs/modelos_panel_v0_1/*.csv
outputs/modelos_panel_v0_2/*.csv
```

El archivo `outputs/descriptivo_v0_1/analisis_descriptivo_ia_productividad_ue27_v0_1.xlsx` es un artefacto de consulta. No es la fuente canónica del análisis.

## Primeros resultados

- La adopción general media aumenta de 9,2% en 2021 a 17,2% en 2024.
- La productividad laboral aparente media pasa de 61,8 a 72,8 miles de euros corrientes por persona ocupada.
- La correlación en niveles entre adopción general y log-productividad es 0,564.
- La correlación entre el cambio 2021–2024 en adopción general y el cambio en log-productividad es -0,217.
- En la especificación con efectos fijos país–sector y país–año, ningún indicador de IA presenta una asociación estadísticamente significativa a niveles convencionales.

## Robustez v0.2

El script `analysis/04_robustez_panel.py` genera `outputs/modelos_panel_v0_2/` con:

- comparación de especificaciones M1, M2 y M3 para la muestra balanceada;
- M3 en muestra balanceada;
- M3 en muestra central completa no balanceada;
- M3 ponderado por personas ocupadas;
- M3 excluyendo extremos p1-p99 de productividad en la muestra balanceada.

Estas pruebas evalúan sensibilidad de signo, magnitud y significatividad. No deben usarse para seleccionar la especificación más favorable, sino para documentar la estabilidad de los resultados.

## Interpretación

Los resultados son descriptivos y asociativos. La asociación positiva en niveles puede reflejar diferencias persistentes entre países y sectores. Las correlaciones de cambios y los modelos con efectos fijos pueden estar afectados por inflación, shocks sectoriales, causalidad inversa, inversiones complementarias, horizonte corto y error de medición. No deben interpretarse causalmente.

La validación con `linearmodels` confirma los coeficientes del modelo preferido. Los errores estándar pueden diferir respecto de la implementación manual porque las bibliotecas aplican correcciones de grados de libertad y covarianza no idénticas.
