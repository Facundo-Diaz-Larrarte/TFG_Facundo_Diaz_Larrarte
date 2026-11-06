# Auditoría del Trabajo Final — tareas de corrección



**Documento auditado:** `trabajo_final.tex` y PDF compilado (42 páginas).  

**Fecha de auditoría:** 26-10-2026.  

**Alcance:** manuscrito y anexos; contraste local con CSV, scripts, README, figuras, tablas y log de LaTeX. No se modificó la tesina.  

**Uso:** resolver las tareas en orden; marcar cada casilla solo tras comprobar la corrección en el PDF final.



> Auditoría exhaustiva dentro de los materiales locales disponibles, pero no certifica la inexistencia de cualquier otro defecto. No se validaron externamente todas las referencias ni cada afirmación contra sus fuentes originales. Los hallazgos basados en el log de compilación deben revalidarse, porque el log puede no corresponder al fuente actual.



## Bloqueantes de entrega



- [ ] **T1 — Completar los datos pendientes de la portada. Prioridad alta.** `trabajo_final.tex:121,129`. En el PDF aparecen `Registro Universitario: [completar]` y `Fecha de presentación: [completar]`. Sustituirlos por datos definitivos; confirmar con Secretaría si el registro es obligatorio y completar o retirar ese campo. La normativa consultada exige que figure el año de presentación.



- [x] **T2 — Incorporar o excluir formalmente la sensibilidad de productividad real. Prioridad alta.** `trabajo_final.tex:277,655–659`; `outputs/modelos_panel_v0_3/robustez_productividad_real_adopcion_general.csv`. Para la muestra balanceada, el resultado local cambia de nominal β≈−0,001071, p≈0,250 a real aproximado β≈+0,001892, p≈0,036 (n=627). La tesis trata el problema de precios como relevante, pero no informa esta sensibilidad. Incluir método, fuente del deflactor, límites e interpretación; o retirar explícitamente esa extensión del objetivo/alcance. No presentarla como evidencia causal.



- [x] **T3 — Corregir la afirmación de “invariancia” ante diferencias de escala. Prioridad alta.** `trabajo_final.tex:525,1065–1067`. La ponderación por empleo cambia p=0,154 a p=0,032; no es invariante en significancia ni prueba formal de neutralización de escala. Describirla como sensibilidad ponderada, explicar qué estimando enfatiza y discutir el cambio de inferencia.



- [x] **T4 — Acotar qué controlan los efectos fijos país–año. Prioridad alta.** `trabajo_final.tex:405,635` y revisar discusión/conclusiones. Absorben shocks comunes a sectores dentro de cada país-año, no precios relativos específicos por sector ni otros shocks sectoriales variables en el tiempo. Reemplazar frases absolutas como “absorbe toda la inflación” y “aislando limpiamente”; armonizar con la limitación reconocida en `:1195`.



- [x] **T5 — Moderar la explicación causal de la correlación en niveles. Prioridad alta. Resuelta.** `trabajo_final.tex:739` y conclusión de `presentacion_tfg.tex:502`. Se sustituyó “responde preponderantemente” por una formulación de compatibilidad: el contraste entre $r=0,558$ y M3 nominal ($\beta\approx-0,0013$, $p\approx0,154$) puede reflejar en parte heterogeneidad estructural correlacionada, pero no cuantifica su aporte a la correlación transversal ni establece causalidad. El rechazo de ortogonalidad en el Wald de Mundlak/CRE ($\chi^2=69,10$, $p<0,001$) se describe como compatible con esa heterogeneidad bajo la especificación RE evaluada, sin corroborar formalmente la explicación. Compilaciones aisladas de tesina (41 páginas) y presentación (28 diapositivas) completaron y `pdftotext` confirmó ambos pasajes; no se sobrescribieron PDFs del repositorio. `git diff --check` informó únicamente whitespace ya existente en `trabajo_final.pdf`, que no se modificó. No aplican pruebas RED por ser corrección de prosa.



- [x] **T6 — Separar resultados empíricos de mecanismos no medidos. Prioridad alta.** Ubicación vigente: `trabajo_final.tex:736`; limitaciones `:714–716` (referencias anteriores `:1219`, `:1191–1193` obsoletas). El modelo no mide directamente capacitación, reorganización ni maduración, por lo que no permite afirmar que sean condiciones necesarias ni que la adopción sea insuficiente en general. El texto vigente las presenta como mecanismos teóricos plausibles y reconoce que no se miden; conservar esa separación y comprobarla en el PDF final.



## Consistencia entre texto, resultados y materiales reproducibles



- [x] **T7 — Completar la reproducción v0.3 o corregir lo que promete el repositorio. Prioridad alta.** `analysis/00_reproducir_todo.py:75–103`; `analysis/05_productividad_real_sectorial.py`; `analysis/README.md`; Anexo D `trabajo_final.tex:1541–1551`. El comando maestro ejecuta solo scripts 01–04, no ejecuta/verifica v0.3, aunque README afirma que incluye productividad real; el anexo también enumera solo 01–04. Integrar script 05 y verificaciones, o retirar afirmaciones contradictorias. El pipeline no se ejecutó para evitar sobrescribir salidas.



- [x] **T8 — Actualizar cifras desfasadas del README. Prioridad media.** `analysis/README.md:90–93`. Informa 17,2%, 61,8→72,8, r=0,564 y r=−0,217; CSV actuales y tesis usan 17,0%, 62,0→72,1, r=0,558 y r=−0,229. Actualizar con salidas reproducibles o versionar claramente esos valores anteriores.



- [x] **T9 — Sincronizar el diccionario del Anexo A con los nombres reales de columnas. Prioridad media.** `trabajo_final.tex:1303–1307`; `data/processed/panel_analitico.csv`. El anexo usa `value_added_meur`, `persons_employed`, `labour_productivity`; el CSV canónico contiene `value_added_meur_ge10`, `persons_employed_ge10`, `labour_productivity_keur`. Usar identificadores exactos o declarar alias conceptuales y mapearlos.



