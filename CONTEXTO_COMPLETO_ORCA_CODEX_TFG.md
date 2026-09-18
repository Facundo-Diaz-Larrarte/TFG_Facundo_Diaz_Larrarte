# Contexto completo para continuar el TFG con Orca/Codex

**Responsable:** Facundo Díaz Larrarte

**Carrera:** Licenciatura en Economía, Facultad de Ciencias Económicas, Universidad Nacional de Río Cuarto

**Estado del documento:** handoff operativo y académico

**Última actualización:** 18 de septiembre de 2026

**Repositorio:** <https://github.com/Facundo-Diaz-Larrarte/TFG_Facundo_Diaz_Larrarte>

> **Instrucción para cualquier agente nuevo:** leer este archivo completo antes de proponer cambios. No cambiar el tema, la pregunta, el alcance, las hipótesis ni la estrategia econométrica sin autorización expresa de Facundo. Antes de editar, comprobar la rama, el estado de Git y los PR abiertos.

---

## 1. Resumen ejecutivo

Este proyecto es una **tesina o Trabajo Final de Grado de Licenciatura en Economía**, no una tesis doctoral ni un artículo que deba resolver identificación causal completa. El profesor ya dio conformidad general para trabajar sobre el tema. El proyecto es viable y debe continuar, con un alcance compatible con aproximadamente dos o tres meses de trabajo, datos públicos secundarios y sin encuestas propias.

El objeto es estudiar cómo varían la **adopción y los usos empresariales de inteligencia artificial entre sectores de la Unión Europea** y en qué medida esas diferencias se asocian con niveles y variaciones de **productividad laboral aparente**.

La intuición sustantiva de Facundo no es simplemente demostrar que “más IA equivale a más productividad”. Le interesa entender que:

- la utilidad económica de la IA puede depender del sector, la tarea y la forma de integración;
- adoptar IA no garantiza obtener resultados productivos;
- algunas tareas pueden resolverse mejor mediante automatización determinística convencional;
- la reorganización de procesos, las capacidades del personal y otros activos complementarios pueden condicionar el resultado;
- una elevada adopción sin una mejora equivalente de productividad puede sugerir una **brecha de realización productiva**, aunque los datos agregados no permitan diagnosticar por qué ocurre.

El enfoque académico acordado es, por lo tanto, una **replicación y extensión** de antecedentes existentes: reconstrucción transparente de datos oficiales, distinción entre adopción general y usos funcionales, comparación entre correlaciones en niveles y variaciones dentro de cada unidad país–sector, y análisis de heterogeneidad sectorial.

La base ya existe. También existe un primer análisis descriptivo y una estimación preliminar de panel, pero el código y sus productos siguen en un PR abierto y todavía deben validarse con una biblioteca econométrica estándar, ampliar la heterogeneidad sectorial y ejecutar las pruebas de robustez.

---

## 2. Restricciones y decisiones que no deben olvidarse

1. **Es una tesina de grado.** Debe ser rigurosa, económica y reproducible, pero acotada.
2. **No prometer causalidad.** El diseño actual identifica asociaciones, no el efecto causal de la IA.
3. **No inferir comportamientos de empresas individuales.** La unidad es país–sector–año.
4. **No afirmar que una empresa “usa mal la IA”, que pagó demasiado, que necesitaba automatización tradicional o que obtuvo un ROI negativo.** Los datos no miden eso.
5. **No afirmar que la falta de significatividad demuestra que la IA no sirve.** Puede reflejar horizonte corto, medición agregada, inversiones complementarias, causalidad inversa, shocks o poca variación temporal.
6. **No convertir indicadores distintos en un índice sofisticado inventado.** La adopción y cada uso se analizan por separado, salvo que exista una justificación teórica y estadística previa.
7. **No mezclar definiciones que cambiaron entre olas.** Deben documentarse rupturas y comparabilidad.
8. **La IA es el núcleo.** Capacidades complementarias pueden incorporarse como marco teórico, controles o extensiones si la información lo permite, pero no deben diluir el tema.
9. **No mencionar en la tesina, el plan, los resultados, el repositorio público ni las presentaciones el proyecto empresarial privado que motivó parte del interés personal.** Tampoco utilizar su nombre. Este límite es estricto.
10. **STORM está descartado**, porque requiere API y Facundo necesita herramientas que funcionen con ChatGPT/Codex/Orca o sin contratar una API adicional.
11. **Overleaf es la fuente de verdad del manuscrito LaTeX.** El repositorio debe conservar versiones reproducibles, pero antes de modificar texto académico hay que comprobar si Overleaf contiene cambios más recientes.
12. **GitHub es la fuente de verdad del código, datos versionados, resultados y revisiones.** Trabajar mediante ramas y PR; no fusionar automáticamente sin pedido de Facundo.
13. **No inventar referencias.** Verificar autor, título, año, DOI/URL y correspondencia entre la cita y lo que realmente sostiene el trabajo.

