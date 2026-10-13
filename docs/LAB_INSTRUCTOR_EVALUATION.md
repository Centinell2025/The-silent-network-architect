# Examinador — revisión de 14 laboratorios

**Autoría:** Beacon of the Eagle LLC / Centinell Suite Defense. Los laboratorios contienen únicamente evidencias ficticias.

## Matriz de evaluación
Por cada uno de los **42 checkpoints**, asignar 0–4 puntos:

- **0:** sin respuesta o sin fuente.
- **1:** conjetura sin justificación reproducible.
- **2:** una observación acertada con referencias parciales.
- **3:** correlación correcta entre fuentes, control de tiempo y explicación alternativa.
- **4:** análisis reproducible, incertidumbre y consecuencia operacional explícitas.

**Puntuación interna máxima:** 168 puntos. No constituye calificación oficial de Hack The Box.

Un PASS de `labs/runner.py validate` certifica **solo la estructura** y la presencia de citas en los archivos, nunca la exactitud del razonamiento.

## Revisión avanzada LAB-13 y LAB-14

**LAB-13:** exigir un cálculo documentado de relojes, observabilidad y límites de una aprobación. Penalizar atribuciones humanas infundadas, asumir que dos modelos sintéticos son adquisiciones independientes o declarar un cero de paquetes como prueba definitiva del mecanismo de intrusión.

**LAB-14:** exigir decisiones de escalamiento con umbral y justificación, preservación antes de cambios irreversibles y coordinación del SOC. Penalizar acciones que modifiquen evidencias antes de calcular hashes, ignorar continuidad operativa o confundir un recibo sintético con prueba de daño real.

## Lista de revisión humana
Verificar personalmente las fuentes citadas, los registros, los cálculos, falsos positivos, recomendaciones, limitaciones e idoneidad para dificultad avanzada. Realizar al menos dos investigaciones a ciegas antes de afirmar nivel Insane. Mantener las soluciones del instructor fuera del repositorio público y del ZIP para alumnos.
