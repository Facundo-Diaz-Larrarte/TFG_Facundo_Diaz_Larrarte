# Reestructurar presentación para defensa oral del TFG

## Objetivo
Convertir `presentacion_tfg.tex` en una defensa oral académica, breve y orientada a los resultados económicos del `trabajo_final.tex`, sin inventar ni alterar hallazgos. La presentación principal tendrá aproximadamente 14 diapositivas —incluyendo portada y Gracias/Preguntas— y el material extenso se desplazará al apéndice posterior.

## Alcance autorizado
- `Facundo_Diaz_Larrarte_TFG/presentacion_tfg.tex`
- `odd/tasks/revisar-presentacion-tfg.md`

**Fuera de alcance:** `trabajo_final.tex`, resultados, bases, scripts, bibliografía y archivos generados.

## Requisitos innegociables
- Al comienzo, conservar formulaciones fieles de pregunta central, objetivo general y hipótesis central; aclarar el carácter asociativo/no causal.
- Diseño principal: UE-27; 9 sectores; 2021, 2023 y 2024; 627 observaciones de 209 entidades; unidad país–sector–año.
- Diferenciar de forma visual y conceptual comparación entre unidades (*between*) y variación dentro de país–sector (*within*).
- Conservar valores: adopción 9,2% → 10,0% → 17,2%; correlación en niveles r=+0,564; correlación en cambios r=−0,217; M3 nominal β=−0,0011, p=0,250; robustez real aproximada β=+0,0019, p=0,036.
- Heterogeneidad sectorial explícitamente exploratoria; no afirmar que IA reduzca productividad ni causalidad.
- Mantener limitaciones y conclusiones vinculadas con pregunta, objetivo e hipótesis, incluyendo activos complementarios.
- Eliminar del cuerpo principal referencias a GitHub, repositorios, scripts, códigos internos, pipelines y reproducibilidad innecesaria.
- Poner Gracias/Preguntas antes del apéndice; mover bibliografía completa, detalles metodológicos y resultados secundarios al apéndice.

## Criterios de aceptación
- [x] Deck principal de 14 diapositivas: portada; planteo; diseño; marco económico; between/within; descriptivo; contraste; M3 nominal; nominal/real; heterogeneidad; interpretación; límites; conclusiones; Gracias/Preguntas.
- [x] Apéndice después de Gracias con bibliografía completa y detalle útil para preguntas.
- [x] Contenido fiel a `trabajo_final.tex`, sin nuevos resultados ni inferencias causales.
- [x] `latexmk` compila en directorio temporal externo y la revisión visual no detecta superposiciones, recortes ni texto ilegible.

## Plan y progreso
- [x] T1 — Mapear tesis completa, presentación vigente y narrativa de defensa. Evidencia: `gentle-ai-explore` `mutzg09v-h-x569`.
- [x] T2 — Reestructurar y sintetizar la presentación, conservando estilo visual y resultados exactos. Evidencia: `gentle-ai-worker` `mutzjiho-i-ymoi`; deck principal de 14 diapositivas, apéndice posterior y bibliografía completa.
- [x] T3 — Compilar y realizar auditoría visual independiente del PDF. Evidencia: `gentle-ai-verify` `mutzzjin-k-kq9t`; PDF de 23 páginas, 14 de defensa y 9 de apéndice, compilación final limpia y rasterización completa a 150 DPI sin solapamientos ni recortes. La métrica de años se compactó como «3 olas: 2021 · 2023 · 2024».

## Estrategia de entrega
- Estrategia: `single-pr` (cambio coherente en un solo documento).
- TDD: no aplicable; comprobación mediante compilación y lectura visual.

## Resultado
Presentación lista para defensa: narrativa económica jerarquizada, resultados fieles y cautela inferencial explícita.