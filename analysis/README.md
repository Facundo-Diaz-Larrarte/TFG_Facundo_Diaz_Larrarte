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

- Grilla teórica: 729 celdas país–sector–año.
- Muestra principal *core* no balanceada: 667 observaciones de productividad nominal y adopción general, correspondientes a 233 entidades país–sector.
- Los indicadores secundarios de IA usan casos completos por indicador: 626–662 observaciones no balanceadas. Por tanto, 667 no implica completitud en todos los indicadores secundarios.
- Sensibilidad balanceada: *core* de 209 entidades y 627 observaciones; indicadores secundarios de 590–625 observaciones, según indicador.

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



## Reproducción del análisis base (scripts 01–04)



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



Al final verifica que existan los productos clave, que los coeficientes de la especificación preferida coincidan entre la implementación canónica y `linearmodels.AbsorbingLS`, y que los contrastes y robusteces de panel se hayan generado correctamente. La coincidencia de coeficientes no implica identidad de errores estándar ni valores p, porque las convenciones de covarianza son distintas.



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



- La adopción general media aumenta de 9,2% en 2021 a 17,0% en 2024.

- La productividad laboral aparente media pasa de 62,0 a 72,1 miles de euros corrientes por persona ocupada.

- La correlación en niveles entre adopción general y log-productividad es 0,558.

- La correlación entre el cambio 2021–2024 en adopción general y el cambio en log-productividad es -0,229.

- En la especificación con efectos fijos país–sector y país–año, ningún indicador de IA presenta una asociación estadísticamente significativa a niveles convencionales.



## Robustez v0.2



El script `analysis/04_robustez_panel.py` genera `outputs/modelos_panel_v0_2/` con:



- comparación de M1, M2 y M3 sobre la muestra *core* no balanceada, en `comparacion_especificaciones_principal.csv`;
- M3 para cada indicador en los escenarios *core* no balanceado, *core* ponderado por empleo, *core* sin extremos p1-p99 y *core* balanceado;
- en el escenario no balanceado, la adopción general usa 667 observaciones y los indicadores secundarios, 626–662;
- en el escenario balanceado, la adopción general usa 627 observaciones y los indicadores secundarios, 590–625;
- las muestras se definen por casos completos de cada indicador.

Para un indicador dado, M1, M2 y M3 usan la misma muestra de casos completos; el tamaño muestral no cambia por la especificación de efectos fijos. El archivo `comparacion_especificaciones_balanceada.csv` se conserva sólo por compatibilidad de nombre y duplica la comparación *core* no balanceada; su nombre no prueba estimaciones balanceadas.

Estas pruebas evalúan sensibilidad de signo, magnitud y significatividad. No deben usarse para seleccionar la especificación más favorable, sino para documentar la estabilidad de los resultados.



## Cobertura y sensibilidad de flags SBS

El siguiente comando lee `Fuente_SBS` del libro versionado, agrega los status `b` por país--sector--año a través de las cuatro clases de tamaño y estima M3 con la misma rutina `AbsorbingLS` de robustez:

```bash
.venv/Scripts/python.exe analysis/06_auditar_flags_sbs.py \
  --source-workbook Facundo_Diaz_Larrarte_TFG/Datos/base_analitica_ia_productividad_ue27_v0_1.xlsx \
  --panel data/processed/panel_analitico.csv \
  --output-dir outputs/modelos_panel_v0_2
```

Genera `cobertura_flags_sbs.csv` y `sensibilidad_flags_sbs.csv`. El primero informa la cobertura fuente/panel y el segundo compara M3 completo con dos exclusiones de sensibilidad: filas core marcadas y entidades con alguna fila core marcada. La muestra principal conserva todas las filas core; el script no modifica el panel y rechaza sobrescribir cualquiera de esos dos archivos.

## Tratamiento de precios y delimitación nominal



Siguiendo a Berndt (1991), la productividad laboral aparente se analiza en términos nominales estandarizados de Eurostat SBS. No se aplican deflactores macroeconómicos agregados de Cuentas Nacionales (`nama_10_a64`) por el descalce entre el universo empresarial de SBS (empresas formales de 10 o más ocupados) y el universo macroeconómico global. En M3, los efectos fijos país--año ($\gamma_{ct}$) absorben componentes de inflación agregada y shocks macroeconómicos comunes a todos los sectores de un país--año; no identifican precios relativos ni shocks específicos de sector.



