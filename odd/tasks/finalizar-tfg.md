# Finalizar el TFG

**Estado:** en curso
**Rama de trabajo:** `feature/finalize-tfg` (mismo directorio de trabajo; sin worktree separado)
**Fuente del plan detallado:** `Facundo_Diaz_Larrarte_TFG/PLAN_ATAQUE_TFG.md`
**Registro de hallazgos:** `Facundo_Diaz_Larrarte_TFG/AUDITORIA_TFG_TAREAS.md`
**Alcance:** resolver las tareas abiertas de auditoría, una por vez; mantener evidencia, reproducibilidad y consistencia entre manuscrito, anexos, presentación, guion y PDF final.
**Reanudación:** el usuario autorizó continuar hasta terminar. Priorizar tareas independientes; detenerse solo ante decisiones sustantivas que requieran al autor/dirección o datos institucionales. No hacer revisión nativa por tarea; conservarla para el cierre acotado.

## Decisiones y límites vigentes

- La productividad del estudio es **nominal**; conservar el cociente de valor agregado por persona ocupada, con `AV_MEUR` a precios básicos desde 2021.
- La aproximación de productividad real que mezcla SBS y Cuentas Nacionales está retirada por completo del TFG activo: no usarla en análisis, resultados, robusteces, conclusiones ni instrucciones de reproducción. Conservar sus artefactos sin borrarlos ni sobrescribirlos, marcados ARCHIVADO — NO USAR; el script 05 debe rechazar su ejecución.
- No convertir asociaciones en afirmaciones causales; presentar mecanismos no medidos como hipótesis o explicaciones plausibles.
- Mantener intactos los cambios previos sin commit del usuario. En el commit propio, excluir cualquier hunk preexistente y los PDF generados que incorporen cambios ajenos a la tarea.
- Cerrar cada tarea solo después de comprobar sus artefactos de salida; para cambios de manuscrito, revisar la compilación y el PDF.

## Tarea cerrada: T18

**Resolución autoritativa posterior del autor (prevalece sobre el registro histórico):** la proxy de productividad real SBS–Cuentas Nacionales queda retirada por completo del TFG activo por incompatibilidad de universos. No puede usarse en análisis, resultados, robusteces, inferencia, conclusiones, entregables ni instrucciones de reproducción. `analysis/05_productividad_real_sectorial.py`, `data/processed/panel_analitico_productividad_real.csv` y `outputs/modelos_panel_v0_3/` se preservan sin borrado sólo como archivo histórico trazable, marcado **ARCHIVADO — NO USAR**. El script 05 rechaza deliberadamente toda ejecución para impedir regenerar o sobrescribir esas salidas.

El registro anterior de exclusión inferencial se conserva como antecedente, pero no autoriza una presentación exploratoria, una comparación nominal-real ni una restauración futura sin una nueva decisión metodológica explícita del autor.

**Verificación histórica:** build aislado del seminario (7 páginas, citas resueltas); texto extraído confirma el cambio en páginas 3–4 y 6. `git diff --check` pasó. No hay prueba RED aplicable a corrección de prosa/documentación. Commit no creado por falta de autorización explícita; los PDF del repositorio permanecieron intactos.

## Tarea cerrada: T19

Como no se encontró el código original, se implementó una reconstrucción documentada en `analysis/07_heterogeneidad_sectorial.py`, con salida `outputs/modelos_panel_sectorial_v0_1/heterogeneidad_sectorial.csv` y cuatro pruebas focalizadas. La especificación usa adopción general en puntos porcentuales, log-productividad SBS nominal, muestra core con outcome positivo (N=667; 233 entidades), FE país--sector y país--año, manufactura como referencia y covarianza cluster-debiased por entidad. Las pendientes sectoriales son contrastes $w'Vw$; el estadístico firmado es z y la inferencia usa Wald asintótico χ²(1). La tabla reproduce los nueve resultados a la precisión publicada. No se afirma recuperar el código original ni causalidad.