- [x] **T10 — Aclarar el umbral de significancia en M1. Prioridad media.** `trabajo_final.tex:1367,1437`. Se califica como significativo el coeficiente de adopción general con p=0,091. Indicar el umbral del 10% (si está definido y justificado) o retirar esa calificación. Mantener el criterio en tabla, prosa, resumen y conclusiones.



- [x] **T11 — Corregir la descripción de los períodos del panel balanceado. Prioridad baja.** `trabajo_final.tex:495,499`. 2021, 2023 y 2024 no son “tres años consecutivos”. Usar “tres olas/períodos observados” y buscar otras apariciones de “consecutivo”.



- [x] **T12 — Precisar qué neutralizan los cocientes y los efectos fijos de entidad. Prioridad media.** `trabajo_final.tex:517–525`. Dividir por empleo/universo genera medidas intensivas, pero no elimina composición, economías de escala o heterogeneidad de tamaño. Los efectos fijos absorben solo diferencias invariantes en el tiempo. Acotar “queda matemáticamente cancelada” y “neutraliza”.



- [x] **T13 — Revisar códigos geográficos del Anexo C. Prioridad media.** `trabajo_final.tex:1465,1485,1503`. La columna dice “Código ISO”, pero Grecia figura como `EL`, identificado en la nota como código oficial de Eurostat. Renombrar “Código geográfico Eurostat” o explicar la excepción respecto de ISO.



## Presentación y consistencia editorial



- [x] **T14 — Agregar referencias en el cuerpo a los exhibits sin citar. Prioridad media.** Tabla 1 `trabajo_final.tex:537–543` (`tab:sectores`); Figura 1 `:717–725` (`fig:adopcion-anio`); Figura 4 `:877–885` (`fig:matriz-correlaciones`). Aparecen en el documento/listados, pero no se encontró referencia desde el cuerpo. Introducirlos e interpretar qué aportan, o retirar los redundantes.



- [x] **T15 — Definir abreviaturas en su primera aparición. Prioridad media.** Ejemplos: `NACE`, `SBS`, `UE`, `TIC` en `trabajo_final.tex:225,389,495`; `SBS` se desarrolla más adelante en `:491`. Escribir el nombre completo en la primera mención y usar la forma abreviada consistentemente. Confirmar si la guía de la Facultad exige una lista; no se encontró una sección dedicada.



- [x] **T16 — Corregir “la asociación positiva se desvanece por completo”. Prioridad baja.** `trabajo_final.tex:1115`. p=0,154 indica que no se detecta asociación estadísticamente significativa en esa especificación; no demuestra que la asociación sea exactamente cero. Sustituir por una formulación de no detección coherente con las secciones más cautas.



- [x] **T17 — Recompilar y revisar el log de LaTeX contra el fuente final. Prioridad media.** `trabajo_final.log`; errores/overfull boxes señalados alrededor de `trabajo_final.tex:435,503,613,615,622`. El log conserva errores de entorno matemático y overfull boxes, pero es anterior al fuente actual; no se puede asegurar que persistan. Recompilar desde el fuente definitivo, resolverlos y revisar visualmente las páginas afectadas.



## Controles que pasaron en la revisión local



- Los exhibits revisados tienen captions y numeración secuencial coherente; las imágenes locales están presentes y los valores de las figuras descriptivas inspeccionadas coinciden con sus CSV.

- No se detectaron claves de cita del texto ausentes en `referencias.bib`.

- No se marcaron automáticamente las entradas bibliográficas no citadas: la sección se titula “Bibliografía”, no “Referencias”.

- No se encontró un marcador TODO/FIXME adicional en el manuscrito; los dos `[completar]` de portada están registrados en T1.



## Pendiente fuera de esta auditoría local



- Validar existencia/datos bibliográficos de cada referencia y comprobar que cada fuente respalde la afirmación citada. No se hizo búsqueda web ni se enviaron fragmentos del manuscrito a servicios externos; requiere una verificación separada.

- Confirmar con dirección/Facultad si corresponde declarar el uso de IA. No se localizó una regla específica en los materiales consultados; no debe inferirse que esté permitido o prohibido.



## Segunda pasada — contraste de econometría y presentación (26-10-2026)

Esta pasada amplía la auditoría anterior; no modifica ni marca como resueltas las tareas históricas. Se contrastaron fuentes TeX, resultados CSV, scripts y texto extraído de los PDF con `pdftotext`. No se recompiló ni se ejecutó el pipeline. El PDF disponible de la tesina tiene 41 páginas (no 42 como se indicaba arriba); la presentación tiene 28. El contraste fue textual, no visual.

### Hallazgos nuevos para resolver

- [x] **T18 — Excluir la serie de productividad real aproximada de la inferencia sustantiva. Prioridad alta. Resuelta.** Se retiró del seminario la afirmación de que la proxy SBS–Cuentas Nacionales es una robustez inferencial. La lista de fuentes del panel ahora enumera únicamente TIC/IA y SBS; `nama_10_a64` queda identificado aparte como proxy exploratoria descartada por incompatibilidad de universos, sin interpretación ni uso inferencial (`Facundo_Diaz_Larrarte_TFG/seminario_presentacion_metodologia.tex:116–122,171`). `analysis/README.md:124` identifica el script, panel derivado y carpeta de outputs v0.3 como artefactos preservados para trazabilidad, exploratorios/no canónicos y no válidos como robustez inferencial. No se borraron ni regeneraron artefactos. Build aislado del seminario: 7 páginas, citas resueltas; extracción de texto confirmó el cambio en pp. 3–4 y 6. `git diff --check` pasó. No aplica RED por ser corrección de prosa/documentación. Sin commit; no se autorizó commit.