---

## 3. Título, pregunta, objetivos e hipótesis vigentes

### 3.1 Título de trabajo

**Usos empresariales de inteligencia artificial y productividad laboral: evidencia país–sector para la Unión Europea**

### 3.2 Pregunta principal

> ¿Cómo varían la adopción y los usos empresariales de inteligencia artificial entre los sectores económicos de la Unión Europea, y en qué medida esas diferencias se asocian con distintos niveles y variaciones de productividad laboral?

### 3.3 Objetivo general

Analizar cómo varían la adopción y los usos empresariales de inteligencia artificial entre sectores de la Unión Europea y estimar su asociación con la productividad laboral aparente, utilizando la adopción general como referencia y considerando la heterogeneidad productiva sectorial.

### 3.4 Objetivos específicos vigentes

- Integrar en una base país–sector–año indicadores de IA, valor agregado y personas ocupadas de Eurostat.
- Describir la evolución y heterogeneidad por país, sector y año.
- Calcular y comparar productividad laboral aparente.
- Estimar una asociación de referencia entre adopción general y productividad mediante panel.
- Comparar adopción general con usos en procesos/decisiones, producción, logística, marketing/ventas y seguridad informática.
- Examinar heterogeneidad sectorial.
- Evaluar robustez frente a muestras, ponderaciones, valores extremos, precios y efectos fijos alternativos.
- Explicitar limitaciones de medición e interpretación.

### 3.5 Hipótesis

**Hipótesis de referencia:** una mayor adopción empresarial de IA se asocia con una mayor productividad laboral aparente.

**Primera hipótesis central:** la relación no es uniforme entre funciones. Los usos vinculados con procesos internos, decisiones, producción y logística podrían relacionarse más estrechamente con productividad que la adopción general o usos de apoyo/comercialización.

**Segunda hipótesis central:** la asociación entre IA y productividad es heterogénea entre sectores debido a diferencias en tareas, tecnologías productivas y capacidades complementarias.

Las hipótesis son asociativas y, para varios usos, exploratorias. No deben redactarse como resultados ya asegurados.

---

## 4. Encuadre económico

La incorporación de IA se interpreta como una decisión empresarial de adopción e integración tecnológica. Una tecnología puede alterar costos, calidad, tiempos, decisiones, escala o variedad, pero el resultado depende de:

- las tareas concretas sobre las que actúa;
- la exposición y posibilidad técnica de automatización o asistencia;
- rediseño organizacional y de procesos;
- capital humano y aprendizaje;
- datos, software, infraestructura y calidad de gestión;
- costos de implementación, coordinación y mantenimiento;
- horizonte temporal necesario para obtener resultados.

La literatura sobre tecnologías de propósito general y la **curva J de productividad** permite explicar que las inversiones complementarias pueden generar costos iniciales y beneficios demorados. Este marco es importante para interpretar por qué una correlación positiva entre unidades puede desaparecer al controlar diferencias estructurales o por qué la adopción reciente todavía no aparece asociada con crecimiento contemporáneo.

El aporte desde Economía debe concentrarse en incentivos, complementariedades, productividad, heterogeneidad y medición; no convertirse en una descripción puramente técnica de herramientas de IA.

---

## 5. Diseño empírico actual

### 5.1 Unidad de observación

Combinación **país–sector–año**.

### 5.2 Cobertura

- **Países:** UE-27.
- **Años:** 2021, 2023 y 2024.
- **Empresas:** 10 o más personas ocupadas, para mantener compatibilidad con los indicadores de IA.
- **Sectores NACE Rev. 2:** nueve secciones.

| Código | Sector |
|---|---|
| C | Industria manufacturera |
| F | Construcción |
| G | Comercio mayorista y minorista |
| H | Transporte y almacenamiento |
| I | Alojamiento y servicios de comida |
| J | Información y comunicación |
| L | Actividades inmobiliarias |
| M | Actividades profesionales, científicas y técnicas |
| N | Actividades administrativas y servicios auxiliares |

No incorporar 2025 al panel principal hasta disponer de SBS plenamente compatible. Si se usa, debe quedar como extensión descriptiva separada.

### 5.3 Tamaño de la base

- Universo teórico: 27 países × 9 sectores × 3 años = **729 filas**.
- Filas con información central completa: **667**.
- Panel balanceado: **209 entidades país–sector**, observadas tres veces.
- Observaciones del panel balanceado: **627**.