Se corrigieron tabla/nota de la tesina, fuente de la presentación, atribuciones del guion, mención metodológica del seminario y la lectura sectorial en la matriz bibliográfica. Tests: 4/4. Builds aislados y extracción: tesina 41 páginas, presentación 28, guion 16, seminario 7 y matriz 7; citas resueltas, pasajes revisados. Persisten advertencias de overfull/underfull boxes listadas en el informe de verificación. Los PDFs del repo y artefactos T18/v0.3 permanecieron intactos. Commit no creado por falta de autorización explícita.

## Tarea T20 — implementación completa; verificación consolidada pendiente

Se ajustó el lenguaje de muestra en tesina, presentación, guion, seminario y README para distinguir el universo de 729 celdas, el core 667/233 con productividad y adopción general, y los N listwise por indicador/escenario. Por indicación del usuario, la compilación y revisión quedan para el control consolidado al final. No se regeneraron outputs existentes.

## Tarea T21 — implementación completa; verificación consolidada pendiente

Se añadió `analysis/08_sensibilidad_cluster_m3.py`, dos pruebas focalizadas, `outputs/inferencia_v0_1/sensibilidad_cluster_m3.csv` y la explicación en README. En la misma muestra y M3, 667 filas/233 entidades/81 país--año/27 países, β permanece −0,001263; SE/p pasan de 0,000884/0,15410 (una vía) a 0,000939/0,17955 (dos vías entidad+país--año). La sensibilidad cambia solo la covarianza, no el estimando. La inferencia se deja como aproximada por 27 grupos país y T=3. Los materiales de defensa ya recibieron la descripción del resultado; compilación/revisión final diferidas conforme a la preferencia del usuario.

## Tarea T22 — implementación completa; verificación consolidada pendiente

Se delimitó la interpretación del contraste de ortogonalidad RE/Mundlak-CRE a lo largo de todo el corpus (`trabajo_final.tex`, `presentacion_tfg.tex`, `guion_defensa_tfg.tex` y `matriz_bibliografia_marco_teorico.tex`). Se desarmaron las caracterizaciones de M3 como "mandatorio", "único consistente" o prueba causal. Se explicitó la hipótesis nula exacta de cada especificación probada: la regresión auxiliar sin controles temporales contrasta $H_0:\ \texttt{ai\_mean}=0$ arrojando $\chi^2(1)=69,10$ ($p<0,001$), mientras que con dummies globales de año da $\chi^2(1)=108,98$ ($p<0,001$). Se aclaró que ninguna equivale a M3 con efectos país--año y que el rechazo aporta evidencia contra la ortogonalidad RE/CRE bajo sus supuestos, justificando la elección de M3 por diseño (absorción de heterogeneidad país--sector y país--año) y no como imposición matemática de un test. Por indicación del usuario, la compilación y revisión visual quedan diferidas al control final consolidado.

## Tarea T23 — implementación completa; verificación consolidada pendiente

Se corrigieron las formulaciones problemáticas en las diapositivas y en el guion de defensa. En la Diapositiva 8 (`presentacion_tfg.tex:381`), se eliminó la afirmación de que la asociación "se disipa por completo", precisando que el coeficiente de adopción general en M3 ($-0,0013$) no resulta estadísticamente significativo a niveles convencionales ($p=0,154$), lo cual no equivale a demostrar una asociación nula. En la Diapositiva 13 de conclusiones (`:502-503`), se separó explícitamente el estimando descriptivo de la correlación de cambios 2021--2024 ($r=-0,229$, $p<0,01$) respecto al estimador condicional M3, eliminando el término "se desvanece" y evitando aceptar la hipótesis nula como prueba de efecto cero. Los textos correspondientes del guion (`guion_defensa_tfg.tex`) fueron alineados con esta distinción. Compilación y verificación diferidas al cierre consolidado.

## Tarea T25 — implementación completa; verificación consolidada pendiente

Se reconciliaron las referencias y citas entre `trabajo_final.tex`, `presentacion_tfg.tex`, `guion_defensa_tfg.tex`, `matriz_bibliografia_marco_teorico.tex` y `referencias.bib`. Se agregaron las entradas empíricas clave (Czarnitzki et al. 2023, Aldasoro et al. 2026 / BIS-EIB, Kádárová et al. 2026, Yilmaz 2026) a la guía bibliográfica de defensa en `guion_defensa_tfg.tex:502-515`. Todas las diapositivas de bibliografía de la presentación (1/3, 2/3 y 3/3) coinciden exactamente con las claves de `referencias.bib` y el estilo APA 7.ª edición.