- [x] **T19 — Publicar la ruta reproducible de heterogeneidad sectorial. Prioridad alta. Resuelta.** No se encontró el código original que generó la tabla, por lo que se implementó una reconstrucción explícita (no presentada como recuperación) en `analysis/07_heterogeneidad_sectorial.py`, con salida versionada `outputs/modelos_panel_sectorial_v0_1/heterogeneidad_sectorial.csv` y cuatro pruebas en `tests/test_heterogeneidad_sectorial.py`. Usa `ai_any_pct` en puntos porcentuales, log-productividad nominal, muestra core positiva (N=667; 233 entidades), FE país--sector y país--año, C como referencia y covarianza cluster-debiased por entidad. Las pendientes se calculan con contrastes completos $w'Vw$; el estadístico firmado se rotula $z$ y el p-valor proviene de Wald asintótico χ²(1), no Student-t. Los nueve coeficientes, EE, estadísticos, p-valores y efectos de 10 pp reproducen la tabla a la precisión publicada. Se corrigieron la etiqueta inferencial y la atribución errónea a `03_validacion_linearmodels.py`; guion, presentación, seminario y matriz distinguen resultados asociativos de mecanismos no medidos. Tests focalizados 4/4; cinco builds aislados (tesina 41 pp., presentación 28, guion 16, seminario 7, matriz 7) completados con citas resueltas y extracción de los pasajes revisada. Las advertencias de cajas overfull/underfull indicadas en la verificación no impidieron los builds. No se modificaron PDFs del repo ni artefactos v0.3. Sin commit; no se autorizó commit.

- [ ] **T20 — Precisar la población analítica y los faltantes por indicador. Prioridad media.** `core_complete` deja 667 casos, pero la eliminación listwise por variable hace variar N entre modelos (626–667; `analysis/02_modelos_panel.py:96–99`; `outputs/modelos_panel_v0_1/modelo_preferido.csv:2–9`). La cobertura por indicador difiere (`outputs/descriptivo_v0_1/tables/cobertura.csv:2–9`). Evitar llamar “muestra completa” a cada especificación; explicar que 667 es la muestra base con outcome/adopción general disponible y que los modelos adicionales usan N variable. Evaluar y reportar implicancias de comparabilidad/missingness.

- [ ] **T21 — Describir con precisión lo que identifica M3 y la inferencia de errores estándar. Prioridad alta (evaluar con especialista econométrico).** M3 incluye efectos fijos país-sector y país-año (`analysis/02_modelos_panel.py:28–32`; `trabajo_final.tex:396–406`), por lo que la identificación procede de cambios relativos entre sectores dentro del país-año. La inferencia agrupa por entidad país-sector (`analysis/03_validacion_linearmodels.py:67–68`), con solo tres períodos observados. Aclarar estimando/limitaciones y evaluar sensibilidad a dependencia residual común entre sectores dentro de país-año o alternativas adecuadas al panel corto. No declarar inválido el error estándar sin un contraste apropiado.

- [ ] **T22 — Acotar la conclusión del test Mundlak/Hausman. Prioridad alta.** *Implementada en código (verificación compilatoria diferida al cierre):* Contraste acotado a la hipótesis evaluada ($H_0:\ \texttt{ai\_mean}=0$); se eliminaron claims de causalidad y de "M3 mandatorio/único consistente" en `presentacion_tfg.tex`, `guion_defensa_tfg.tex`, `matriz_bibliografia_marco_teorico.tex` y `trabajo_final.tex`. El test documentado rechaza la especificación RE examinada, pero no demuestra que M3 sea “mandatorio” ni valida causalidad. La presentación usa esa formulación (`presentacion_tfg.tex:412,502`; PDF pp.13,17). Además, RE/Mundlak sin años y Mundlak con dummies de año son contrastes distintos (`analysis/03_validacion_linearmodels.py:96–116`). Describir el resultado como evidencia contra RE bajo la especificación probada; justificar M3 por el diseño/pregunta y explicar por separado el contraste con años.

- [ ] **T23 — Corregir dos formulaciones de la presentación. Prioridad media.** *Implementada en código (verificación compilatoria diferida al cierre):* Se eliminó "se disipa por completo" en Diapositiva 8 (`presentacion_tfg.tex:381`) y se separó el estimando descriptivo ($r=-0,229$) del condicional M3 en Diapositiva 13 (`:501-502`) sin usar "se desvanece", alineando también `guion_defensa_tfg.tex`. En PDF p.12 (`presentacion_tfg.tex:380–381`) se dice que la asociación “se disipa por completo”, aunque M2 tiene p≈0,050 y la tabla de la tesina muestra indicadores con significancia; no equivale a que toda asociación sea cero. En p.17 (`:501–502`) se usa “se desvanece” para resumir una correlación de cambios negativa significativa (r≈−0,229) junto con el M3 no significativo: son resultados diferentes. Reescribir distinguiendo descriptivo y condicionado, sin aceptar la hipótesis nula como prueba de efecto cero.

- [ ] **T24 — Reconciliar documentación de fuentes y reproducción v0.3. Prioridad alta.** El pipeline canónico 00 ejecuta 01–04 (`analysis/00_reproducir_todo.py:70–103`) y el README describe ese alcance; el script 05 descarga datos, usa verificación TLS deshabilitada y sobrescribe datos/salidas (`analysis/05_productividad_real_sectorial.py:73–77,104–121,163–183`). Existen CSV procesados, pero no se hallaron extractos brutos/recibos/checksums para trazabilidad completa (`data/processed/README.md:1–35`). Definir si v0.3 es exploratorio fuera del pipeline o integrarlo con insumos fechados/versionados, hashes, filtros y reproducción segura. No ejecutar el pipeline actual sin revisar sus escrituras/sobrescrituras.

