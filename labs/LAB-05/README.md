# LAB-05 — Monitoreo en verde, sensor ciego

**Dificultad:** Advanced · **Escenario:** NB-IR-2026-104 · **Autor:** Beacon of the Eagle LLC

## Objetivo
Diferencia disponibilidad del agente, tráfico realmente ingerido y cambios de SPAN. La infraestructura de Northbridge Systems, sus personas y sus datos son ficticios. Los analistas deben presentar inferencias apoyadas en evidencias, no suposiciones.

## Preparación
Trabaja con Python 3.10+ en Kali Linux, Ubuntu o Windows; sin instalación adicional ni acceso a Internet. En la raíz del paquete extraído:

```bash
python3 labs/runner.py start LAB-05 --output student_work
python3 tools/workbench.py inventory
python3 tools/workbench.py timeline --limit 25
```

En Windows, utiliza `py -3` si `python3` no existe. Para PCAP emplea `python3 tools/packet_inspector.py summary` y para fuentes CSV, `python3 tools/workbench.py inspect evidencia.csv` cambiando la ruta por un archivo real.

## Tres ejercicios verificables

### LAB-05-C1
**Problema:** Delimita el período de interrupción de captura con evidencias del switch y controlador.

**Fuentes obligatorias:**
- `evidence/05_network/span_counters.csv`
- `evidence/06_control_plane/controller_audit.csv`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.

### LAB-05-C2
**Problema:** Explica por qué un agente activo no acredita la recepción de paquetes.

**Fuentes obligatorias:**
- `evidence/08_soc/siem_health.csv`
- `evidence/05_network/span_counters.csv`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.

### LAB-05-C3
**Problema:** Investiga si el retraso de una alerta cambia la hora de inicio de la anomalía.

**Fuentes obligatorias:**
- `evidence/00_intake/soc_alerts.csv`
- `evidence/05_network/span_counters.csv`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.


## Evaluación
Edita `student_work/LAB-05/submission.json`; después:

```bash
python3 labs/runner.py validate LAB-05 --output student_work
```

El estado PASS valida únicamente **estructura y referencias**, no demuestra que la inferencia sea correcta. El examinador revisará fuentes, precisión, incertidumbre y recomendaciones operativas. Máximo interno: 12 puntos (4 por ejercicio).