## Tarea T43 y T44 — implementación completa; verificación consolidada pendiente

En `trabajo_final.tex:342,409`, se delimitó con exactitud matemática el estimando y la estructura inferencial de M3. Se explicitó que, por FWL, la identificación condicional de $\beta$ proviene exclusivamente de la variación sectorial relativa entre ramas dentro de cada país--año respecto a su media histórica. Se aclaró que el clustering por entidad país--sector permite correlación serial y heterocedasticidad arbitrarias dentro de unidad asintóticamente en el número de entidades, pero no corrige error de medición ni dependencia contemporánea entre sectores (para lo cual se provee la sensibilidad de covarianza de dos vías). En WLS, se explicitó que constituye un cambio de estimando (ponderado por masa laboral) y no una prueba de composición sectorial sin descomposición formal.

## Tareas T51, T52, T53, T54, T55 y T58 — implementación completa; verificación consolidada pendiente

Se calibró la narrativa teórica y econométrica en el manuscrito (`trabajo_final.tex`):
- **T51:** Bresnahan et al. (2002) y Acemoglu & Restrepo (2018) quedan delimitados estrictamente como marcos conceptuales (complementariedades IT y modelado basado en tareas), sin atribuirles evidencia directa de IA empresarial contemporánea (`:265`).
- **T52:** Se preserva el tratamiento de productividad como nominal, fundamentado en Berndt (1991), y los efectos país--año como absorción de shocks de precios e inflación nacional agregada (`:255,725`).
- **T53:** El sesgo de Pooled OLS se formula como una vulnerabilidad teórica condicional por selección (evitando afirmar signo o magnitud probados sin identificación, `:281`).
- **T54:** La Curva J de productividad de Brynjolfsson et al. (2021) se acota explícitamente como una hipótesis interpretativa general compatible y no como una causa demostrada en este panel agregado (`:673`).
- **T55:** Se retiró la atribución causal de la mayor pendiente negativa de WLS a costos de reestructuración sectoriales, dejándola como conjetura teórica a falta de descomposición matemática formal (`:657`).
- **T58:** Las recomendaciones de política y gestión empresarial se presentan como implicancias tentativas derivadas del marco conceptual y de la ausencia de retornos contemporáneos, y no como efectos estimados de M3 (`:749`).

## Tarea cerrada: T45

**Corregir la definición operativa de productividad nominal y la aplicabilidad del código SBS.** La serie de referencia 2021+ usa `AV_MEUR` (valor agregado a precios básicos, millones de EUR) y `EMP_NR` (personas ocupadas). El cociente de este estudio es una construcción propia: `AV_MEUR × 1000 / EMP_NR`, en miles de EUR corrientes por persona ocupada. No atribuirla al código histórico `V91110` sin evidencia de que ese indicador esté disponible para la tabla 2021+ empleada. Alinear texto, fórmula, diccionario y materiales actuales de defensa; citar metadata oficial. La fuente Eurostat `sbs_esms_an_1.pdf` mapea las variables 2021+ y `isoc_se_esms.htm` documenta el cambio a precios básicos y la ruptura frente a la serie previa.

**Criterio de aceptación:** ninguna salida final llama a `AV_MEUR` valor agregado a costo de factores ni presenta `V91110` como el indicador usado en la muestra 2021/2023/2024; la fórmula, las unidades, la etiqueta nominal y las fuentes son coherentes en TeX, anexos, presentación, guion y PDF inspeccionado. Las modificaciones preexistentes de portada/figura y del guion se conservan sin incluirse en el commit T45.

## Tarea cerrada: T46

**Documentar cobertura y sensibilidad de los flags SBS sin exclusión automática.** La auditoría reporta 258 celdas fuente con status `b`, todas en 2021; 242 corresponden a 35 observaciones core de productividad (26 con ambos indicadores marcados y 9 con empleo marcado), en seis países. Revalidar esos conteos desde los insumos y scripts antes de incorporarlos a resultados. Mantener separadas las marcas fuente, las variables del panel y las observaciones analíticas; no atribuir causas más allá de las notas oficiales.

