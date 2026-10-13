# LAB-02 — Cambios de red bajo sospecha

**Dificultad:** Intermediate · **Escenario:** NB-IR-2026-104 · **Autor:** Beacon of the Eagle LLC

## Objetivo
Determina si el cambio de red respetó el activo, la acción y el alcance de una autorización. La infraestructura de Northbridge Systems, sus personas y sus datos son ficticios. Los analistas deben presentar inferencias apoyadas en evidencias, no suposiciones.

## Preparación
Trabaja con Python 3.10+ en Kali Linux, Ubuntu o Windows; sin instalación adicional ni acceso a Internet. En la raíz del paquete extraído:

```bash
python3 labs/runner.py start LAB-02 --output student_work
python3 tools/workbench.py inventory
python3 tools/workbench.py timeline --limit 25
```

En Windows, utiliza `py -3` si `python3` no existe. Para PCAP emplea `python3 tools/packet_inspector.py summary` y para fuentes CSV, `python3 tools/workbench.py inspect evidencia.csv` cambiando la ruta por un archivo real.

## Tres ejercicios verificables

### LAB-02-C1
**Problema:** Confronta el alcance autorizado del ticket con las operaciones registradas por el controlador.

**Fuentes obligatorias:**
- `evidence/02_governance/change_tickets.csv`
- `evidence/06_control_plane/controller_audit.csv`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.

### LAB-02-C2
**Problema:** Evalúa la cuenta de servicio involucrada frente a su política de acceso.

**Fuentes obligatorias:**
- `evidence/02_governance/access_policy.csv`
- `evidence/03_identity/privileged_access.csv`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.

### LAB-02-C3
**Problema:** Distingue la actividad de mantenimiento genuina de los cambios posteriores.

**Fuentes obligatorias:**
- `evidence/02_governance/maintenance_attestation.csv`
- `evidence/04_endpoint/process_activity.csv`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.


## Evaluación
Edita `student_work/LAB-02/submission.json`; después:

```bash
python3 labs/runner.py validate LAB-02 --output student_work
```

El estado PASS valida únicamente **estructura y referencias**, no demuestra que la inferencia sea correcta. El examinador revisará fuentes, precisión, incertidumbre y recomendaciones operativas. Máximo interno: 12 puntos (4 por ejercicio).
