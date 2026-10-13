# LAB-04 — Dos relojes y una cronología

**Dificultad:** Advanced · **Escenario:** NB-IR-2026-104 · **Autor:** Beacon of the Eagle LLC

## Objetivo
Normaliza tiempos de dispositivos antes de comparar eventos que parecen contradictorios. La infraestructura de Northbridge Systems, sus personas y sus datos son ficticios. Los analistas deben presentar inferencias apoyadas en evidencias, no suposiciones.

## Preparación
Trabaja con Python 3.10+ en Kali Linux, Ubuntu o Windows; sin instalación adicional ni acceso a Internet. En la raíz del paquete extraído:

```bash
python3 labs/runner.py start LAB-04 --output student_work
python3 tools/workbench.py inventory
python3 tools/workbench.py timeline --limit 25
```

En Windows, utiliza `py -3` si `python3` no existe. Para PCAP emplea `python3 tools/packet_inspector.py summary` y para fuentes CSV, `python3 tools/workbench.py inspect evidencia.csv` cambiando la ruta por un archivo real.

## Tres ejercicios verificables

### LAB-04-C1
**Problema:** Calcula la equivalencia UTC de un evento local de firewall y declara la incertidumbre.

**Fuentes obligatorias:**
- `evidence/05_network/acl_policy_log.csv`
- `evidence/06_control_plane/ntp_samples.csv`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.

### LAB-04-C2
**Problema:** Explica cualquier discrepancia temporal entre el firewall y el controlador.

**Fuentes obligatorias:**
- `evidence/05_network/acl_policy_log.csv`
- `evidence/06_control_plane/controller_audit.csv`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.

### LAB-04-C3
**Problema:** Evalúa si una conexión de NetFlow coincide después de aplicar la corrección del reloj.

**Fuentes obligatorias:**
- `evidence/06_control_plane/ntp_samples.csv`
- `evidence/05_network/netflow.csv`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.


## Evaluación
Edita `student_work/LAB-04/submission.json`; después:

```bash
python3 labs/runner.py validate LAB-04 --output student_work
```

El estado PASS valida únicamente **estructura y referencias**, no demuestra que la inferencia sea correcta. El examinador revisará fuentes, precisión, incertidumbre y recomendaciones operativas. Máximo interno: 12 puntos (4 por ejercicio).