**Criterio de aceptación:** conteos de flags y su intersección con la muestra core reproducibles; impacto descrito sin exclusión automática ni causalidad no sustentada; limitación de ruptura 2021 explicada con fuentes oficiales.

## Tarea cerrada: T47

**Corregir la caracterización de Czarnitzki et al. (2023) en todas las salidas sustantivas.** El artículo de 18 páginas (DOI `10.1016/j.jebo.2023.05.008`) estudia 5.851 firmas alemanas (409 usuarias de IA) con ventas y valor agregado como medidas de output. Se eliminaron el rango +4–8% no delimitado, la atribución de productividad laboral condicionada a personal calificado y cualquier afirmación causal. Se describe la asociación positiva en especificaciones con controles observados y se conserva el límite explícito de que analizar canales de competencias requiere datos más detallados de fuerza laboral/capital humano.

**Materiales corregidos:** `trabajo_final.tex`, `matriz_bibliografia_marco_teorico.tex` y `seminario_presentacion_metodologia.tex`; el claim BIS/Aldasoro quedó separado para T48.

**Verificación:** `git diff --check` limpio. Build aislado en `C:\Users\54358\AppData\Local\Temp\T47-final-SVWpzA`; citas/referencias resueltas. Inspección visual de la página 13 de la tesina, página 2 de la matriz y página 3 del seminario, sin clipping ni solapamientos en esos pasajes. Sin pruebas automatizadas aplicables por ser corrección de prosa. Se preservaron los PDFs preexistentes del repositorio.

**Commit:** `181a2fc99f3c5a1cd0a480771d6a72dfde8e3211` — `fix(thesis): bound Czarnitzki evidence claims`; solo tres fuentes TeX, sin hunks ajenos. La revisión nativa consolidada se difiere por preferencia expresa del usuario; T47 no tiene dictamen de revisión nativa.

## Tarea cerrada: T48

**Ajustar las afirmaciones atribuidas a BIS Working Paper 1325 / EIB Working Paper 2026/02.** Se reemplazó la atribución a “transformaciones profundas de gobernanza y gestión” por los resultados realmente medidos: datos EIBIS--ORBIS 2019–2024; productividad laboral principalmente como facturación por empleado (valor agregado por empleado como robustez); estimación con adopción instrumentada de 0,041 (≈4,1%), cuya lectura causal se atribuye explícitamente a los autores y a sus supuestos de identificación. Se incorporó la heterogeneidad por tamaño y las interacciones más fuertes para software/datos y capacitación; infraestructura tiene una interacción menor positiva y organización/procesos no es significativa. Se separó evidencia firm-level de la explicación del panel sectorial propio.

**Materiales corregidos:** `trabajo_final.tex:259,703`, la fila BIS de `matriz_bibliografia_marco_teorico.tex` y la oración BIS de `seminario_presentacion_metodologia.tex:103`. Las recomendaciones de `trabajo_final.tex:747` quedan reservadas a T57/T58.

**Verificación:** builds aislados y referencias resueltas en `/tmp/T48-thesis-B0ahGd/Facundo_Diaz_Larrarte_TFG`, `/tmp/T48-matrix-24d25o` y `/tmp/T48-seminar-8v1JM4`; se inspeccionaron páginas 13 y 31 de tesina, 1 de matriz y 3 de seminario sin defectos en los pasajes. `git diff --check` limpio. Sin pruebas automatizadas aplicables; PDFs del repositorio preservados.

**Commit:** `1a43d860c4309e8f0bbd548c3ac54b11f1e609fd` — `fix(thesis): delimit BIS AI productivity evidence`; tres fuentes TeX, sin hunks ajenos. Por preferencia del usuario no se ejecutó revisión nativa por tarea; se difiere una revisión consolidada acotada al cierre.

## Tarea cerrada: T49

**Restringir el alcance atribuido a Kádárová et al. (2026).** Dado que no se localizó el texto completo, se limitó la atribución al resumen RePEc (DOI `10.3390/su18042135`): comparación descriptiva Eslovaquia–agregado UE-27, datos Eurostat 2021–2024, adopción eslovaca creciente pero por debajo de la media, productividad volátil y ausencia de asociación agregada estable/inmediata. Se quitaron la generalización a todos los Estados miembros, la división Este–núcleo y la correlación Between positiva no respaldada; se dejó claro que el contraste Between/Within pertenece al análisis propio del TFG.

