# Northbridge Systems — Laboratorios DFIR/SOC

**Autor:** Beacon of the Eagle LLC · Centinell Suite Defense  
**Víctima ficticia:** Northbridge Systems  
**Plataformas:** Kali Linux, Ubuntu y Windows con Python 3.10+  
**Contenido:** **14 laboratorios, 42 ejercicios** complementarios a las 30 preguntas del Sherlock.

Son investigaciones defensivas **100 % offline** con evidencias simuladas y un PCAP generado artificialmente. No se utiliza malware activo, no se escanean IP, y no se requiere acceso a redes ajenas. La guía del profesor y las respuestas no están incluidas.

## Ejecutar un laboratorio
Desde la raíz del ZIP del estudiante:

```bash
python3 labs/runner.py list
python3 labs/runner.py start LAB-01 --output student_work
python3 tools/workbench.py inventory
python3 tools/packet_inspector.py summary
# Completar student_work/LAB-01/submission.json
python3 labs/runner.py validate LAB-01 --output student_work
```

El comprobador **NO conoce las respuestas**. Solo verifica que la investigación tenga conclusiones, dos citas válidas por ejercicio, una hipótesis alternativa y nivel de confianza. El instructor debe comprobar el análisis, no solo el formulario.

| Laboratorio | Tema | Nivel | Checkpoints |
|---|---|---|---|
| [LAB-01](LAB-01/README.md) | Integridad y cadena de custodia | Foundations | 3 |
| [LAB-02](LAB-02/README.md) | Cambios de red bajo sospecha | Intermediate | 3 |
| [LAB-03](LAB-03/README.md) | Identidad y puesto compartido | Advanced | 3 |
| [LAB-04](LAB-04/README.md) | Dos relojes y una cronología | Advanced | 3 |
| [LAB-05](LAB-05/README.md) | Monitoreo en verde, sensor ciego | Advanced | 3 |
| [LAB-06](LAB-06/README.md) | Procesos y salto privilegiado | Advanced | 3 |
| [LAB-07](LAB-07/README.md) | Integridad de la exportación | Advanced | 3 |
| [LAB-08](LAB-08/README.md) | DNS, NetFlow y proxy | Advanced | 3 |
| [LAB-09](LAB-09/README.md) | Análisis PCAP sintético | Expert | 3 |
| [LAB-10](LAB-10/README.md) | Persistencia y restauración | Expert | 3 |
| [LAB-11](LAB-11/README.md) | Reglas SOC y falsos positivos | Expert | 3 |
| [LAB-12](LAB-12/README.md) | Informe ejecutivo de respuesta | Expert | 3 |
| [LAB-13](LAB-13/README.md) | Reconstrucción con indicios contradictorios | Expert+ | 3 |
| [LAB-14](LAB-14/README.md) | Simulacro de crisis SOC y comunicación | Expert+ | 3 |

**Total:** 14 laboratorios, 42 checkpoints, más las 30 preguntas principales del Sherlock. Los checkpoints son actividades formativas, **no preguntas oficiales de HTB**.

## Criterios de calidad
Cada checkpoint se valora 0 a 4: sin respuesta, conjetura, evidencia parcial, correlación verificable, o correlación reproducible con incertidumbre y consecuencia operativa. La puntuación de los laboratorios es solo una rúbrica de autoría, no un sistema de notas HTB.

**Reglas:** no atribuir una persona por una IP compartida; validar horarios UTC y fuentes; registrar alternativas; no suponer contenido TLS ausente; distinguir un PCAP sintético de una captura nativa. Conservar evidencia inalterada y entregar trabajo en otra carpeta.