Estas cifras son las preliminares verificadas. Pueden cambiar tras la auditoría definitiva o para indicadores con menor cobertura.

### 5.4 Variable dependiente

Productividad laboral aparente:

\[
Productividad_{cst}=\frac{Valor\ agregado_{cst}}{Personas\ ocupadas_{cst}}
\]

- Valor agregado: Eurostat Structural Business Statistics (SBS).
- Personas ocupadas: Eurostat SBS.
- Unidad guardada: miles de euros corrientes por persona (`labour_productivity_keur`).
- Regresiones: logaritmo de productividad.

No es productividad total de factores. El uso de euros corrientes obliga a discutir inflación y comparabilidad de precios. Los efectos país–año de la especificación preferida absorben shocks nominales comunes a los sectores de cada país/año, pero no resuelven toda diferencia de precios relativos entre sectores. Debe ejecutarse una robustez con deflactores, volumen o PPS/PPP si la disponibilidad lo permite.

### 5.5 Variables explicativas de IA

Todas son porcentajes de empresas (`PC_ENT`) y se analizan inicialmente por separado:

| Variable | Significado |
|---|---|
| `ai_any_pct` | utiliza al menos una tecnología de IA |
| `ai_ge2_pct` | utiliza dos o más tecnologías de IA |
| `ai_ge3_pct` | utiliza tres o más tecnologías de IA |
| `ai_workflow_pct` | IA en organización de procesos o toma de decisiones |
| `ai_production_pct` | IA en procesos productivos |
| `ai_logistics_pct` | IA en logística |
| `ai_marketing_pct` | IA en marketing y ventas |
| `ai_security_pct` | IA en seguridad de TIC |

### 5.6 Columnas de la base analítica

```text
country_code
country_name
sector_code
sector_name
year
ai_any_pct
ai_any_flag
ai_ge2_pct
ai_ge2_flag
ai_ge3_pct
ai_ge3_flag
ai_workflow_pct
ai_workflow_flag
ai_production_pct
ai_production_flag
ai_logistics_pct
ai_logistics_flag
ai_marketing_pct
ai_marketing_flag
ai_security_pct
ai_security_flag
value_added_meur_ge10
persons_employed_ge10
av_size_groups_available
emp_size_groups_available
labour_productivity_keur
missing_ai_measures
ai_any_break
core_complete
balanced_entity
```

Los campos `*_flag`, disponibilidad de grupos de tamaño, faltantes y rupturas deben conservarse para auditoría; no eliminarlos por comodidad.

### 5.7 Indicadores complementarios auditados

- Combinaciones de IA con analítica/cloud: continuidad insuficiente para núcleo principal.
- Forma de adquisición o desarrollo de IA: aproximadamente 170–197 celdas por año; posible anexo o análisis secundario.
- Barreras para no adoptar: aproximadamente 160–181 celdas por año; posible anexo o contexto.
- Propósitos con códigos PBA/PME en 2021 y PBAM desde 2023: cambio de definición; no tratarlos como una serie homogénea.

---

## 6. Fuentes de datos

### 6.1 Eurostat

- Uso empresarial de IA, `isoc_eb_ai`:
  <https://ec.europa.eu/eurostat/databrowser/view/isoc_eb_ai/default/table?lang=en>
- Indicadores adicionales de IA, `isoc_eb_ain2`:
  <https://ec.europa.eu/eurostat/databrowser/view/isoc_eb_ain2/default/table?lang=en>
- Metadatos de la encuesta TIC empresarial:
  <https://ec.europa.eu/eurostat/cache/metadata/en/isoc_e_esms.htm>
- Portal de Structural Business Statistics:
  <https://ec.europa.eu/eurostat/web/structural-business-statistics/database>

Estructuras SDMX consultadas:

- <https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/structure/dataflow/ESTAT/isoc_eb_ai/1.0?detail=referencepartial&references=descendants>
- <https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/structure/dataflow/ESTAT/isoc_eb_ain2/1.0?detail=referencepartial&references=descendants>

Facundo aportó dos archivos comprimidos con estructuras SDMX:

- `ESTAT_ISOC_EB_AI_1.0.xml.gz`
- `ESTAT_ISOC_EB_AIN2_1.0.xml.gz`

En el entorno de trabajo del 18/09/2026 estaban en:

```text
/workspace/scratch/ec88d04dace5/upload/01-ESTAT_ISOC_EB_AI_1.0.xml.gz
/workspace/scratch/ec88d04dace5/upload/02-ESTAT_ISOC_EB_AIN2_1.0.xml.gz
```