**Materiales corregidos:** `trabajo_final.tex:261` y fila Kádárová de `matriz_bibliografia_marco_teorico.tex:210-214`. `plan_trabajo.tex:116` ya era descriptivo; presentación, seminario y guion no tenían afirmaciones sustantivas que corregir.

**Verificación:** builds aislados `/tmp/T49-thesis-GFMvWf/Facundo_Diaz_Larrarte_TFG` y `/tmp/T49-matrix-w4Qbrc`; referencias resueltas. Inspección de tesina p. 13 y matriz p. 3 sin clipping/overlap; geometría revisada sin texto fuera de página ni solapamientos. `git diff --check` limpio. Sin pruebas automatizadas aplicables; PDFs del repositorio preservados.

**Commit:** `c798ebf521c387ce5ebebf848bdb66a76820a25b` — `fix(thesis): bound Kadarova comparison evidence`; dos fuentes TeX, sin hunks ajenos. Revisión nativa diferida al cierre por preferencia expresa del usuario.

## Tarea cerrada: T50

**Delimitar qué evidencia aporta el dataset Yilmaz (2026).** Se conservó la cita del dataset de Ekrem Yilmaz, DOI `10.17632/gznvk45cfk.1`, y se limitó la atribución a la evidencia verificable del registro DataCite/Mendeley: 733 observaciones país--sector--año de UE-27, siete sectores, olas 2021/2023/2024/2025 y el AI Attribution Wedge (AAW) como indicador descriptivo de *screening* que combina adopción, productividad posterior y horas trabajadas; el registro declara expresamente que no es causal.

**Materiales corregidos:** `Facundo_Diaz_Larrarte_TFG/trabajo_final.tex`, `Facundo_Diaz_Larrarte_TFG/matriz_bibliografia_marco_teorico.tex`, `Facundo_Diaz_Larrarte_TFG/seminario_presentacion_metodologia.tex`, `Facundo_Diaz_Larrarte_TFG/AUDITORIA_TFG_TAREAS.md` y `odd/tasks/finalizar-tfg.md`.

**Criterio de aceptación y evidencia:** los tres materiales etiquetan el AAW como descriptivo y no causal; no presentan ausencia de correlato contemporáneo como resultado del dataset. La selección o agregación de firmas de frontera y rezagadas queda identificada como hipótesis no medida, no como hallazgo de Yilmaz. No se localizó un estudio acompañante independiente verificable ni se usaron resultados SSRN no vinculados.

**Verificación:** compilaciones aisladas sin sobrescribir los PDFs del repositorio: tesina (41 páginas) en `/tmp/T50-thesis-jiXjYn`, matriz (7 páginas) en `/tmp/T50-matrix-JWIqx8` y seminario (7 páginas) en `/tmp/T50-seminar-sTT3ld`; extracción textual confirmó los pasajes. `git diff --check` informó whitespace en el PDF preexistente modificado `Facundo_Diaz_Larrarte_TFG/trabajo_final.pdf`; no se modificó. No aplican pruebas RED por ser corrección de prosa. No se ejecutó revisión nativa por preferencia expresa del usuario.

**Commit:** no se creó ni se preparó ninguno.

## Tarea cerrada: T5

**Rebajar la explicación de la correlación transversal en niveles y su vínculo con RE.** En la conclusión de la tesina y en la diapositiva de conclusiones se reemplazó la atribución de que la asociación positiva “responde preponderantemente” a diferencias estructurales permanentes. El texto ahora limita la lectura a que el contraste entre $r\approx0,558$ y M3 nominal ($\beta\approx-0,001263$, $p\approx0,154$) es compatible con que una parte de la asociación transversal refleje heterogeneidad estructural correlacionada; no cuantifica esa parte ni establece causalidad. El Wald de Mundlak/CRE ($\chi^2=69,10$, $p<0,001$) se presenta como rechazo de la ortogonalidad en la especificación RE evaluada, compatible con heterogeneidad correlacionada y no como corroboración formal de la explicación de niveles.

