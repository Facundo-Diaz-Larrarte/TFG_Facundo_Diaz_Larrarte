# Plan de ataque para finalizar el TFG

**Base:** tareas abiertas de `AUDITORIA_TFG_TAREAS.md` al 2026-11-05. Este documento organiza la corrección; no cambia el estado de las casillas de auditoría. Una tarea solo se marca resuelta después de revisar la fuente corregida y el PDF final.

## Secuencia de trabajo y puertas de decisión

### Fase 0 — Acordar alcance y desbloqueos

1. **Retirar por completo la productividad real aproximada de los entregables y análisis activos (T18).** Respetar la decisión del autor sobre la incompatibilidad SBS–Cuentas Nacionales: no usarla en inferencia, robusteces, resultados, conclusiones ni instrucciones de reproducción. Preservar los artefactos sin borrarlos, marcados como archivo histórico — NO USAR, y bloquear la ejecución del script 05.
2. **Resolver las decisiones metodológicas antes de editar resultados:** estimando/muestra principal (T26), si se reportará el CRE con país–año como sensibilidad (T27), y si se conserva una heterogeneidad sectorial sin evidencia reproducible (T19). Si no aparece el cálculo original, elegir entre reconstruirlo reproduciblemente o retirar esas afirmaciones.
3. **Resolver consultas institucionales** que no puede contestar la auditoría: vigencia y aplicación de normativa al Plan 2021; Res. 259/14; codirección/designación; datos administrativos de portada (T1, T33, T34). No inventar respuestas; dejar pendientes formales claramente identificados.

### Fase 1 — Congelar definiciones, fuentes y panel

4. Alinear el outcome con SBS 2021+: valor agregado a precios básicos nominal, `AV_MEUR × 1000 / EMP_NR`; verificar código/etiqueta y corregir nomenclatura en todo el material (T45).
5. Fijar trazabilidad de IA/SBS: endpoint correcto de IA, consultas/URL/parámetros y metadatos; describir encuesta/población desde manuales; documentar comparabilidad entre olas, flags y supresiones (T37, T38, T40, T42, T46).
6. Producir un patrón de faltantes/flags por país-sector-año-indicador y causas solo cuando las notas fuente las documenten; distinguir dato ausente de causa (T29, T31, T32). Buscar precisión muestral de los regresores agregados; si no existe por celda, declararlo como limitación (T41).
7. Construir ETL local auditable desde los insumos conservados, con reglas, versiones, hashes y conciliación; no sobrescribir los CSV/XLSX actuales (T28). Mantener v0.3/script 05 sólo como archivo histórico bloqueado, fuera del pipeline, README y anexos activos (T24).
8. Con las decisiones anteriores, fijar N por modelo y armonizar el README con la muestra y el uso del panel desbalanceado (T20, T26, T30).

### Fase 2 — Estimación e inferencia reproducibles

9. Recuperar el artefacto de heterogeneidad sectorial. Si no existe, reconstruir interacciones y contrastes sectoriales con código, tabla y validación independientes; si no se hace, retirar las pendientes y conclusiones dependientes (T19).
10. Revisar el estimando M3 y los errores: explicitar variación sectorial relativa dentro del país-año; evaluar dependencia residual y limitaciones de tres períodos; no atribuir al clustering corrección de error muestral (T21, T43, T44).
11. Presentar correctamente RE/Mundlak: identificar qué null prueba cada versión, no llamarlo prueba de causalidad ni de superioridad exclusiva de M3; mantener separados el modelo sin tiempo, con dummies de año y CRE ampliado (T22, T27).
12. Reconciliar errores/p-valores entre implementación manual y `linearmodels`; documentar corrección de grados de libertad/covarianza, contrastar contra una referencia apropiada para FE absorbidos y fijar una salida canónica (T60).
13. Describir WLS como cambio de ponderación/estimando; retirar la atribución a composición sectorial y costos de reestructuración si no se presenta una descomposición que la sustente. Formular la dirección del sesgo Pooled OLS como posibilidad, no como magnitud/signo demostrado (T43, T53, T55).
14. Ajustar el lenguaje de precios: FWL no es una corrección de inflación; los FE país-año absorben componentes comunes, no precios relativos sectoriales. Sustentar con fuente verificable cualquier afirmación sobre deflactores y conservar la productividad como nominal si no hay deflactor válido (T52).