Esas rutas son transitorias. Los dos Excel analíticos sí están versionados en GitHub.

### 6.2 Por qué SBS

SBS significa **Structural Business Statistics** o estadísticas estructurales empresariales. Eurostat provee allí el valor agregado y las personas ocupadas con desglose país–sector–año. La productividad se construye, no se toma como una variable misteriosa externa:

```text
productividad laboral aparente = valor agregado / personas ocupadas
```

Se debe revisar que numerador y denominador usen cobertura sectorial y empresarial compatible.

---

## 7. Estrategia econométrica

### 7.1 Especificación principal

\[
\ln(Productividad_{cst})=
\beta IA_{cst}+\alpha_{cs}+\gamma_{ct}+\varepsilon_{cst}
\]

Donde:

- `c`: país.
- `s`: sector.
- `t`: año.
- `ln(Productividad)`: logaritmo de valor agregado por persona ocupada.
- `IA`: porcentaje de empresas que usa IA o uno de sus usos funcionales.
- `α_cs`: efectos fijos de entidad país–sector; eliminan diferencias permanentes de cada combinación.
- `γ_ct`: efectos fijos país–año; absorben shocks comunes a todos los sectores de un país en un año.
- `ε_cst`: componente no observado.
- Errores estándar: agrupados por entidad país–sector.

`β` compara cambios de IA y productividad dentro de la misma entidad, netos de shocks país–año. Si IA está expresada en puntos porcentuales, `β` es el cambio aproximado en log-productividad ante un aumento de un punto porcentual. Para comunicar un aumento de 10 puntos, usar `100 × (exp(10β) − 1)`.

### 7.2 Especificaciones comparativas

- **M1:** efectos fijos de país, sector y año.
- **M2:** efectos fijos de entidad país–sector y año.
- **M3:** efectos fijos de entidad país–sector y país–año. Es la preferida preliminar.

La diferencia entre M1 y M2/M3 ayuda a mostrar cuánto de la asociación en niveles proviene de diferencias estructurales persistentes.

### 7.3 Heterogeneidad sectorial

\[
\ln(Productividad_{cst})=
\beta IA_{cst}+
\sum_{s\neq s_0}\delta_s(IA_{cst}\times Sector_s)+
\alpha_{cs}+\gamma_{ct}+\varepsilon_{cst}
\]

- `s0` es el sector de referencia omitido.
- `β` es la pendiente estimada del sector de referencia.
- `δ_s` es cuánto difiere la pendiente del sector `s` respecto de la referencia.
- La pendiente del sector `s` es `β + δ_s`.

Los efectos fijos de entidad absorben los niveles constantes de sector, pero **no** absorben una interacción entre un indicador que varía en el tiempo y el sector. Esta corrección ya fue incorporada al plan luego de una revisión de Codex.

Con tres olas, las interacciones deben presentarse como evidencia exploratoria de heterogeneidad asociativa, con intervalos de confianza y control del problema de comparaciones múltiples. No sobrecargar un único modelo con todos los usos altamente correlacionados.

### 7.4 Robusteces previstas

- Panel balanceado frente a muestra no balanceada.
- Estimaciones ponderadas por personas ocupadas.
- Sensibilidad a valores extremos.
- Efectos fijos alternativos.
- Tratamiento de precios, inflación, PPS/PPP o deflactores.
- Adopción general, intensidad y usos específicos en modelos separados.
- Diagnóstico de multicolinealidad.
- Exclusión o tratamiento explícito de rupturas marcadas por flags.
- Errores estándar alternativos cuando sea defendible.
- Ajuste o disciplina por comparaciones múltiples.
- Validación con `statsmodels` o, preferentemente para panel, `linearmodels`.

No elegir la especificación final solamente porque arroja significatividad estadística.

---

## 8. Resultados preliminares ya obtenidos

Estos resultados sirven para orientar el trabajo; **no son conclusiones finales**.

### 8.1 Evolución agregada

- Adopción general media: **9,2 % en 2021** y **17,2 % en 2024**.
- Productividad nominal media: **61,8** a **72,8 miles de euros corrientes por persona**.

### 8.2 Correlaciones en niveles con log-productividad

| Indicador | Pearson r |
|---|---:|
| Adopción general | 0,564 |
| Dos o más tecnologías | 0,497 |
| Tres o más tecnologías | 0,463 |
| Procesos y decisiones | 0,533 |
| Producción | 0,504 |
| Logística | 0,418 |
| Marketing y ventas | 0,414 |
| Seguridad informática | 0,438 |

### 8.3 Correlaciones de cambios 2021–2024

