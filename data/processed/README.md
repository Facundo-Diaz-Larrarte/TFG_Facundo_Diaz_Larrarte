# Datos procesados

El archivo reproducible principal del repositorio es:

```text
data/processed/panel_analitico.csv
```

Contiene la grilla completa de 729 observaciones país–sector–año y las variables `core_complete` y `balanced_entity`, que permiten reconstruir la muestra central completa y la muestra balanceada de 627 filas.

## Relación con los Excel

Los libros Excel ubicados en:

```text
Facundo_Diaz_Larrarte_TFG/Datos/
```

conservan una versión cómoda para inspección, auditoría y uso académico. Sin embargo, la reproducción del análisis se apoya en `panel_analitico.csv` y en los scripts de `analysis/`, para evitar depender de operaciones manuales sobre Excel.

## Fuentes

- Eurostat, `isoc_eb_ai`: adopción y uso empresarial de inteligencia artificial.
- Eurostat, `isoc_eb_ain2`: indicadores complementarios sobre usos de inteligencia artificial.
- Eurostat, Structural Business Statistics (SBS): valor agregado y personas ocupadas.

## Cobertura

- UE-27.
- Secciones NACE C, F, G, H, I, J, L, M y N.
- Años 2021, 2023 y 2024.
- Empresas con 10 o más personas ocupadas.

## Productividad laboral aparente

La productividad laboral aparente se calcula como:

```text
valor agregado / personas ocupadas
```

En la base, el valor agregado está expresado en millones de euros y se convierte a miles de euros por persona ocupada mediante:

```text
labour_productivity_keur = value_added_meur_ge10 * 1000 / persons_employed_ge10
```

## Variables de control de muestra

- `core_complete`: indica observaciones con información central completa.
- `balanced_entity`: indica entidades país–sector observadas en los tres años principales.
- `missing_ai_measures`: cantidad de indicadores de IA faltantes.
- `*_flag`: banderas de calidad o disponibilidad asociadas a indicadores específicos.

El análisis reproducible se ejecuta desde la raíz del repositorio con:

```bash
python analysis/00_reproducir_todo.py
```
