# LAB-10 — Persistencia y restauración

**Dificultad:** Expert · **Escenario:** NB-IR-2026-104 · **Autor:** Beacon of the Eagle LLC

## Objetivo
Evalúa si restaurar reglas de red basta para cerrar el incidente. La infraestructura de Northbridge Systems, sus personas y sus datos son ficticios. Los analistas deben presentar inferencias apoyadas en evidencias, no suposiciones.

## Preparación
Trabaja con Python 3.10+ en Kali Linux, Ubuntu o Windows; sin instalación adicional ni acceso a Internet. En la raíz del paquete extraído:

```bash
python3 labs/runner.py start LAB-10 --output student_work
python3 tools/workbench.py inventory
python3 tools/workbench.py timeline --limit 25
```

En Windows, utiliza `py -3` si `python3` no existe. Para PCAP emplea `python3 tools/packet_inspector.py summary` y para fuentes CSV, `python3 tools/workbench.py inspect evidencia.csv` cambiando la ruta por un archivo real.

## Tres ejercicios verificables

### LAB-10-C1
**Problema:** Reconstruye la creación y ejecución de una tarea programada.

**Fuentes obligatorias:**
- `evidence/04_endpoint/scheduled_tasks.csv`
- `evidence/03_identity/windows_security.csv`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.

### LAB-10-C2
**Problema:** Contrasta una tarea bajo SYSTEM con la evidencia de procesos.

**Fuentes obligatorias:**
- `evidence/04_endpoint/scheduled_tasks.csv`
- `evidence/04_endpoint/process_activity.csv`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.

### LAB-10-C3
**Problema:** Explica qué exposición continúa después de restaurar la configuración de red.

**Fuentes obligatorias:**
- `evidence/06_control_plane/config_snapshots.csv`
- `evidence/04_endpoint/scheduled_tasks.csv`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.


## Evaluación
Edita `student_work/LAB-10/submission.json`; después:

```bash
python3 labs/runner.py validate LAB-10 --output student_work
```

El estado PASS valida únicamente **estructura y referencias**, no demuestra que la inferencia sea correcta. El examinador revisará fuentes, precisión, incertidumbre y recomendaciones operativas. Máximo interno: 12 puntos (4 por ejercicio).