**Materiales corregidos:** `Facundo_Diaz_Larrarte_TFG/trabajo_final.tex:739`, conclusión de `Facundo_Diaz_Larrarte_TFG/presentacion_tfg.tex:502`, `Facundo_Diaz_Larrarte_TFG/AUDITORIA_TFG_TAREAS.md` y esta tarea.

**Verificación:** compilaciones aisladas sin sobrescribir PDFs del repositorio: tesina (41 páginas) en `/tmp/T5-thesis-DslPCG` y presentación (28 diapositivas) en `/tmp/T5-presentation-PnAsaB`. La extracción con `pdftotext` confirmó los dos pasajes. `git diff --check` informó únicamente whitespace ya existente en `Facundo_Diaz_Larrarte_TFG/trabajo_final.pdf`, que no se modificó. No aplican pruebas RED por ser corrección de prosa; no se ejecutó revisión nativa.

**Commit:** no se creó ni se preparó ninguno.

## Matriz de tareas abiertas

| ID | Trabajo | Estado | Evidencia de cierre |
|---|---|---|---|
| T1 | Confirmar campos administrativos obligatorios y completar portada. | Pendiente (consulta institucional) | PDF final y validación administrativa. |
| T5 | Rebajar la atribución “preponderantemente” sobre la correlación en niveles y el vínculo con RE. | Resuelta | Conclusión y presentación limitan la lectura a compatibilidad con heterogeneidad correlacionada, sin cuantificar su aporte ni afirmar causalidad; builds aislados y extracción textual cotejados. |
| T18 | Retirar íntegramente la proxy real de análisis, entregables, robusteces e instrucciones activas; preservar sólo archivo histórico NO USAR y bloquear script 05. | Resuelta | Ninguna salida o instrucción activa usa la proxy; script 05 rechaza ejecución y los artefactos v0.3 permanecen archivados sin borrado. |
| T19 | Localizar/reconstruir heterogeneidad sectorial o retirar los claims. | Resuelta | Script 07, cuatro pruebas y CSV versionado reproducen los nueve contrastes Wald χ²(1); atribuciones y etiqueta z corregidas; cinco TeX builds aislados revisados. |
| T20 | Reportar N y cobertura por indicador/modelo. | Implementada (verif. diferida) | Cuadro N por especificación y distinción core/listwise incorporados en todos los TeX y README. |
| T21 | Revisar dependencia residual e inferencia agrupada con alcance explícito. | Implementada (verif. diferida) | Script 08, tabla de sensibilidad dos vías (entidad + país-año) y notas metodológicas incorporadas. |
| T22 | Precisar qué null prueba cada versión RE/Mundlak. | Implementada (verif. diferida) | Contraste Wald Mundlak/CRE acotado a la hipótesis evaluada; eliminación de afirmaciones de M3 mandatorio o causal en todo el corpus. |
| T23 | Corregir lenguaje de resultados en la presentación. | Implementada (verif. diferida) | Eliminadas expresiones 'se disipa por completo' y 'se desvanece'; distinción clara entre descriptivo y condicional. |
| T24 | Mantener v0.3/script 05 exclusivamente como archivo histórico bloqueado y reconciliar documentación activa. | Pendiente | Pipeline/README/anexo no ofrecen v0.3 como ruta reproducible; script 05 rechaza ejecución y las referencias históricas están marcadas NO USAR. |
| T25 | Reconciliar referencias/citas del manuscrito y la presentación. | Implementada (verif. diferida) | Bibliografía de presentación (3 slides) y guion alineados con referencias.bib y trabajo_final.tex. |
| T26 | Fijar muestra y estimando principales; describir faltantes. | Pendiente (decisión metodológica) | Decisión documentada y N comparables. |
| T27 | Decidir y, si se aprueba, reportar CRE con país-año como sensibilidad. | Pendiente (decisión metodológica) | Tabla/nota con alcance y prueba correctos. |
| T28 | Crear ETL reproducible desde insumos preservados, con hashes y conciliación. | Pendiente | Reconstrucción limpia sin alterar fuentes originales. |
| T29 | Documentar flags/quiebres/supresiones y sensibilidad. | Pendiente | Procedencia, política y resultados reportados. |
| T30 | Alinear README con panel no balanceado principal y sensibilidad balanceada. | Pendiente | README coincide con tablas/scripts. |
| T31 | Tabular faltantes por dimensión e indicador. | Pendiente | Tabla reproducible y explicación prudente. |
| T32 | Aclarar universo de conteo de quiebres y cruce con muestra core. | Pendiente | Conteos reconciliados y nota metodológica. |
| T33 | Confirmar normativa vigente/aplicable con Secretaría. | Pendiente (consulta institucional) | Copias oficiales y requisitos aplicables. |
| T34 | Confirmar codirección/designación y datos de portada. | Pendiente (consulta institucional) | Aprobación formal y metadatos definitivos. |
| T35 | Revisar formato, firmas y ejemplar administrativo. | Pendiente (consulta institucional) | Checklist y PDF conforme. |
| T36 | Cronometrar defensa y ajustar guion. | Pendiente | Ensayo dentro del límite confirmado. |
| T37 | Verificar endpoint, parámetros y extracción de indicadores IA. | Pendiente | Extracción archivada y reproducible. |
| T38 | Sustentar diseño de encuesta e informantes con fuentes primarias por ola. | Pendiente | Afirmaciones vinculadas a manuales/metadata. |
| T39 | Verificar claims interpretativos/recomendaciones frente a fuentes. | Pendiente | Matriz claim–fuente–pasaje–límite. |
| T40 | Documentar revisiones del indicador IA y rupturas nacionales. | Pendiente | Manuales/notas por año y sensibilidad. |
| T41 | Buscar precisión muestral de proporciones Eurostat o declarar limitación. | Pendiente | Fuente de precisión o limitación explícita. |
| T42 | Atribuir causas de faltantes solo cuando las fuentes las documenten. | Pendiente | Mapa trazable; causas desconocidas no inventadas. |
| T43 | Explicar clustering, “masa crítica” y WLS sin sobreinterpretar. | Implementada (verif. diferida) | Inferencia por entidad explicada asintóticamente; WLS acotado como estimando ponderado en trabajo_final.tex. |
| T44 | Explicar identificación condicional de M3 con FE de entidad y país-año. | Implementada (verif. diferida) | Identificación condicional acotada a variación sectorial relativa dentro de país-año en trabajo_final.tex:409. |
| T45 | Corregir valor agregado a precios básicos, fórmula propia y código SBS 2021+. | Resuelta | Texto, fórmula, unidades, fuentes y PDF final consistentes. |
| T46 | Reportar cobertura/impacto de flags SBS sin exclusión automática. | Resuelta | Tabla de sensibilidad y limitación de quiebre 2021. |
| T47 | Corregir el alcance de la cita de Czarnitzki. | Resuelta | Tres materiales corregidos, fuente cotejada y PDFs temporales inspeccionados; commit `181a2fc`. |
| T48 | Ajustar el claim sobre complementos al resultado BIS/EIB medido. | Resuelta | Tres materiales corregidos, resultados de Tabla 6 delimitados y PDFs temporales inspeccionados; commit `1a43d86`. |
| T49 | Restringir Kádárová a Slovakia–UE-27 y evidencia descriptiva. | Resuelta | Tesina y matriz acotadas al resumen; build/inspección temporal; commit `c798ebf`. |
| T50 | Tratar AAW/Yilmaz como descriptivo hasta localizar evidencia acompañante. | Resuelta | Tres materiales acotados a metadata verificable; builds aislados y extracción textual; documentación de cierre actualizada. |
| T51 | Delimitar Bresnahan y Acemoglu–Restrepo como marcos conceptuales. | Implementada (verif. diferida) | Delimitados como marcos teóricos de IT y task-based en trabajo_final.tex:265. |
| T52 | Corregir atribución de FWL/precios y soporte de deflactores. | Implementada (verif. diferida) | FE país-año limitados a absorción de inflación/shocks comunes nacionales en trabajo_final.tex:255,725. |
| T53 | Presentar sesgo de Pooled OLS como posibilidad condicional. | Implementada (verif. diferida) | Sesgo redefinido como vulnerabilidad por selección sin asumir signo/magnitud probados en trabajo_final.tex:281. |
| T54 | Usar J-curve como mecanismo general, no causalidad identificada. | Implementada (verif. diferida) | Curva J acotada como hipótesis interpretativa general compatible en trabajo_final.tex:673. |
| T55 | Retirar mecanismo sectorial de WLS o presentar descomposición reproducible. | Implementada (verif. diferida) | Eliminada atribución directa a costos de reestructuración sectorial en trabajo_final.tex:657. |
| T56 | Sustentar shocks energéticos/logísticos o mantenerlos como hipótesis. | Implementada (verif. diferida) | Delimitados como hipótesis plausible no medida para manufactura/comercio en trabajo_final.tex:681,725. |
| T57 | Acotar claims sobre motivaciones/capacidades, consultoría, SaaS y gobernanza. | Implementada (verif. diferida) | Tratados explícitamente como hipótesis interpretativas y agenda micro en trabajo_final.tex:713. |
| T58 | Presentar política como recomendación tentativa, no efecto estimado. | Implementada (verif. diferida) | Recomendaciones enmarcadas como implicancias tentativas de complementariedades en trabajo_final.tex:749. |
| T60 | Reconciliar discrepancia manual/AbsorbingLS y fijar inferencia canónica. | Pendiente | EE/p-valores trazables y tabla consistente. |