## Archivo histórico retirado: proxy de productividad real

**NO USAR EN EL TFG ACTIVO NI EN SU REPRODUCCIÓN.** Los artefactos v0.3 —`analysis/05_productividad_real_sectorial.py`, `data/processed/panel_analitico_productividad_real.csv` y `outputs/modelos_panel_v0_3/`— permanecen archivados únicamente para trazabilidad histórica. La decisión del autor retira por completo esta proxy de todos los resultados, análisis, robusteces, conclusiones e instrucciones activas: combina universos incompatibles de SBS y Cuentas Nacionales. El script 05 se niega deliberadamente a ejecutarse y no debe reactivarse sin una decisión metodológica nueva y explícita.

## Interacciones sectoriales nominales (T19)

La reconstrucción sectorial nominal se ejecuta desde el panel canónico y escribe una única salida versionada:

```bash
.venv/Scripts/python.exe analysis/07_heterogeneidad_sectorial.py
```

Genera `outputs/modelos_panel_sectorial_v0_1/heterogeneidad_sectorial.csv` con pendientes de `ai_any_pct` por sector, efectos fijos país--sector y país--año, y covarianza agrupada y debiased por entidad país--sector. El script se niega a sobrescribir la salida existente. Es una reconstrucción asociativa no causal de la especificación documentada, no una recuperación de código original. Los nueve contrastes sectoriales usan Wald asintótico χ²(1): deben presentarse como una única familia exploratoria, con $p$ crudos y Holm. Tras Holm, C=0.00110, G=0.00000000151 y M=0.04838 permanecen bajo 0.05; I pasa de $p$ crudo 0.013261 a 0.07957 y no alcanza 5%. Este análisis usa exclusivamente productividad nominal.

## Sensibilidad de covarianza M3 (T21)

El comando siguiente genera una comparación acotada de la inferencia de M3 para `ai_any_pct`, sin ejecutar el pipeline completo ni modificar las salidas existentes del modelo:

```bash
.venv/Scripts/python.exe analysis/08_sensibilidad_cluster_m3.py
```

Es una sensibilidad de la matriz de covarianza de `AbsorbingLS`: conserva muestra *core*, productividad nominal positiva en logaritmos, regresor, ausencia de ponderaciones y efectos fijos país--sector y país--año de M3. Compara la agrupación unidimensional por entidad con la bidimensional entidad--país--año, que permite dependencia residual compartida entre sectores de un mismo país--año. No sustituye la inferencia canónica T60: ésta usa CR1 de rango efectivo $\frac{G}{G-1}\frac{N-1}{N-\operatorname{rank}(X)}$ para clusters de entidad y referencia $t_{G-1}$. El CSV informa los grupos realizados después del filtrado exacto; la inferencia sigue limitada por 27 países y T=3.

Para M3 general, la inferencia canónica T60 usa $n=667$, $G=233$, $\operatorname{rank}(X)=288$, $\beta=-0.001263116$, $EE=0.001171453$, $p=0.282043$ e IC95% $[-0.00357116,\ 0.00104493]$. La sensibilidad `AbsorbingLS` conserva el coeficiente: con su propia convención de covarianza, una vía produce $EE=0.000884369$, $p=0.15410$ y dos vías $EE=0.000939258$, $p=0.17955$. Esos números no describen un aumento directo desde el EE canónico; son convenciones separadas.

## Interpretación



Los resultados son descriptivos y asociativos. La asociación positiva en niveles puede reflejar diferencias persistentes entre países y sectores. Las correlaciones de cambios y los modelos con efectos fijos pueden estar afectados por inflación, shocks sectoriales, causalidad inversa, inversiones complementarias, horizonte corto y error de medición. No deben interpretarse causalmente.



`linearmodels.AbsorbingLS` valida los coeficientes del modelo preferido. Sus errores estándar y valores p siguen una convención de covarianza distinta de la inferencia canónica T60 y no deben sustituirla.