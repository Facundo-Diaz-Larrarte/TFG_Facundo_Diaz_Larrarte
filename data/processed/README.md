# Datos procesados

El archivo reproducible principal del repositorio es `panel_analitico.csv`. Contiene la grilla completa de 729 observaciones y las variables `core_complete` y `balanced_entity`, que permiten reconstruir la muestra balanceada de 627 filas.

El libro completo `base_analitica_ia_productividad_ue27_v0_1.xlsx` conserva además las observaciones fuente filtradas, el diccionario y la auditoría, y se distribuye como artefacto versionado fuera del historial Git.

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

El análisis reproducible se encuentra en `analysis/01_descriptivo.py` y `analysis/02_modelos_panel.py`.