| Indicador | Pearson r |
|---|---:|
| Adopción general | -0,217 |
| Dos o más tecnologías | -0,220 |
| Tres o más tecnologías | -0,209 |
| Procesos y decisiones | -0,059 |
| Producción | -0,135 |
| Logística | 0,027 |
| Marketing y ventas | -0,268 |
| Seguridad informática | -0,120 |

La diferencia entre niveles y cambios es central: sectores/países estructuralmente más productivos también pueden adoptar más IA, pero eso no implica que los aumentos recientes de adopción estén acompañados por aumentos contemporáneos de productividad.

### 8.4 Modelo M3 preliminar

| Indicador | β por 1 pp | EE agrupado | p | efecto estimado de +10 pp |
|---|---:|---:|---:|---:|
| Adopción general | -0,001071 | 0,001265 | 0,398 | -1,06 % |
| Dos o más tecnologías | -0,001534 | 0,001343 | 0,255 | -1,52 % |
| Tres o más tecnologías | -0,001913 | 0,001918 | 0,320 | -1,89 % |
| Procesos y decisiones | -0,000294 | 0,002263 | 0,897 | -0,29 % |
| Producción | -0,001110 | 0,002447 | 0,651 | -1,10 % |
| Logística | 0,001014 | 0,011415 | 0,929 | 1,02 % |
| Marketing y ventas | -0,003780 | 0,002962 | 0,203 | -3,71 % |
| Seguridad informática | -0,001204 | 0,003275 | 0,714 | -1,20 % |

Ningún coeficiente M3 es estadísticamente significativo a niveles convencionales. Para adopción general: `n = 627`, `clusters = 209`.

Interpretación correcta:

- Existe una asociación positiva clara en niveles.
- Esa relación no aparece como una asociación temporal robusta al introducir controles exigentes.
- No se ha demostrado que la IA reduzca productividad.
- No se ha demostrado que sea ineficaz.
- El patrón es compatible con diferencias estructurales, maduración lenta, inversiones complementarias, shocks, causalidad inversa o limitaciones de medición.

### 8.5 Limitación técnica actual

La primera versión de los modelos se implementó mediante álgebra OLS con `numpy`/`scipy` porque `statsmodels` no estaba disponible en aquel entorno. Es imprescindible replicar las estimaciones con una biblioteca econométrica estándar y comparar coeficientes, errores, grados de libertad y tratamiento de efectos absorbidos antes de usarlos en la tesina.

---

## 9. Estado real del repositorio y PR

### 9.1 Rutas

En la computadora de Facundo:

```text
C:\Users\54358\TFG_Facundo_Diaz_Larrarte
```

En el entorno Codex usado para este handoff:

```text
/workspace/scratch/ec88d04dace5/TFG_Facundo_Diaz_Larrarte
```

La segunda ruta es transitoria. GitHub es el respaldo persistente.

### 9.2 `main` al crear este documento