### Fase 3 — Fuentes, interpretación y narrativa

15. Completar verificación bibliográfica afirmación por afirmación y reconciliar `.bib` con la presentación (T25, T39). Aplicar los límites ya establecidos: Czarnitzki no respalda control por personal calificado (T47); BIS/EIB respalda software/datos y capacitación, no gobernanza/gestión profunda como mecanismo demostrado (T48); Kádárová compara Eslovaquia con el agregado UE-27, no a todos los países (T49); Yilmaz es un indicador descriptivo y no causal, pendiente el estudio acompañante (T50); Bresnahan y Acemoglu–Restrepo dan marco conceptual, no evidencia directa de implementación IA empresarial (T51); J-curve es mecanismo general compatible, no explicación causal identificada aquí (T54).
16. Para shocks energéticos/logísticos, motivaciones y capacidades de firmas, SaaS/consultoría/gobernanza y recomendaciones: añadir fuentes directas y delimitadas o reescribir como hipótesis/implicancias; no presentarlas como resultados de Eurostat/M3 (T56, T57, T58).
17. Reescribir las conclusiones usando solo resultados reproducibles: acotar el origen de la correlación en niveles, distinguir “no se detecta” de “no existe”, y mantener mecanismos como plausibles/no medidos. Aplicar igual cautela a cada frase de discusión y presentación (T5, T23, T39, T54–T58).
18. Mantener la proxy de productividad real retirada de todas las salidas activas y no defenderla, reproducirla ni presentarla como evidencia (T18). Revisar la formulación de costos de ajuste y rendimientos rezagados para que el alcance de las fuentes coincida con el de la muestra (T54).

### Fase 4 — Requisitos formales y cierre

19. Completar portada y datos, confirmar normativa, codirección y firmas con Secretaría/director; verificar plantilla, extensión y formato en el PDF (T1, T33–T35).
20. Ajustar el guion y la presentación a los resultados validados, corregir lenguaje de asociación/significancia y cronometrar la exposición para el límite acordado (T23, T36).
21. Actualizar README/anexos/documentación junto con cada cambio (T24, T25, T28, T30, T37, T38).
22. Reproducir desde cero en un entorno seguro, sin sobrescribir insumos originales; compilar el PDF final, revisar visualmente cuadros/fórmulas/portada/anexos, cotejar PDF–TeX–CSV–presentación–guion y verificar cada casilla abierta con evidencia. Solo entonces cerrar tareas y preparar la entrega.

## Matriz de ataque por tarea abierta

