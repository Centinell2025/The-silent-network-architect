# LAB-14 — Simulacro de crisis SOC y comunicación

**Dificultad:** Expert+ · **Escenario:** NB-IR-2026-104 · **Autor:** Beacon of the Eagle LLC

## Objetivo
Coordina una respuesta blue-team con decisiones justificadas sin atribuir un actor inexistente. La infraestructura de Northbridge Systems, sus personas y sus datos son ficticios. Los analistas deben presentar inferencias apoyadas en evidencias, no suposiciones.

## Preparación
Trabaja con Python 3.10+ en Kali Linux, Ubuntu o Windows; sin instalación adicional ni acceso a Internet. En la raíz del paquete extraído:

```bash
python3 labs/runner.py start LAB-14 --output student_work
python3 tools/workbench.py inventory
python3 tools/workbench.py timeline --limit 25
```

En Windows, utiliza `py -3` si `python3` no existe. Para PCAP emplea `python3 tools/packet_inspector.py summary` y para fuentes CSV, `python3 tools/workbench.py inspect evidencia.csv` cambiando la ruta por un archivo real.

## Tres ejercicios verificables

### LAB-14-C1
**Problema:** Determina cuándo escalar una alerta con información incompleta.

**Fuentes obligatorias:**
- `evidence/00_intake/soc_alerts.csv`
- `evidence/03_identity/privileged_access.csv`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.

### LAB-14-C2
**Problema:** Propón un plan de preservación de accesos, tareas y eventos volátiles.

**Fuentes obligatorias:**
- `evidence/04_endpoint/scheduled_tasks.csv`
- `evidence/03_identity/windows_security.csv`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.

### LAB-14-C3
**Problema:** Prepara una recomendación de recuperación que no destruya las huellas de la exportación.

**Fuentes obligatorias:**
- `evidence/07_receipts/receiving_object_audit.csv`
- `evidence/06_control_plane/config_snapshots.csv`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.


## Evaluación
Edita `student_work/LAB-14/submission.json`; después:

```bash
python3 labs/runner.py validate LAB-14 --output student_work
```

El estado PASS valida únicamente **estructura y referencias**, no demuestra que la inferencia sea correcta. El examinador revisará fuentes, precisión, incertidumbre y recomendaciones operativas. Máximo interno: 12 puntos (4 por ejercicio).