## Evidencia de trabajo

- Rama creada en el mismo worktree: `feature/finalize-tfg`.
- Verificación T45 (2026-11-05): compilación aislada de la tesina en `C:\Users\54358\AppData\Local\Temp\t45-final-QSrSW0\Facundo_Diaz_Larrarte_TFG\trabajo_final.pdf`, con BibTeX ejecutado, 41 páginas y citas/referencias resueltas. Se inspeccionaron las páginas físicas 12, 37 y 38: definición nominal correcta; diccionario completo hasta `balanced_entity`; encabezado y nota de fuente visibles, sin solapamiento ni choque con el pie. Los cinco accesos nuevos de Eurostat indican 5 de noviembre de 2026. Los PDF existentes del repositorio no se sobrescribieron.
- Advertencias no bloqueantes del build: paquete `everypage` obsoleto, destino PDF duplicado `page.1`, una caja overfull de 26.76207 pt en `trabajo_final.tex:251-252` y advertencias underfull; no hubo error fatal ni defecto visual en el contenido revisado.
- Commit T45: `76d097ae01c13bc01aacb3b7830b427eb73c213b` — `fix(thesis): correct nominal SBS productivity definition`. Incluye seis fuentes TeX/Bib; excluye PDFs, auditoría y cambios previos ajenos.
- Revisión nativa: linaje `review-39aba2b41ac1a736`, lente `review-reliability`; resultado aprobado y acknowledgement completado. La autoridad de revisión quedó consumida para este commit.
- Avance T46 verificado independientemente: 258 marcas SBS `b` (111 `AV_MEUR`, 147 `EMP_NR`, todas en 2021); 242 celdas fuente corresponden a 35 observaciones core (26 con ambos componentes, 9 solo empleo), seis países. El panel principal de 667 filas permanece intacto.
- T46: 3 pruebas unitarias pasan; los CSV de cobertura y sensibilidad se reprodujeron byte por byte en una carpeta temporal. M3: completa β=−0,001263, p=0,154, n/G=667/233; sin filas marcadas 632/232, β=−0,001097, p=0,234; sin entidades afectadas 565/198, β=−0,001352, p=0,174. PDF aislado de 41 páginas compiló con citas resueltas; build final en `C:\Users\54358\AppData\Local\Temp\t46-thesis-BJ7dP6\Facundo_Diaz_Larrarte_TFG\trabajo_final.pdf`; páginas 15, 16, 20, 27, 28 y 33 inspeccionadas sin defectos visuales.
- Commit T46: `42f9d0adecd210d3db5d8ccbd09312616a57caca` — `feat(analysis): audit SBS break-flag sensitivity`; siete archivos, 307 inserciones. La revisión nativa se difirió por decisión explícita del usuario: el forecast de cuatro revisores no se ejecutó y el linaje se abandonó con `operator_disposition`, sin dictamen. Se propone una revisión única al final sobre un candidato acotado; no sobre la rama acumulada.
