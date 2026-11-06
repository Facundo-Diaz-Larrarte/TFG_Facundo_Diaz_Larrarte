# Reconciliar cierre del TFG

**Estado:** en curso  
**Alcance autorizado:** aplicar las decisiones confirmadas por el autor sobre artefactos activos, redacción, inferencia y defensa; preservar historial/insumos de productividad real sin incluirlos en resultados activos; verificar compilación y PDF finales contra fuentes. No realizar commit sin autorización expresa.

## Decisiones fijadas

- La productividad real aproximada queda fuera de todos los entregables y análisis activos. Sus artefactos históricos se preservan, etiquetados como archivados/no usar, sin borrar insumos originales.
- La designación oficial en los materiales de entrega es únicamente Miguel Bosch.
- Los contrastes sectoriales se mantienen como exploratorios; informar p sin ajustar y Holm, sin presentar sectores como efectos demostrados.
- El flujo reproducible activo debe ejecutar los pasos canónicos 01–04 y los análisis activos 06–08, comprobar las salidas y no regenerar la proxy real.
- Resolver T60 antes de fijar valores inferenciales en materiales de entrega.

## Tareas

1. **Definir inferencia canónica de T60.** Rastrear divergencia manual/AbsorbingLS, comparar covarianzas y correcciones finitas; seleccionar, documentar y propagar una convención defendible. Incluir pruebas/regresión reproducible.
2. **Retirar la proxy real del trabajo activo.** Quitarla de manuscrito, defensa, documentación operativa y documentos auxiliares; conservar los artefactos históricos fuera de uso, actualizar README y etiquetar drafts para que no parezcan productos válidos del TFG.
3. **Revisar claims y presentación sectorial.** Corregir afirmaciones absolutas de FE/precios y lenguaje de efecto cero; añadir ajuste Holm a las nueve pendientes y actualizar tabla, texto, presentación y guion como evidencia exploratoria.
4. **Reconciliar entregables y reproducción.** Fijar a Miguel Bosch en materiales activos; incluir scripts 06–08 en el runner/documentación canónicos con protecciones contra sobrescritura; verificar coherencia de nombres, cifras y fuentes.
5. **Compilar y cotejar PDFs finales.** Compilar en ubicación temporal, inspeccionar visualmente páginas relevantes, comparar texto/cifras/citas con TeX/CSV y actualizar registros de tareas con evidencia observada.

## Estado y evidencia

1. **T60 — completada en código, verificación focalizada pasada.** La matriz manual tenía 314 columnas y rango efectivo 288; su CR1 usaba 314. Se corrigió a CR1 con rango efectivo y referencia t con G−1 grados de libertad. `AbsorbingLS` queda como validación independiente de coeficientes/inferencia alternativa, ya no reemplaza la salida canónica. RED observado; 3 tests GREEN. Falta actualizar y regenerar salidas finales/documentación en tareas posteriores.
2. **Proxy real — completada en el alcance activo.** Script 05 bloqueado antes de red/archivos; READMEs, planes y registros indican archivo histórico/no usar; drafts de IA se etiquetaron archivados y ya no recomiendan reincorporarla. Outputs históricos preservados; no se borró nada.
3. Claims sectoriales/Holm: pendiente.
4. Reproducción/metadatos: pendiente.
5. PDFs/build final: pendiente.

## Evidencia y cierre

- No marcar una tarea verificada hasta observar sus pruebas/builds/artefactos.
- No reemplazar PDFs rastreados ni outputs existentes durante pruebas: usar directorios temporales; cualquier actualización final debe ser deliberada y confirmada.
- Commits quedan pendientes de autorización expresa del usuario.