Commit de referencia: `9ad20a0` (merge del PR #5).

Archivos principales:

```text
Facundo_Diaz_Larrarte_TFG/
├── Datos/
│   ├── base_analitica_ia_productividad_ue27_v0_1.xlsx
│   └── analisis_descriptivo_ia_productividad_ue27_v0_1.xlsx
├── Graficos/
│   └── fig1.png
├── Imagenes/
│   ├── fce_logo.png
│   └── unrc_logo.png
├── plan_trabajo.tex
├── referencias.bib
└── trabajo_final.tex

Programa Seminario Taller TGF II.docx
Res-260-02-Tesis.pdf
```

El plan y `trabajo_final.tex` deben tratarse como plantillas o versiones de trabajo; antes de redactar, sincronizar con Overleaf.

### 9.3 Historial de PR relevante

| PR | Estado al 18/09/2026 | Contenido |
|---|---|---|
| [#1](https://github.com/Facundo-Diaz-Larrarte/TFG_Facundo_Diaz_Larrarte/pull/1) | **Abierto** | análisis descriptivo, CSV procesado, scripts, modelos y outputs |
| [#2](https://github.com/Facundo-Diaz-Larrarte/TFG_Facundo_Diaz_Larrarte/pull/2) | Fusionado | primer plan de trabajo |
| [#3](https://github.com/Facundo-Diaz-Larrarte/TFG_Facundo_Diaz_Larrarte/pull/3) | Fusionado | antecedentes y redefinición como replicación/extensión |
| [#4](https://github.com/Facundo-Diaz-Larrarte/TFG_Facundo_Diaz_Larrarte/pull/4) | Fusionado | heterogeneidad sectorial y corrección de interacciones |
| [#5](https://github.com/Facundo-Diaz-Larrarte/TFG_Facundo_Diaz_Larrarte/pull/5) | Fusionado | incorporación de los dos Excel |

### 9.4 Contenido del PR #1 que todavía no está en `main`

```text
analysis/01_descriptivo.py
analysis/02_modelos_panel.py
analysis/README.md
analysis/requirements.txt
data/processed/README.md
data/processed/panel_analitico.csv
outputs/descriptivo_v0_1/...
outputs/modelos_panel_v0_1/...
```

No asumir que estos archivos están fusionados sólo porque los Excel ya están en `main`.

Comandos de reproducción actuales desde la raíz, una vez disponible el contenido de esa rama:

```bash
python analysis/01_descriptivo.py \
  --input data/processed/panel_analitico.csv \
  --output-dir outputs/descriptivo_v0_1

python analysis/02_modelos_panel.py \
  --input data/processed/panel_analitico.csv \
  --output-dir outputs/modelos_panel_v0_1
```

Antes de fusionar el PR #1:

1. actualizar su rama con `main` sin borrar trabajo;
2. revisar conflictos y duplicación de los Excel;
3. ejecutar ambos scripts;
4. validar que los outputs reproducidos coincidan;
5. revisar dependencias y añadir versión estándar del modelo;
6. dejar que Facundo decida o autorice la fusión.

### 9.5 Convención de trabajo con Git

1. `git fetch` y revisar `git status`.
2. Partir del `main` actualizado.
3. Crear una rama breve por tarea.
4. Hacer cambios acotados y verificables.
5. Ejecutar pruebas o reproducción.
6. Commit descriptivo.
7. Push y PR.
8. No mezclar correcciones académicas, datos y refactors grandes en un mismo PR cuando puedan separarse.
9. No hacer `reset --hard`, `checkout --` destructivo ni sobrescribir cambios de Facundo.
10. No fusionar ni cerrar PR sin autorización expresa.

---

## 10. Antecedentes académicos y originalidad

La relación IA–productividad ya fue estudiada. El TFG sigue siendo válido porque una tesina no necesita inaugurar un campo: debe formular una pregunta clara, utilizar un método defendible, reproducir evidencia y aportar una comparación o extensión bien delimitada.

### 10.1 Trabajos cercanos ya identificados

- Brynjolfsson, Rock y Syverson (2021), *The Productivity J-Curve*.
  DOI: <https://doi.org/10.1257/mac.20180386>
- Czarnitzki, Fernández y Rammer (2023), *Artificial Intelligence and Firm-Level Productivity*.
  DOI: <https://doi.org/10.1016/j.jebo.2023.05.008>
- Kádárová et al. (2026), *Artificial Intelligence Adoption and Labour Productivity in Slovakia and the EU27*.
  DOI: <https://doi.org/10.3390/su18042135>
- Aldasoro et al. (2026), *AI Adoption, Productivity and Employment: Evidence from European Firms*, BIS Working Paper 1325.
  <https://www.bis.org/publ/work1325.htm>
- Yilmaz (2026), *AI Adoption Velocity, Productivity and Labour Outcomes in Europe: A Country-Sector Dataset...*
  DOI: <https://doi.org/10.17632/gznvk45cfk.1>
- Wooldridge (2010), *Econometric Analysis of Cross Section and Panel Data*, para metodología.

### 10.2 Aporte propio defendible

- reconstrucción independiente y reproducible con fuentes oficiales;
- adopción general frente a funciones empresariales específicas;
- correlación entre unidades frente a variación dentro de cada país–sector;
- heterogeneidad sectorial de las pendientes;
- discusión crítica entre adopción e integración productiva;
- auditoría explícita de comparabilidad, rupturas y precios.

No presentarse como “el primero” en estudiar IA y productividad. Presentarse como una replicación/extensión transparente con énfasis propio.

### 10.3 Estructura sugerida de la revisión bibliográfica

1. Adopción tecnológica en la empresa.
2. IA, tareas y procesos.
3. Organización, habilidades y activos complementarios.
4. Productividad, costos de ajuste y curva J.
5. Problemas de medición y causalidad inversa.
6. Evidencia empírica empresarial y europea.
7. Brecha específica que cubre esta tesina.

Una fuente argentina como nadIA puede servir para contexto o revisión de literatura, pero no es directamente comparable con el panel Eurostat ni debe reemplazar la fuente empírica central. Las exploraciones previas con BTOS/FAT o un enfoque exclusivamente argentino quedan como antecedentes de ruta, no como diseño vigente.

---

## 11. Repositorios y herramientas auxiliares

### 11.1 Stack operativo recomendado

| Herramienta | Rol | Estado/decisión |
|---|---|---|
| Orca/Codex | código, datos, documentación, auditoría y PR | núcleo de trabajo |
| GitHub | fuente de verdad para versiones y revisión | activo |
| Overleaf | fuente de verdad para manuscrito LaTeX | activo/canónico |
| ChatGPT Deep Research | búsquedas bibliográficas acotadas y verificadas | recomendado; no requiere contratar API aparte |
| Zotero | biblioteca y deduplicación de referencias | opcional, recomendado |
| STORM | investigación asistida | **descartado por requisito de API** |

### 11.2 Repositorios de ayuda considerados

#### A. Scientific Agent Skills

- Repositorio: <https://github.com/K-Dense-AI/scientific-agent-skills>
- Objetivo: disponer en Codex de rutinas de revisión, búsqueda, citas, escritura y análisis científico.
- Estado: candidato recomendado; no asumir que está instalado.
- No instalar el paquete completo sin necesidad. Instalar sólo habilidades relevantes y revisar sus instrucciones.
- Habilidades de interés:
  - `literature-review`
  - `research-lookup`
  - `citation-management`
  - `scientific-writing`
  - `hypothesis-generation`
  - `scientific-critical-thinking`
  - `statistical-analysis`
  - `exploratory-data-analysis`
- Comando que se había considerado, sujeto a verificar la documentación vigente:

```bash
npx skills add K-Dense-AI/scientific-agent-skills
```

Preferir instalación acotada al proyecto. Ninguna habilidad sustituye la decisión metodológica ni la verificación humana.

#### B. GPT Researcher

- Repositorio: <https://github.com/assafelovic/gpt-researcher>
- Posible rol: descubrimiento estructurado y elaboración de informes de búsqueda.
- Estado: considerado, no instalado.
- Restricción: puede requerir proveedores, claves o configuración de modelos. Como Facundo no quiere depender de una API adicional, se prefiere ChatGPT Deep Research salvo que exista una configuración local legítima que no agregue ese requisito.

#### C. PaperQA2

- Repositorio oficial identificado: <https://github.com/Future-House/paper-qa>
- Posible rol: preguntas y síntesis con respaldo en un corpus local de papers previamente verificados.
- Estado: considerado, no instalado.
- Restricción: puede requerir configuración de proveedor/modelo. No incorporarlo hasta comprobar que encaja con el requisito de no contratar otra API.
- Buen uso: consultar PDFs verificados y rastrear evidencia.
- Mal uso: tomar sus respuestas como prueba de que una cita existe o refleja fielmente el paper.

#### D. OpenDraft

- Posible rol inicialmente discutido: capa de apoyo a redacción.
- Estado: **no instalado y upstream exacto no validado**. Existen varios proyectos con ese nombre.
- Acción: no clonar ni citar un repositorio concreto hasta revalidar identidad, mantenimiento, licencia y compatibilidad.
- En cualquier caso, Overleaf seguirá siendo canónico; la escritura también puede hacerse directamente con Codex y revisión humana.

#### E. Research Pilot

- Estado: descartado por baja madurez observada en la exploración inicial.

### 11.3 Flujo de investigación asistida recomendado

1. Definir una pregunta bibliográfica acotada.
2. Usar ChatGPT Deep Research o búsqueda directa para descubrir papers.
3. Verificar DOI, revista, autores, año y texto completo en fuentes originales.
4. Registrar cada antecedente en una matriz de evidencia.
5. Guardar los PDFs legítimamente accesibles y, sólo si aporta valor, usar PaperQA2 sobre ese corpus.
6. Usar Scientific Agent Skills/Codex para crítica, síntesis, estructura y análisis.
7. Redactar con trazabilidad; integrar la versión definitiva en Overleaf.

No instalar todos los repositorios a la vez. Incorporar una herramienta sólo cuando resuelva una necesidad concreta y después de comprobar dependencias, licencias y uso de API.

---

## 12. Próximos pasos, en orden

### Prioridad 0 — Ordenar el repositorio

- Revisar y actualizar el PR #1 sobre el `main` actual.
- Resolver posibles duplicados/rutas de los Excel.
- Ejecutar scripts y verificar reproducibilidad.
- No fusionar sin revisión/autorización.

### Prioridad 1 — Cerrar el protocolo empírico

- Congelar pregunta, variables, muestra principal y especificaciones antes de buscar resultados “convenientes”.
- Escribir una tabla de especificaciones principales y robusteces.
- Definir sector de referencia y criterio de comparaciones múltiples.
- Documentar cómo se tratarán precios y flags.

### Prioridad 2 — Matriz de literatura

Crear una tabla con:

```text
referencia | pregunta | nivel de datos | países/años | variable IA |
resultado de productividad | método | causal/asociativo | hallazgo |
limitaciones | relación con este TFG | cita verificada
```

La búsqueda debe cubrir adopción, usos/tareas, complementariedades, curva J, evidencia europea y heterogeneidad sectorial.

### Prioridad 3 — Auditoría final de datos

- Confirmar códigos, unidades y filtros de tamaño.
- Verificar valor agregado y empleo para cada celda.
- Auditar faltantes y rupturas.
- Investigar deflactores, índices de volumen o PPS/PPP adecuados.
- Mantener un diccionario de datos reproducible.

### Prioridad 4 — Descriptivo sectorial definitivo

- Perfiles de adopción y usos por sector/año.
- Productividad por sector/año.
- Mapas o rankings sólo si son legibles y relevantes.
- Niveles frente a cambios.
- Identificación descriptiva de brechas sin atribuir causas empresariales.

### Prioridad 5 — Modelos validados

- Replicar M1–M3 con `linearmodels`/`statsmodels`.
- Estimar interacciones sectoriales.
- Reportar pendientes sectoriales completas (`β + δ_s`), intervalos y tests conjuntos.
- Mantener usos en especificaciones separadas.
- Ejecutar robusteces predefinidas.

### Prioridad 6 — Tablas, gráficos e interpretación

- Tabla descriptiva de muestra y cobertura.
- Evolución de adopción/productividad.
- Comparación de correlaciones en niveles y cambios.
- Tabla de modelos principales.
- Gráfico de coeficientes por uso.
- Gráfico de pendientes sectoriales con intervalos.
- Redactar mecanismos como hipótesis compatibles, no como diagnósticos demostrados.

### Prioridad 7 — Redacción

- Metodología y datos primero, porque ya están avanzados.
- Luego resultados, marco teórico, introducción y conclusiones.
- Revisión final de lenguaje causal y consistencia entre texto, tablas, código y bibliografía.

---

## 13. Criterios para interpretar la idea central de Facundo

El análisis **sí puede** ayudar a responder:

- qué sectores presentan mayor o menor adopción;
- qué usos se difunden más en cada sector;
- qué sectores son más productivos en promedio;
- si la asociación IA–productividad cambia entre sectores;
- si la correlación transversal se mantiene al observar variaciones internas;
- dónde aparece una brecha descriptiva entre rápida adopción y resultados productivos contemporáneos.

El análisis **no puede** responder directamente:

- si una empresa concreta eligió la herramienta correcta;
- si debió usar software determinístico en vez de IA;
- cuánto gastó, cuánto ahorró o cuál fue su retorno;
- si la implementación fue técnicamente buena o mala;
- qué proceso específico debería rediseñar;
- cuál es el efecto causal de la IA sin supuestos adicionales fuertes.

Una redacción válida sería:

> La ausencia de una asociación positiva contemporánea en determinados sectores puede ser compatible con diferencias en la intensidad y calidad de integración, costos de ajuste, inversiones complementarias o plazos de maduración, pero los datos agregados no permiten distinguir entre estos mecanismos.

Una redacción inválida sería:

> Las empresas del sector usan mal la IA y deberían reemplazarla por automatización convencional.

---

## 14. Lista de control para el agente que retome

- [ ] Leí este documento completo.
- [ ] Revisé `git status`, ramas y PR antes de editar.
- [ ] Confirmé si Overleaf tiene una versión más nueva del manuscrito.
- [ ] No mencioné el proyecto empresarial privado.
- [ ] Mantuve el alcance de una tesina de Economía.
- [ ] Separé descripción, asociación e inferencia causal.
- [ ] No hice afirmaciones a nivel empresa con datos agregados.
- [ ] Verifiqué DOI/URL y contenido antes de sumar una referencia.
- [ ] No mezclé indicadores con definiciones incompatibles.
- [ ] No instalé herramientas que exijan una API adicional sin autorización.
- [ ] Reproduje los resultados antes de modificarlos.
- [ ] Informé comandos, verificaciones y limitaciones.
- [ ] Abrí un PR claro y no lo fusioné sin autorización.

---

## 15. Mensaje breve de continuidad

El TFG es viable y no debe pivotearse. El hallazgo preliminar —asociación positiva en niveles, pero ausencia de una relación temporal robusta con efectos fijos exigentes— no es un fracaso: es precisamente una razón para distinguir adopción de realización productiva y estudiar heterogeneidad sectorial con prudencia. La meta inmediata no es buscar significatividad, sino consolidar reproducibilidad, comparabilidad, robustez e interpretación económica.
