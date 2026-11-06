# Datos procesados

El archivo reproducible principal del repositorio es:

```text
data/processed/panel_analitico.csv
```

El archivo siguiente se conserva solo como **archivo histórico — NO USAR**:

```text
data/processed/panel_analitico_productividad_real.csv
```

Fue derivado de una proxy retirada por incompatibilidad entre el universo SBS y los deflactores de Cuentas Nacionales. No integra el TFG activo, sus análisis, robusteces ni las instrucciones de reproducción. Se preserva sin modificación ni eliminación exclusivamente para trazabilidad.

## Relación con los Excel

Los libros Excel ubicados en:

```text
Facundo_Diaz_Larrarte_TFG/Datos/
```

conservan una versión cómoda para inspección, auditoría y uso académico. Sin embargo, la reproducción activa se apoya exclusivamente en `panel_analitico.csv` y en los scripts activos documentados en `analysis/README.md`, para evitar depender de operaciones manuales sobre Excel.

## Fuentes

- Eurostat, `isoc_eb_ai`: adopción y uso empresarial de inteligencia artificial.
- Eurostat, `isoc_eb_ain2`: indicadores complementarios sobre usos de inteligencia artificial.
- Eurostat, Structural Business Statistics (SBS): valor agregado y personas ocupadas.
- Archivo histórico — **NO USAR**: Eurostat, `nama_10_a64`, conservado solo como insumo de la proxy retirada; no es una fuente del análisis activo.

## Cobertura

- UE-27.
- Secciones NACE C, F, G, H, I, J, L, M y N.
- Años 2021, 2023 y 2024.
- Empresas con 10 o más personas ocupadas.

## Productividad laboral aparente

La productividad laboral aparente nominal se calcula como:

```text
valor agregado / personas ocupadas
```

En la base, el valor agregado está expresado en millones de euros y se convierte a miles de euros por persona ocupada mediante:

```text
labour_productivity_keur = value_added_meur_ge10 * 1000 / persons_employed_ge10
```

La fórmula siguiente documenta un cálculo histórico archivado, no una variable disponible para uso activo:

```text
deflactor = GVA corriente / GVA volumen encadenado 2020
deflactor normalizado = deflactor / deflactor país-sector en 2021
labour_productivity_real_2021_keur = labour_productivity_keur / deflactor normalizado
```

La proxy se retiró por aplicar deflactores de cuentas nacionales por industria al valor agregado SBS de empresas con 10 o más personas ocupadas. `analysis/05_productividad_real_sectorial.py` rechaza su ejecución para prevenir la regeneración accidental.

## Variables de control de muestra

- `core_complete`: indica observaciones con información central completa.
- `balanced_entity`: indica entidades país–sector observadas en los tres años principales.
- `missing_ai_measures`: cantidad de indicadores de IA faltantes.
- `*_flag`: banderas de calidad o disponibilidad asociadas a indicadores específicos.

El análisis reproducible se ejecuta desde la raíz del repositorio con:

```bash
python analysis/00_reproducir_todo.py
```