- [ ] **T25 — Hacer trazable la bibliografía de la presentación y validar fuentes. Prioridad media.** *Implementada en código (verificación compilatoria diferida al cierre):* Referencias de presentación (apéndices 1/3, 2/3, 3/3) y guion de defensa reconciliadas con `referencias.bib` y `trabajo_final.tex`. Se agregaron Czarnitzki, BIS/EIB, Kádárová y Yilmaz a la guía del guion. La presentación mantiene referencias manuales (`presentacion_tfg.tex:698–727`) sin una bibliografía enlazada; la tesina usa `referencias.bib`. Reconciliar referencias y citas entre ambos documentos, e identificar entradas bibliográficas no citadas o solo de contexto. La existencia y el respaldo de cada fuente por la afirmación asociada siguen sin verificación externa; no se hizo búsqueda web en esta pasada.

- [ ] **T26 — Revisar la muestra no balanceada con efectos fijos/aleatorios y reformular el lenguaje sobre faltantes. Prioridad alta.** La grilla contiene 729 celdas posibles, 667 observaciones core y 627 en entidades balanceadas (`outputs/modelos_panel_v0_2/escenarios_robustez.csv:2–5`; `trabajo_final.tex:312–314`). FE/RE admiten panel no balanceado; los scripts ya usan la muestra core de 667 y aplican eliminación por variable, dejando N entre 626 y 667 (`analysis/02_modelos_panel.py:84–99`; `outputs/modelos_panel_v0_2/comparacion_especificaciones_principal.csv:2–25`). Eliminar filas para balancear no es necesario para estimar FE, pero “usar toda la muestra” significa usar todas las filas observadas que tengan los datos requeridos por cada regresión, no imputar automáticamente ni usar registros sin outcome/regresor. Revisar la afirmación de que el enfoque “previene sesgo de atrición” (`trabajo_final.tex:314`): conservar más filas no prueba que los faltantes sean ignorable. Documentar N por especificación, cobertura/razones observables y comparar FE principal con RE/Mundlak, explicitando supuestos; solicitar criterio de dirección para el estimando final.

- [ ] **T27 — Conservar una interpretación precisa del Mundlak/CRE. Prioridad alta.** El test titular del repositorio (Wald χ²(1)=69,10) usa RE con IA + media de IA, sin controles temporales; la variante χ²=108,98 agrega años globales, no efectos país–año de M3. Se reestimó en memoria con `.venv` (linearmodels 7.0) y la misma muestra nominal `core_complete`, outcome log-productividad, entidad país-sector y errores agrupados por entidad. M3 FE tiene n=667, G=233, β(adopción general)=−0,001263116, EE=.000884369, p=.154099. CRE convencional con dummies país–año + media IA rechaza H0: media IA=0 (Wald χ²(1)=86,606, p<10⁻¹⁹), pero su β difiere ligeramente (−0,001239480). CRE ampliado con medias de los dummies país–año coincide con FE a precisión numérica (β=−0,001263116), y la media IA también es distinta de cero (χ²(1)=84,858, p<10⁻¹⁹). El test conjunto de todas las medias (χ²(19)=1437,08) incluye patrones de observación de entidades desbalanceadas; no interpretarlo solo como endogeneidad sustantiva de IA. En las 8 medidas de IA, el coeficiente FE coincide con CRE ampliado (<6×10⁻¹⁶) y las medias de IA se rechazan individualmente; CRE convencional no coincide exactamente. El procedimiento implementado es un test Wald de restricción en una regresión CRE/Mundlak, no el estadístico clásico de diferencia FE–RE; en el RE simple con IA como único regresor variable, H0 se refiere a la media de IA. La prueba con dummies globales es otra especificación y no equivale al contraste de M3 con FE país–año. El resultado respalda rechazar la ortogonalidad del RE simple bajo esa especificación, pero no demuestra causalidad ni hace M3 “mandatorio” en sentido exclusivo. Reportar p numéricamente subdesbordado como p muy pequeño, no 0. Antes de modificar el texto, obtener criterio de dirección sobre si presentar el contraste CRE con país–año como sensibilidad metodológica.

- [ ] **T28 — Hacer reproducible y auditable la construcción de la base. Prioridad alta.** La hoja `Panel` del libro fuente-like y `data/processed/panel_analitico.csv` coinciden en las 729 claves y los 30 campos: 0 discrepancias en 21.870 celdas tras normalizar serialización numérica. Aplicando las reglas documentadas en `Resumen`, `Diccionario` y `Auditoria` a `Fuente_IA` (7.441 filas) y `Fuente_SBS` (5.635), se reconstruyen las 729 filas y la productividad; también se replican 714 valores de IA general, 676 productividades, 667 core y 627 filas balanceadas. Esto es evidencia fuerte de coherencia interna del libro/CSV, no de autenticidad o fecha efectiva de las descargas. Sigue faltando script ETL versionado, URLs/consultas/metadata de respuesta y hashes; el historial no añade esos materiales. Crear un constructor local que lea las hojas fuente y reproduzca el CSV, guardando reglas, hashes y reporte de conciliación; conservar artefactos actuales sin sobrescribirlos.

- [ ] **T29 — Definir y aplicar la política de flags, quiebres y supresión estadística. Prioridad alta.** El libro documenta `b` como quiebre de serie y recomienda no excluirlo automáticamente (`Diccionario!F15`, `Auditoria!C16`). `Fuente_IA` tiene 134 celdas `b` (56 Francia, 72 Suecia en 2023; 6 Países Bajos en 2025); en el panel principal 18 país-sector-año tienen `ai_any_break=Yes` (9 Francia + 9 Suecia en 2023), pero solo 17 son core-complete. La diferencia es Francia-L-2023, sin productividad/empleo SBS. Los scripts 01–04 preservan valores y no filtran por quiebre, pero tampoco comparan resultados con/sin observaciones afectadas. Confirmar la definición contra metadatos archivados y evaluar sensibilidad apropiada; no excluir a ciegas.

- [ ] **T30 — Alinear README con la muestra principal y los faltantes. Prioridad media.** `analysis/README.md:26–32` describe 627 como muestra balanceada, mientras tesis/scripts establecen 667 no balanceadas como principal (`trabajo_final.tex:312–314,420`; `analysis/04_robustez_panel.py:88–95`). Declarar n=667 principal, n=627 sensibilidad balanceada, y explicar N variable por indicador.

