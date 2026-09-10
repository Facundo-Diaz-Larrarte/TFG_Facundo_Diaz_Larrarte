# Datos procesados

La base de trabajo es `base_analitica_ia_productividad_ue27_v0_1.xlsx`.

## Fuentes

- Eurostat, `isoc_eb_ain2`: adopción y usos de inteligencia artificial por actividad económica.
- Eurostat, `sbs_sc_ovw`: valor agregado y personas empleadas de Structural Business Statistics.

## Cobertura

- UE-27.
- Secciones NACE C, F, G, H, I, J, L, M y N.
- Años 2021, 2023 y 2024.
- Empresas con 10 o más personas empleadas.

La productividad laboral aparente se calcula como valor agregado, expresado en millones de euros, multiplicado por 1.000 y dividido por personas empleadas. El resultado se expresa en miles de euros corrientes por persona.

La hoja `Panel` conserva la grilla teórica completa y sus faltantes. La hoja `Muestra_balanceada` contiene 209 entidades país–sector observadas durante los tres años.

El libro también conserva las observaciones fuente filtradas, el diccionario de variables y las reglas de auditoría. Debido a que es un archivo binario derivado, debe versionarse con un número de versión y no editarse manualmente. El análisis reproducible se encuentra en `analysis/01_descriptivo.py`.
