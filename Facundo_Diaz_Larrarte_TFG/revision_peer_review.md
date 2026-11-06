# ARCHIVADO — borrador de trabajo de peer review generado por IA

**Estado:** archivado; no es una revisión aceptada ni una conclusión editorial, metodológica o de investigación.  
**Documento evaluado:** *Usos empresariales de inteligencia artificial y productividad laboral: evidencia país--sector para la Unión Europea*  
**Autor:** Facundo Díaz Larrarte  
**Reviewer name:** Draft Detective — Reviewer 2  
**Nota:** borrador generado por un sistema de IA para discusión histórica. No debe usarse para decisiones editoriales, académicas o de investigación sin evaluación humana independiente. La decisión posterior del autor retiró completamente la proxy de productividad real SBS–Cuentas Nacionales del TFG activo; este borrador no recomienda restaurarla ni usar sus artefactos archivados.

## SECTION 1: SUMMARY OF ARGUMENT AND SUPPORTING EVIDENCE

El trabajo estudia la asociación entre adopción y usos empresariales de inteligencia artificial (IA) y productividad laboral aparente en 27 países y nueve sectores de la Unión Europea, para 2021, 2023 y 2024. Construye un panel país--sector--año con fuentes de Eurostat y distingue entre la correlación transversal —positiva— y la asociación temporal dentro de cada unidad, estimada mediante efectos fijos de país--sector y país--año. La conclusión central es que la adopción declarada no se asocia con un aumento contemporáneo estadísticamente detectable de la productividad en la ventana observada; el diseño se presenta como observacional y asociativo, no causal.

La evidencia más sólida es el contraste entre la correlación positiva en niveles (r = 0,558) y la estimación FE principal para adopción general (β = −0,0013 por punto porcentual; p = 0,154; n = 667), junto con estimaciones alternativas de panel y una implementación de validación independiente. El manuscrito reconoce límites de medición, causalidad inversa, heterogeneidad no observada y panel corto.

## SECTION 2: STRENGTHS

El trabajo delimita con claridad su unidad de análisis, período y cobertura, y no confunde productividad laboral aparente con productividad total de los factores. La advertencia de que los datos agregados no identifican decisiones o resultados de empresas individuales es metodológicamente importante. También es una fortaleza distinguir asociación transversal de variación intraunidad: el contraste entre r = 0,558 y el coeficiente FE evita atribuir a la adopción el patrón de niveles entre países y sectores.

La estrategia empírica es transparente en sus elementos centrales: se informa la estructura del panel, los efectos fijos, los errores agrupados y las sensibilidades de muestra/especificación. La discusión de capacidades complementarias y rezagos ofrece mecanismos plausibles, y el propio texto reconoce que no identifica la curva J ni demuestra causalmente esos mecanismos. La base reproducible y la documentación de sus fuentes son activos que conviene preservar y alinear mejor con cada cifra publicada.

## SECTION 3: WEAKNESSES

**La reproducibilidad requiere comprobar que las tablas finales, el README y la salida vigente refieran a los mismos datos y especificaciones nominales canónicas.** `analysis/00_reproducir_todo.py` ejecuta los scripts activos 01–04 y verifica los productos nominales correspondientes. Los artefactos v0.3 retirados no forman parte de esta ruta ni deben regenerarse.

**Algunas expresiones son más concluyentes que el diseño.** En las conclusiones, el contraste de Hausman/Mundlak se presenta como corroboración de que la asociación transversal está condicionada por diferencias estructurales permanentes. El rechazo de la restricción de efectos aleatorios respalda que la heterogeneidad individual está correlacionada con los regresores y debilita RE bajo sus supuestos; no identifica por sí mismo qué diferencias explican la correlación transversal ni demuestra el mecanismo. Del mismo modo, un p-valor no significativo no prueba ausencia de asociación, y las explicaciones de costos de ajuste, activos complementarios o brecha de realización deben quedar expresamente como interpretaciones compatibles, no como mecanismos verificados.

**La inferencia sectorial y la multiplicidad necesitan más protagonismo.** Con tres olas temporales, las pendientes sectoriales descansan en variación temporal limitada. El documento las denomina exploratorias, pero las conclusiones narrativas sobre manufactura, comercio y servicios informáticos pueden leerse como resultados firmes. Debe precisarse cuántas comparaciones se hicieron, si hubo ajuste por multiplicidad y qué resultados son descriptivos frente a confirmatorios.

## SECTION 4: ACTIONABLE NEXT STEPS

### Recomendación 1 — Cerrar la brecha de reproducibilidad

| Elemento | Acción |
|---|---|
| Problema central | Las tablas, el README y las salidas nominales canónicas deben mantenerse alineados. |
| Pasos recomendados | Comprobar las salidas activas contra un entorno limpio y registrar versión de datos, muestra y especificación nominal. |
| Tradeoffs o riesgos | La verificación puede requerir tiempo, pero evita que una discrepancia menor debilite la confianza en el flujo empírico activo. |

### Recomendación 2 — Moderar la fuerza de las conclusiones econométricas

| Elemento | Acción |
|---|---|
| Problema central | El test de Hausman/Mundlak y la no significatividad se interpretan, por momentos, como pruebas de mecanismos o de ausencia de relación. |
| Pasos recomendados | Diferenciar evidencia, interpretación y mecanismo; describir Hausman como prueba sobre la restricción RE; reemplazar «demuestra» por lenguaje condicional donde corresponda y declarar explícitamente que p = 0,154 no prueba un efecto nulo. |
| Tradeoffs o riesgos | La prosa será menos categórica, pero reflejará fielmente qué identifican los datos y reducirá objeciones previsibles en la defensa. |

### Recomendación 3 — Delimitar la evidencia sectorial exploratoria

| Elemento | Acción |
|---|---|
| Problema central | Varias pendientes por sector se interpretan con panel de solo tres olas y múltiples comparaciones. |
| Pasos recomendados | Mantenerlas como exploratorias, informar el número de pruebas, mostrar incertidumbre y aclarar si se ajustó por multiplicidad; trasladar afirmaciones de mecanismo a hipótesis futuras. |
| Tradeoffs o riesgos | Un ajuste por multiplicidad puede reducir significación; esa menor contundencia es preferible a una lectura de confirmación que el diseño no sostiene. |

### Recomendación 4 — Conciliar las cifras descriptivas entre manuscrito y artefactos

| Elemento | Acción |
|---|---|
| Problema central | El análisis previo detectó divergencias entre promedios de 2024 reportados en la tesis y documentación de análisis. |
| Pasos recomendados | Recalcular cada promedio desde la salida canónica; registrar denominador, ponderación, unidad y versión de datos; corregir texto, tablas y README desde esa única fuente. |
| Tradeoffs o riesgos | Puede requerir regenerar algunas tablas y figuras, pero evita que una discrepancia menor debilite la confianza en todo el flujo empírico. |

Como agenda futura, el paso más útil es extender el panel con nuevas olas comparables y enlazar, si es posible, datos de adopción e intensidad de uso con medidas de productividad más cercanas a empresas. Un horizonte mayor permitiría estudiar rezagos sin presentar la curva J como ya comprobada; diseños cuasiexperimentales o microdatos longitudinales serían necesarios para avanzar de asociaciones agregadas a inferencias causales.

**Alcance de esta revisión:** evaluación local del manuscrito y los artefactos presentes en el repositorio. No se ejecutaron búsquedas externas ni validaciones bibliográficas web.