- [ ] **T31 — Examinar faltantes por país, sector, año e indicador. Prioridad media.** Cobertura general informa los conteos, pero no se encontró un cuadro de patrón/distribución de faltantes ni su relación con `*_flag`/breaks (`outputs/descriptivo_v0_1/tables/cobertura.csv:2–9`). Producir una tabla de disponibilidad por celdas y documentar qué se sabe de la no publicación; no etiquetar faltantes como aleatorios sin evidencia.

- [ ] **T32 — Aclarar en la metodología el conteo y tratamiento de quiebres de IA. Prioridad media.** Resolver discrepancia aparente: existen 18 filas `ai_any_break=Yes` en toda la grilla, pero solo 17 están en el core, de ahí `Auditoria!B8=17`; la fila FR-L-2023 queda fuera por datos de SBS ausentes. El libro declara no excluirlas automáticamente, pero el significado estadístico del status fuente `b` y sensibilidad de resultados siguen sin documentarse. Añadir una nota de definición/universo de conteo y justificar retención/exclusión con metadatos fuente.

- [ ] **T33 — Archivar y confirmar el marco normativo institucional antes del cierre. Prioridad alta.** Se localizó el texto oficial de Res. CD FCE-UNRC 260/02 (https://www.eco.unrc.edu.ar/wp-content/uploads/2022/03/Res-260-02-Tesis.pdf) en la página institucional de Asuntos Estudiantiles (https://www.eco.unrc.edu.ar/asuntos-estudiantiles/), que también identifica Res. 259/14 como modificación a requisitos de dirección de tesis. La 260/02 enumera portada, índice, introducción, cuerpo, conclusión, bibliografía y resumen; idioma castellano, A4, interlineado máximo 1,5; exposición oral máxima de 60 minutos. El programa de seminario solo cita Res. 120/2017 para acreditación de la asignatura. No se encontró localmente copia de 260/02 ni se recuperó el texto de 259/14; la página oficial lista ambas, pero confirmar con Secretaría la vigencia/concordancias exactas, Plan 2021 y modificaciones antes de certificar el cumplimiento.

- [ ] **T34 — Completar y confirmar la portada y condición del codirector. Prioridad alta.** `trabajo_final.pdf` p.1 incluye Universidad, Facultad, título, autor y director, pero mantiene `[completar]` en fecha de presentación y no muestra el año, exigido por Res. 260/02 VI.1.1. El plan propone codirectora; confirmar si fue formalmente designada e incluirla en portada final si corresponde. También queda `[completar]` el Registro Universitario; verificar si es requisito administrativo del modelo de dictamen.

- [ ] **T35 — Verificar materialmente formato y firmas. Prioridad media.** La inspección textual/metadata confirma castellano y A4 en plan y tesina, y se hallan las secciones obligatorias. No pudo comprobarse de manera fiable el interlineado máximo de 1,5 ni las firmas/avales en portada por extracción de texto. Revisar fuente/render y ejemplar administrativo contra Res. 260/02 V/VI; la línea `Fecha de presentación` aún conserva marcador.

- [ ] **T36 — Preparar la exposición dentro del máximo normativo. Prioridad media.** Res. 260/02 VII.3.3.1 limita la exposición a 60 minutos; el PDF de presentación tiene 28 diapositivas, pero la cantidad no acredita duración. Cronometrar el guion real, reservar tiempo para debate y definir una duración menor operativa acordada con dirección/tribunal.

| Indicador IA | N/G | β FE M3 | β CRE convencional | Wald media IA (χ²(1)) | β CRE ampliado |
|---|---:|---:|---:|---:|---:|
| Adopción general | 667/233 | −0,00126312 | −0,00123948 | 86,606 | −0,00126312 |
| ≥2 usos | 662/232 | −0,00165033 | −0,00161313 | 71,820 | −0,00165033 |
| ≥3 usos | 653/232 | −0,00202665 | −0,00198550 | 57,934 | −0,00202665 |
| Workflow | 662/232 | −0,00069576 | −0,00060995 | 60,995 | −0,00069576 |
| Producción | 631/229 | −0,00142087 | −0,00136945 | 72,869 | −0,00142087 |
| Logística | 627/231 | −0,00108902 | −0,00104467 | 26,002 | −0,00108902 |
| Marketing | 640/231 | −0,00383536 | −0,00380739 | 52,106 | −0,00383536 |
| Seguridad | 626/226 | −0,00186465 | −0,00177408 | 56,841 | −0,00186465 |

CRE convencional incluye dummies país–año y media de IA por entidad; CRE ampliado agrega medias linealmente independientes de las dummies país–año (18–25 columnas adicionales, según indicador). Las medias de indicadores se rechazan en cada especificación; el test conjunto ampliado puede reflejar el patrón desbalanceado. Verificación calculada con el entorno del repositorio; no se guardó output ni se modificó código.

- [ ] **T37 — Precisar el cruce de datasets Eurostat para adopción de IA. Prioridad alta.** Fuentes oficiales distinguen `isoc_eb_ai` (IA por clase de tamaño) y `isoc_eb_ain2` (IA por actividad NACE Rev. 2); ambos ofrecen `E_AI_TANY`, pero el panel país–sector debe provenir de la desagregación `isoc_eb_ain2`. El texto metodológico menciona `isoc_eb_ai` para IA general (`trabajo_final.tex:310`), mientras el Anexo A especifica `isoc_eb_ain2:E_AI_TANY` (`:784–803`) y el libro no conserva en `Fuente_IA` el ID de dataset por fila. No es una contradicción del indicador, sino trazabilidad insuficiente del endpoint usado. Alinear la fuente principal como `isoc_eb_ain2`, describir `isoc_eb_ai` solo si se usó para validación por tamaño, y archivar consultas/URL/parámetros.

- [ ] **T38 — Documentar con fuente primaria el diseño y definiciones del relevamiento TIC/IA. Prioridad media-alta.** La metadata oficial de Eurostat confirma unidad empresa, población habitual de 10+ ocupados, recogida anual por institutos nacionales, método generalmente estratificado, proporciones ponderadas por número de empresas y notas de comparabilidad por país (`https://ec.europa.eu/eurostat/cache/metadata/EN/isoc_e_esms.htm`). En cambio, no se verificó fuente para quién responde (p.ej., CIO/CTO), Reglamento UE citado ni todos los detalles del marco muestral en `trabajo_final.tex:326–351`. Citar manual/cuestionario y metadata por año; no presentar perfil del informante como regla universal sin evidencia.

- [ ] **T39 — Revisar apoyo bibliográfico de afirmaciones interpretativas y recomendaciones. Prioridad media.** Claims de complementariedades/gestión, SaaS, costos sectoriales y recomendaciones de política aparecen en `trabajo_final.tex:643–648,666–710,751–755`; el mapa local detectó afirmaciones específicas apoyadas solo por títulos de referencias o sin cita específica. Leer fuentes originales, ajustar claim a evidencia o marcarlo como hipótesis/implicancia del autor. No se validó externamente cada referencia en esta pasada.

- [ ] **T40 — Describir la estabilidad y los límites de comparabilidad temporal del indicador IA. Prioridad media-alta.** Manuales Eurostat definen `E_AI_TANY` como uso empresarial de al menos una de siete tecnologías para 2021, 2023 y 2024. Eurostat indica que tras 2021 revisó ligeramente preguntas/manual; 2023/2024 agregaron preguntas sobre fines de uso/controles, sin cambiar las siete tecnologías centrales. Hay flags `b` en Francia y Suecia 2023; la metadata advierte diferencias nacionales de traducción, período, modo, no respuesta/routing. Reportar la serie como operacionalmente consistente pero no asumir comparabilidad perfecta; explicar/mostrar sensibilidad para países con break y citar manuales/variable-specific notes.

- [ ] **T41 — Discutir error de medición/incertidumbre muestral en regresores Eurostat agregados. Prioridad media.** La adopción por país-sector es una proporción estimada mediante encuesta, pero la base conservada contiene puntos estimados y status, no error estándar/varianza de muestreo por celda; la inferencia agrupada de la regresión trata esas proporciones como observadas sin error. No se afirma que ello invalide M3: documentar la limitación, evaluar si hay precisiones oficiales disponibles y explicar que el agrupamiento por entidad no incorpora automáticamente error muestral del predictor. Si no hay precisión por celda, mantener como limitación no corregible con los datos agregados disponibles.

- [ ] **T42 — Sustentar las causas atribuidas a datos faltantes. Prioridad alta.** `trabajo_final.tex:312` atribuye los 62 casos no core al secreto estadístico o falta de relevamiento. El conteo es reproducible (53 SBS, 15 IA, 6 superpuestos), pero no se identificó para cada celda metadata que distinga confidencialidad, no publicación, falta de encuesta u otras causas. Separar el hecho observable (ausencia) de la explicación, y conservar motivo por fila solo cuando el status/notas oficiales lo sustenten.

- [ ] **T43 — Corregir el alcance atribuido a errores cluster y a la “masa crítica”. Prioridad alta.** `trabajo_final.tex:342–350` afirma que cluster-robust “absorbe heterocedasticidad por tamaño de celda”; agrupar por país-sector permite covarianza robusta dentro de conglomerado, pero no corrige específicamente error de muestreo del indicador ni heterocedasticidad “por tamaño” por diseño. El número de empleados de una celda tampoco informa el número/precisión de unidades empresariales de la encuesta. Explicar qué cubre clustering, distinguir WLS (cambia el estimando/peso) y reconocer error de medición en proporciones si no hay varianzas de muestreo.

- [ ] **T44 — Precisar la fuente de identificación de M3 en la explicación de FE. Prioridad alta.** `trabajo_final.tex:346–348` describe comparar cada sector con su trayectoria propia, pero M3 incluye además efectos país–año (`:396–406`); condicionalmente, el coeficiente se identifica con variación sectorial relativa dentro de cada país-año, además de absorber heterogeneidad país-sector permanente. Reescribir con ambos efectos y no sugerir que el mero FE de entidad garantiza por sí solo la comparación descrita.

- [x] **T45 — Corregir el concepto de valor agregado en la variable de productividad. Prioridad crítica.** Corregido en cuerpo, Anexo A y materiales de defensa: para 2021/2023/2024, `sbs_sc_ovw` aporta `AV_MEUR` (valor agregado nominal a precios básicos, millones de EUR) y `EMP_NR` (personas ocupadas); la productividad laboral aparente nominal es el cálculo propio `AV_MEUR×1000/EMP_NR`, en miles de EUR corrientes por persona ocupada. No se la denomina valor agregado a costo de factores ni se presenta como el indicador oficial `V91110`. La correspondencia de variables 2021+ confirma los componentes y mapea históricamente `AV_MEUR` a `V12150` (`https://ec.europa.eu/eurostat/cache/metadata/Annexes/sbs_esms_an_1.pdf`); los metadatos SBS y TIC documentan el valor agregado a precios básicos y el quiebre desde 2021 (`https://ec.europa.eu/eurostat/cache/metadata/en/sbs_esms.htm`; `https://ec.europa.eu/eurostat/cache/metadata/en/isoc_se_esms.htm`). La comprobación de aplicabilidad del código muestra que `V91110` pertenece a la tabla histórica `sbs_na_1a_se_r2` (2005--2020), no a los componentes 2021+ usados aquí (`https://ec.europa.eu/eurostat/databrowser/view/sbs_na_1a_se_r2__custom_9128690/d`).

- [ ] **T46 — Documentar la cobertura de flags SBS y su sensibilidad, sin excluirlos automáticamente. Prioridad alta.** Implementación pendiente de verificación del padre: `analysis/06_auditar_flags_sbs.py` agrega `status=b` de `Fuente_SBS` por país--sector--año entre clases de tamaño y genera `cobertura_flags_sbs.csv` y `sensibilidad_flags_sbs.csv`, sin modificar el panel ni sobrescribir outputs existentes. Reproduce 5.635 filas fuente y 258 marcas `b` (111 `AV_MEUR`, 147 `EMP_NR`, todas 2021); 35 observaciones core (26 ambos componentes, 9 sólo empleo) reúnen 242 marcas en CZ/FI/FR/NL/PT/RO. M3 de adopción general retiene la muestra principal (667/233; β=−0,001263, p=.154); las exclusiones sólo de sensibilidad dan 632/232 (β=−0,001097, p=.234) y 565/198 (β=−0,001352, p=.174). Las marcas son rupturas, no errores automáticos; las comparaciones no son causales.

- [x] **T47 — Corregir la caracterización de Czarnitzki et al. (2023). Prioridad alta. Resuelta.** `trabajo_final.tex:259`, matriz bibliográfica y seminario. El artículo (JEBO 211, 188–205; DOI `10.1016/j.jebo.2023.05.008`) estudia 5.851 firmas alemanas (409 usuarias de IA), usa ventas/valor agregado como medidas de output y reporta asociaciones positivas en especificaciones con controles observados. Se eliminaron el rango +4–8% no delimitado y la atribución de una condición por personal calificado; se añadió el límite explícito de que analizar canales de competencias requiere datos laborales más detallados. Se mantiene lenguaje asociativo/no causal y el claim BIS/Aldasoro queda separado para T48. Build temporal con referencias resueltas e inspección visual sin defectos en tesina p. 13, matriz p. 2 y seminario p. 3. Commit `181a2fc99f3c5a1cd0a480771d6a72dfde8e3211`; revisión nativa consolidada diferida por decisión del usuario.

- [x] **T48 — Ajustar la afirmación atribuida a BIS Working Paper 1325. Prioridad alta. Resuelta.** `trabajo_final.tex:259,703`, matriz bibliográfica y seminario. El texto EIB WP 2026/02 (copublicación de BIS WP 1325; 40 pp.) reporta en la especificación con controles una estimación instrumentada de 0,041 (~4,1%) en facturación por empleado; los autores la interpretan causalmente bajo sus supuestos. Valor agregado por empleado es robustez. Tabla 6: interacciones positivas más fuertes con software/datos y capacitación, menor y positiva con edificios/infraestructura, no significativa para organización/procesos. Las prácticas de gestión son covariables del emparejamiento, no mecanismo demostrado. Se reescribieron las tres salidas para limitar evidencia a firmas 2019–2024 y no transferirla causalmente al panel sectorial. Build aislado con referencias resueltas; inspección de tesina pp. 13/31, matriz p. 1 y seminario p. 3, sin defectos en los pasajes. Commit `1a43d860c4309e8f0bbd548c3ac54b11f1e609fd`; sin revisión nativa por tarea, diferida al cierre por preferencia del usuario.

- [x] **T49 — Corregir el alcance atribuido a Kádárová et al. (2026). Prioridad media-alta. Resuelta.** `trabajo_final.tex:261` y matriz bibliográfica `:210-214`, DOI `10.3390/su18042135`. El texto completo no estuvo disponible (HTTP 403); la tesina y matriz ahora limitan la evidencia al resumen RePEc: Eurostat 2021–2024, comparación descriptiva Eslovaquia–UE-27, adopción eslovaca creciente pero bajo la media, productividad volátil y sin asociación agregada estable/inmediata. Se retiraron la generalización a los 27 países, la división Este–núcleo y la correlación Between positiva no respaldada; el contraste Between/Within se declara análisis propio del TFG. Build aislado con referencias resueltas e inspección visual/geométrica de tesina p. 13 y matriz p. 3, sin defectos. Commit `c798ebf521c387ce5ebebf848bdb66a76820a25b`; revisión nativa diferida al cierre por preferencia del usuario.

- [x] **T50 — Delimitar qué evidencia aporta el dataset Yilmaz (2026). Prioridad alta. Resuelta.** Se corrigieron `trabajo_final.tex`, `matriz_bibliografia_marco_teorico.tex` y `seminario_presentacion_metodologia.tex`, conservando la cita DOI `10.17632/gznvk45cfk.1`. Los tres materiales describen únicamente la evidencia verificable del dataset DataCite/Mendeley: Ekrem Yilmaz, 733 observaciones país--sector--año para UE-27, siete sectores, olas 2021/2023/2024/2025 y el `AI Attribution Wedge` como indicador descriptivo de *screening* que combina adopción, productividad posterior y horas trabajadas, explícitamente no causal. Se eliminó la atribución de un correlato contemporáneo y se declaró que selección/agregación de firmas de frontera y rezagadas son hipótesis no medidas, no hallazgos de Yilmaz. No se verificó un estudio acompañante independiente ni se usaron resultados SSRN no vinculados. Los builds aislados completaron (tesina 41 pp., matriz 7 pp. y seminario 7 pp.) y la extracción textual confirmó los pasajes. `git diff --check` informó whitespace en el PDF preexistente modificado `trabajo_final.pdf`; no se alteró ese PDF. Fuentes: `https://data.mendeley.com/datasets/gznvk45cfk/1`; `https://api.datacite.org/dois/10.17632/gznvk45cfk.1`.

- [ ] **T51 — Acotar lo que respaldan Bresnahan et al. y Acemoglu–Restrepo. Prioridad media-alta.** *Implementada en código (verificación diferida):* En `trabajo_final.tex:265` se delimitan estrictamente como marcos teóricos conceptuales de complementariedades IT y modelado por tareas, sin atribuirles evidencia empírica directa de IA.

- [ ] **T52 — Precisar el respaldo y el alcance de la afirmación sobre deflactores y efectos país–año. Prioridad alta.** *Implementada en código (verificación diferida):* En `trabajo_final.tex:255,725` se mantiene la productividad como nominal y se acota FWL a la absorción de inflación/shocks comunes nacionales, reconociendo que no absorbe precios relativos sectoriales.

- [ ] **T53 — Reformular como hipótesis la dirección y severidad del sesgo de selección en Pooled OLS. Prioridad media-alta.** *Implementada en código (verificación diferida):* En `trabajo_final.tex:281` se reformuló como vulnerabilidad teórica condicional por selección sin afirmar signo ni magnitud probados.

- [ ] **T54 — Acotar el uso de la curva J de productividad a la evidencia que ofrece. Prioridad media-alta.** *Implementada en código (verificación diferida):* En `trabajo_final.tex:673` se acota Brynjolfsson et al. (2021) como hipótesis interpretativa general compatible y no causa probada en este panel europeo.

- [ ] **T55 — No atribuir el resultado WLS a la composición sectorial/costos de reestructuración sin descomposición. Prioridad alta.** *Implementada en código (verificación diferida):* En `trabajo_final.tex:657` se define WLS estrictamente como cambio de estimando ponderado por empleo, retirando la atribución sectorial no descompuesta formalmente.

- [ ] **T56 — Sustentar o mantener como hipótesis los shocks sectoriales 2022–2023. Prioridad media.** *Implementada en código (verificación diferida):* En `trabajo_final.tex:681,725` se delimitan presiones energéticas/logísticas como hipótesis explicativas plausibles y no resultados medidos.

- [ ] **T57 — Citar evidencia para generalizaciones sobre motivaciones y capacidades empresariales. Prioridad media-alta.** *Implementada en código (verificación diferida):* En `trabajo_final.tex:711-713` se enmarcan SaaS genérico, consultoría y gobernanza como hipótesis y agenda de investigación microeconómica futura.

- [ ] **T58 — Distinguir implicancia de política de efecto demostrado. Prioridad media.** *Implementada en código (verificación diferida):* En `trabajo_final.tex:749` las recomendaciones se presentan como consideraciones tentativas derivadas de complementariedades, no como efectos estimados de M3.

- [ ] **T60 — Reconciliar la inferencia entre implementación manual y biblioteca canónica. Prioridad alta.** `outputs/modelos_panel_v0_1/modelo_preferido.csv:2` reporta para M3 β=−0,0012631, EE=0,0008844, p=0,1541; `modelo_preferido_manual.csv:2` da prácticamente el mismo β, pero EE=0,0012138 y p=0,2991. El script explica que los errores pueden diferir por correcciones de grados de libertad (`analysis/03_validacion_linearmodels.py:1–10`) y conserva el archivo manual como comparación antes de reemplazar el resultado canónico por `AbsorbingLS` (`:134–165`). El signo/coeficiente puntual no cambia, pero la diferencia de inferencia es material para el claim de conclusión. Documentar y justificar la corrección de covarianza/df que se adopta, validar la implementación contra una referencia apropiada para FE absorbidos y reportar de forma consistente la sensibilidad; no tratar el p=.154 como único resultado sin explicar la discrepancia.

### Verificaciones realizadas y límites

- `pdftotext`/`pdfinfo` locales permitieron confirmar que los PDFs concuerdan con el TeX en los valores principales revisados: adopción 9,2%→17,0%; r en niveles≈0,558; correlación de cambios≈−0,229; M3 β≈−0,0013, p≈0,154; WLS p≈0,032; prueba Mundlak/Wald≈69,10.
- Se reestimaron localmente M3 y variantes CRE/Mundlak y se documentaron los resultados en T27; esto no equivale a reejecutar o validar íntegramente todo el pipeline.
- Se realizó verificación externa parcial de fuentes originales/metadatos (entre otras, Czarnitzki et al. 2023, BIS WP 1325, Kádárová et al. 2026, dataset Yilmaz 2026, Bresnahan et al. 2002, Acemoglu–Restrepo 2018 y Brynjolfsson et al. 2021). Cada límite de acceso o afirmación pendiente está indicado en T47–T58; no se validó cada entrada bibliográfica ni cada cita del manuscrito.
- No se hizo inspección visual completa de diagramación ni compilación final. `pdftotext` puede omitir símbolos matemáticos; fórmulas y maquetación quedan pendientes. Tampoco se detectó discrepancia numérica entre presentación PDF y TeX en los claims revisados; sí se detectaron las formulaciones exageradas registradas en T22–T23.
- El hallazgo T19 es una ausencia en los scripts inspeccionados, no prueba definitiva de que el análisis nunca se haya ejecutado: buscar cualquier artefacto/código histórico antes de reconstruirlo.

## Resolución autoritativa posterior — T18 (prevalece sobre las descripciones históricas)

**Decisión del autor:** la proxy de productividad real SBS–Cuentas Nacionales queda retirada por completo del TFG activo. No puede figurar como resultado, robustez, evidencia, conclusión, análisis ni instrucción de reproducción, y no debe regenerarse. Esta resolución reemplaza cualquier formulación histórica de T18 que sólo ordenara excluirla de la inferencia o discutirla con cautela.

Se conservan sin eliminación `analysis/05_productividad_real_sectorial.py`, `data/processed/panel_analitico_productividad_real.csv` y `outputs/modelos_panel_v0_3/` únicamente como archivo histórico trazable, con señalización **ARCHIVADO — NO USAR**. El script 05 debe rechazar de forma segura cualquier ejecución. Las entradas anteriores de esta auditoría se mantienen como registro del hallazgo y de decisiones previas, no como recomendaciones vigentes.

**Criterio de cierre de T18:** no quedan referencias activas que inviten a ejecutar, interpretar, comparar, restaurar o incorporar la proxy; las menciones históricas se identifican inequívocamente como archivadas.

## Criterio de cierre



Antes de entregar, recompilar el PDF final, cotejar conclusiones contra tablas/CSV actualizados, revisar anexos y confirmar que no queden marcadores ni diferencias entre README, scripts, tablas y manuscrito.