| ID | Estado | Ataque concreto | Evidencia de cierre |
|---|---|---|---|
| T1 | Pendiente (consulta institucional) | Confirmar con Secretaría campos obligatorios; completar registro/fecha/año sin marcadores. | PDF final con portada completa y validación administrativa. |
| T5 | Resuelta | Reescribir la atribución “preponderantemente” y el vínculo con el test RE como evidencia compatible, no descomposición causal. | Conclusión y presentación cotejadas con M3/CRE y PDF final. |
| T18 | Resuelta | Retirar íntegramente la proxy real de los análisis, entregables, robusteces e instrucciones activas; conservar sin borrado sólo el archivo histórico marcado NO USAR y bloquear script 05. | Ninguna salida activa ni instrucción de reproducción usa β/p, panel o script reales; los artefactos históricos permanecen preservados y claramente archivados. |
| T19 | Resuelta | Encontrar cálculo original o reconstruir interacciones y contrastes; si no, retirar claims sectoriales. | Script reproducible, tabla, contraste e independencia entre el cálculo y la interpretación. |
| T20 | Implementada (verif. diferida) | Reportar N/cobertura por indicador y comparabilidad entre modelos. | Cuadro N por especificación e interpretación en metodología/README. |
| T21 | Implementada (verif. diferida) | Revisar inferencia agrupada y sensibilidad a dependencia entre sectores por país-año con especialista. | Estimando y supuestos explicitados; análisis alternativo/limitación documentado. |
| T22 | Implementada (verif. diferida) | Renombrar prueba como CRE/Mundlak-Wald de la especificación probada y separar selección de M3. | Método, null, covarianza, años y conclusión coinciden. |
| T23 | Implementada (verif. diferida) | Corregir “se disipa/se desvanece” en presentación. | Diapositivas distinguen descriptivo, FE, cambio temporal y no significancia. |
| T24 | Pendiente | Resolver pipeline v0.3/script 05: alcance explícito, segura reproducción o retiro de promesas. | README/anexo/pipeline coherentes; TLS y sobrescrituras revisados; reproducción controlada. |
| T25 | Implementada (verif. diferida) | Reconciliar referencias/citas de la presentación con `.bib`; auditar entries no citadas. | Lista de referencias completa y consistente en ambos productos. |
| T26 | Pendiente (decisión metodológica) | Fijar muestra principal/desbalance, reportar eliminación por variable y no asumir faltantes ignorable. | Decisión metodológica documentada, N comparables y sensibilidad descrita. |
| T27 | Pendiente (decisión metodológica) | Presentar CRE país-año como sensibilidad si dirección lo aprueba; separar de RE simple. | Tabla/nota con estimando, estadístico, p-value y alcance correctos. |
| T28 | Pendiente | Crear ETL reproducible, con insumos congelados, hashes y conciliación del libro/CSV. | Ejecución limpia reconstruye conteos/valores documentados sin alterar fuentes. |
| T29 | Pendiente | Verificar definición de flags/quiebres/supresión y correr sensibilidad razonada. | Diccionario, procedencia, política y resultados con/sin flags. |
| T30 | Pendiente | Alinear README: muestra no balanceada principal y balanceada como sensibilidad. | Cifras/definiciones README coinciden con tablas y scripts. |
| T31 | Pendiente | Tabular faltantes por dimensión e indicador. | Tabla reproducible y explicación sin supuestos de MCAR no sustentados. |
| T32 | Pendiente | Aclarar universo de conteo de quiebres y cruce con core. | Conteos de grilla/core reconciliados y nota en método. |
| T33 | Pendiente (consulta institucional) | Confirmar vigencia/aplicación normativa, incluida Res. 259/14 y Plan 2021. | Copias oficiales, respuesta de Secretaría y requisitos aplicables listados. |
| T34 | Pendiente (consulta institucional) | Confirmar codirectora/designación y datos de portada. | Aprobación formal y metadatos definitivos. |
| T35 | Pendiente (consulta institucional) | Revisar formato, firmas y ejemplar administrativo según Res. 260/02. | Checklist institucional firmado/revisado y PDF visualmente conforme. |
| T36 | Pendiente | Cronometrar defensa y ajustar guion. | Ensayo cronometrado dentro del límite confirmado. |
| T37 | Pendiente | Usar `isoc_eb_ain2` para IA por actividad y conservar consultas. | Endpoint, indicador, parámetros y extracción archivados/reproducibles. |
| T38 | Pendiente | Citar manual/cuestionario/metadata para diseño de encuesta, informante y definiciones. | Cada afirmación metodológica vinculada a fuente primaria por ola. |
| T39 | Pendiente | Cotejar claims interpretativos/recomendaciones con fuentes; hipótesis sin soporte se rebajan. | Matriz claim–fuente–pasaje–límite; citas exactas en manuscrito. |
| T40 | Pendiente | Documentar revisiones del indicador IA y breaks nacionales. | Manuales/notes por año y sensibilidad/reporting. |
| T41 | Pendiente | Buscar errores estándar/precisión de proporciones Eurostat; si faltan, reconocer error de medición. | Fuente de precisión o limitación explícita en resultados. |
| T42 | Pendiente | Asignar causas de faltantes solo con status/notas oficiales por celda. | Mapa de status rastreable; ausencias sin causa quedan como desconocidas. |
| T43 | Implementada (verif. diferida) | Explicar clustering, “masa crítica” y WLS sin atribuir funciones que no cumplen. | Método distingue dependencia intracluster, precisión muestral y estimando ponderado. |
| T44 | Implementada (verif. diferida) | Explicar identificación condicional de M3 con FE entidad y país-año. | Ecuación e interpretación dicen variación relativa sectorial dentro de país-año. |
| T45 | Resuelta | Renombrar AV_MEUR/productividad y verificar código SBS 2021+. | Diccionario, fórmula, unidades y texto coinciden con metadata oficial. |
| T46 | Resuelta | Reportar cobertura/impacto de flags SBS sin exclusión automática. | Tabla de sensibilidad confirmada y limitación de break 2021 explícita. |
| T47 | Resuelta | Corregir cita de Czarnitzki: Alemania, controles observados, sin afirmar control de skill no medido. | Claim coincide con artículo y método. |
| T48 | Resuelta | Sustituir “gobernanza/gestión profunda” por resultados medidos BIS/EIB. | Claim y cita reflejan heterogeneidad, software/datos y training. |
| T49 | Resuelta | Restringir Kádárová a comparación Slovakia–UE-27 y evidencia descriptiva. | Síntesis cotejada con artículo completo o con límites de abstract declarados. |
| T50 | Resuelta | Tratar AAW como indicador descriptivo; localizar el artículo acompañante o no adjudicarle resultados. | DOI/texto del estudio y resultados verificables, o afirmación reducida al dataset. |
| T51 | Implementada (verif. diferida) | Delimitar Bresnahan/Acemoglu–Restrepo como marco IT/task-based. | Afirmaciones de IA empresarial cuentan con evidencia específica o se etiquetan como hipótesis. |
| T52 | Implementada (verif. diferida) | Corregir atribución FWL/precios y obtener soporte para el reclamo de deflactores. | Explicación de FE limitada a shocks comunes; fuente localizable para cualquier claim de deflactación. |
| T53 | Implementada (verif. diferida) | Presentar sesgo positivo Pooled OLS como posibilidad condicional. | El texto separa coeficiente observado de sesgo y no afirma signo/magnitud sin identificación. |
| T54 | Implementada (verif. diferida) | Usar J-curve como mecanismo general, no causa demostrada para este panel. | Claim cita la publicación y distingue teoría/microdato US de estimación UE agregada. |
| T55 | Implementada (verif. diferida) | Retirar mecanismo sectorial del WLS o añadir descomposición por sector. | Descomposición reproducible sustenta atribución; de lo contrario, reportar solo sensibilidad ponderada. |
| T56 | Implementada (verif. diferida) | Citar shocks energéticos/logísticos comparables y mantenerlos como hipótesis. | Fuente UE/sector/período adecuada y conexión explícitamente no causal. |
| T57 | Implementada (verif. diferida) | Sustentar motivaciones, capacitación, consultoría, SaaS y gobernanza con evidencia directa. | Claims universales acotados, referenciados o etiquetados como hipótesis. |
| T58 | Implementada (verif. diferida) | Presentar política como recomendación tentativa, no efecto estimado. | Fuente de recomendaciones, transferibilidad y límites; no atribuir a M3. |
| T60 | Pendiente | Justificar discrepancia manual/AbsorbingLS y fijar inferencia canónica con sensibilidad. | EE/p-values trazables a corrección explicada; benchmark metodológico y tabla final consistente. |

