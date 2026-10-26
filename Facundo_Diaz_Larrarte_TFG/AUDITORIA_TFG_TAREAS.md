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

- [x] **T5 — Moderar la explicación causal de la correlación en niveles. Prioridad alta.** `trabajo_final.tex:1215`. El contraste r=0,558 frente a β≈−0,0013 (p=0,154) y el rechazo de efectos aleatorios son compatibles con heterogeneidad correlacionada, pero Hausman no demuestra que las diferencias permanentes expliquen toda la correlación. Cambiar “demuestra” por una formulación acotada a la evidencia y reconocer alternativas no identificadas.

- [x] **T6 — Separar resultados empíricos de mecanismos no medidos. Prioridad alta.** `trabajo_final.tex:1219`; limitaciones `:1191–1193`. El modelo no mide directamente capacitación, reorganización ni maduración, por lo que no permite afirmar que sean condiciones necesarias ni que la adopción sea insuficiente en general. Presentarlas como mecanismos teóricos plausibles, no como conclusión demostrada por estas estimaciones.

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

## Criterio de cierre

Antes de entregar, recompilar el PDF final, cotejar conclusiones contra tablas/CSV actualizados, revisar anexos y confirmar que no queden marcadores ni diferencias entre README, scripts, tablas y manuscrito.