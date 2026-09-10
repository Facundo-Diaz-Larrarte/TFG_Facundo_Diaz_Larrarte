# Análisis descriptivo v0.1 — IA y productividad sectorial en la UE-27

Este módulo reproduce el primer diagnóstico de la base analítica construida con datos de Eurostat sobre adopción de inteligencia artificial y Structural Business Statistics (SBS).

## Unidad de análisis

- Combinación país–sector–año.
- UE-27, nueve secciones NACE.
- Años 2021, 2023 y 2024.
- Empresas con 10 o más personas empleadas.
- Muestra balanceada: 209 entidades país–sector y 627 observaciones.

## Ejecución

Desde la raíz del repositorio:

```bash
python analysis/01_descriptivo.py \
  --input data/processed/base_analitica_ia_productividad_ue27_v0_1.xlsx \
  --output-dir outputs/descriptivo_v0_1
```

Dependencias: `pandas`, `numpy`, `scipy`, `matplotlib`, `seaborn` y `openpyxl`.

## Productos

El script genera tablas CSV de cobertura, estadísticos, promedios por año y sector, correlaciones en niveles y correlaciones de cambios 2021–2024. También crea cuatro figuras PNG.

## Primeros resultados

- La adopción general media aumenta de 9,2% en 2021 a 17,2% en 2024.
- La productividad laboral aparente media pasa de 61,8 a 72,8 miles de euros corrientes por persona.
- La correlación en niveles entre adopción general y log-productividad es 0,564.
- La correlación entre el cambio 2021–2024 en adopción general y el cambio en log-productividad es -0,217.
- Entre los usos específicos, procesos y toma de decisiones presenta la correlación en niveles más elevada con log-productividad: 0,533.

## Interpretación

Los resultados son descriptivos y agregados. La asociación positiva en niveles puede reflejar diferencias persistentes entre países y sectores, mientras que las correlaciones de cambios pueden estar afectadas por inflación, shocks sectoriales, causalidad inversa y error de medición. No deben interpretarse causalmente.

El siguiente paso es estimar modelos de panel con efectos fijos país–sector, efectos temporales y controles país–año. Los usos de IA deben evaluarse inicialmente en especificaciones separadas porque se superponen y presentan alta correlación entre sí.