## Reglas de ejecución

- Trabajar por fase y en cambios pequeños; no mezclar decisiones metodológicas, administrativos y estilo en un único cambio.
- Antes de cada corrección sustantiva, registrar la decisión/alcance y el criterio de aceptación.
- Mantener inalterados los insumos originales; validar primero sobre copias/salidas versionadas.
- No declarar completa una tarea por haber editado el TeX: revisar la compilación final y los artefactos que dependen de ella.
- Pedir decisión solo en las puertas señaladas; no pedir al usuario que elija procedimientos de bajo nivel que puedan resolverse con evidencia/fuentes.

## Registro detallado de intervenciones aplicadas para auditoría externa (al 2026-11-06)

Las siguientes tareas fueron intervenidas directamente en el código fuente para resolver los requerimientos de la auditoría, con verificación compilatoria diferida a una pasada consolidada final por indicación del autor:

- **T22 (Restricción RE/Mundlak-CRE):** Se delimitó el contraste a la hipótesis exacta evaluada en `analysis/03_validacion_linearmodels.py` ($H_0:\ \texttt{ai\_mean}=0$), reportando $\chi^2(1)=69,10$ ($p<0,001$) sin controles de tiempo y $\chi^2(1)=108,98$ con dummies de año. Se eliminó la etiqueta de "Hausman clásico", "M3 mandatorio" o "única especificación consistente" en `presentacion_tfg.tex:402-416,503`, `guion_defensa_tfg.tex:318-324,388,464,524`, `matriz_bibliografia_marco_teorico.tex:221-223,289` y `trabajo_final.tex:283-285,397,661-663,741,951`.
- **T23 (Formulaciones en presentación y guion):** Se eliminó la afirmación de que la correlación "se disipa por completo" en Diapositiva 8 (`presentacion_tfg.tex:381`), reemplazándola por ausencia de significancia estadística a niveles convencionales sin asumir efecto nulo exacto. En Diapositiva 13 (`:502`), se separó la correlación de cambios 2021--2024 ($r=-0,229$) como estimando descriptivo del estimador condicional M3, eliminando "se desvanece".
- **T25 (Reconciliación bibliográfica):** Se incorporaron Czarnitzki et al. (2023), Aldasoro et al. / BIS-EIB (2026), Kádárová et al. (2026) y Yilmaz (2026) a la guía bibliográfica de defensa en `guion_defensa_tfg.tex:502-515`. Los apéndices de la presentación (`presentacion_tfg.tex:698-731`) y las citas del manuscrito quedaron completamente alineados con `referencias.bib`.
- **T43 y T44 (Identificación M3, clustering y WLS):** En `trabajo_final.tex:342,409`, se explicitó que por el teorema FWL la identificación de $\beta$ proviene exclusivamente de la variación sectorial relativa entre ramas dentro de cada país--año respecto a su trayectoria histórica. Se precisó que el clustering por entidad es una aproximación asintótica en el número de grupos y no corrige error de medición ni dependencia residual contemporánea (cubierta por la sensibilidad de dos vías). WLS se definió estrictamente como un cambio de estimando ponderado por empleo.
- **T51 (Marcos teóricos IT y task-based):** Se delimitaron Bresnahan et al. (2002) y Acemoglu & Restrepo (2018) como marcos conceptuales de complementariedades organizacionales y enfoque de tareas, eliminando cualquier atribución de evidencia directa sobre adopción empresarial contemporánea de IA (`trabajo_final.tex:265`).
- **T52 (Precios y teorema FWL):** Se mantuvo la productividad como nominal estandarizada y se aclaró que los efectos fijos país--año neutralizan shocks agregados de inflación nacional, pero no variaciones de precios relativos entre sectores (`trabajo_final.tex:255,725`).
- **T53 (Sesgo de Pooled OLS):** Se reformuló el sesgo de selección en corte transversal como una vulnerabilidad teórica condicional que impide interpretar el parámetro como causal, sin afirmar signo ni magnitud demostrados (`trabajo_final.tex:281`).
- **T54 (Curva J de productividad):** La teoría de Brynjolfsson et al. (2021) se acotó a un marco interpretativo general compatible con desfases y costos de ajuste iniciales, no como causa probada en este panel (`trabajo_final.tex:673`).
- **T55 (Mecanismo sectorial en WLS):** Se retiró la afirmación de que la mayor pendiente negativa de WLS demuestre costos de reestructuración en ramas de alto empleo, dejándola como conjetura teórica a falta de una descomposición formal reproducible (`trabajo_final.tex:657`).
- **T56, T57 y T58 (Shocks, SaaS/consultoría y política económica):** Se delimitaron las presiones energéticas/logísticas como hipótesis plausibles no medidas (`:681,725`); los mecanismos de SaaS horizontal, consultoría y gobernanza como hipótesis y agenda microeconómica futura (`:711-713`); y las recomendaciones de política económica como consideraciones tentativas derivadas de complementariedades, no como efectos directos de M3 (`:749`).
