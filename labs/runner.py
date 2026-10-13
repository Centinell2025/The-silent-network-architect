#!/usr/bin/env python3
"""Investigación offline: crea plantillas y revisa citas; NO contiene respuestas."""
from __future__ import annotations
import argparse,hashlib,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];HERE=Path(__file__).resolve().parent
IDS={f"LAB-{i:02}" for i in range(1,15)}
SHA=re.compile(r"^sha256:([0-9a-f]{64})$")
def lab_for(name):
    if name not in IDS:raise ValueError("Laboratorio desconocido")
    lab=json.loads((HERE/name/"lab.json").read_text(encoding="utf-8"))
    if lab["id"]!=name or len(lab["checkpoints"])!=3:raise ValueError("Manifiesto incorrecto")
    return lab
def source_path(path):
    p=Path(path)
    if p.is_absolute() or ".." in p.parts or not path.startswith("evidence/"):raise ValueError("Ruta de evidencia no permitida")
    full=(ROOT/p).resolve()
    if not full.is_relative_to((ROOT/"evidence").resolve()) or not full.is_file():raise ValueError("Evidencia inexistente")
    return full
def template(lab):
    return {"lab_id":lab["id"],"case_id":"NB-IR-2026-104","checkpoints":[{"id":c["id"],"claim":"","citations":[{"path":p,"record":"","observation":""} for p in c["sources"]],"alternative":"","confidence":""} for c in lab["checkpoints"]]}
def verify(lab,sub):
    errors=[]
    if sub.get("lab_id")!=lab["id"]:errors.append("ID de laboratorio no coincide")
    answers=sub.get("checkpoints")
    if not isinstance(answers,list) or len(answers)!=3:return errors+["Se requieren tres checkpoints"]
    for q,ans in zip(lab["checkpoints"],answers):
        key=q["id"]
        if not isinstance(ans,dict) or ans.get("id")!=key:errors.append(key+": identificador incorrecto");continue
        if len(str(ans.get("claim","")).strip())<24:errors.append(key+": falta conclusión detallada")
        if len(str(ans.get("alternative","")).strip())<20:errors.append(key+": falta hipótesis alternativa")
        if ans.get("confidence") not in ("low","medium","high"):errors.append(key+": confianza no válida")
        cites=ans.get("citations")
        if not isinstance(cites,list) or len(cites)!=2:errors.append(key+": se requieren dos citas");continue
        if sorted(c.get("path","") for c in cites if isinstance(c,dict))!=sorted(q["sources"]):
            errors.append(key+": referencias no corresponden a las fuentes exigidas");continue
        for c in cites:
            try:f=source_path(c["path"])
            except (ValueError,KeyError) as exc:errors.append(key+": "+str(exc));continue
            record=str(c.get("record","")).strip()
            if len(str(c.get("observation","")).strip())<15:errors.append(key+": explique qué demuestra cada fuente")
            h=SHA.fullmatch(record)
            if f.suffix in (".pcap",".zip"):
                if not h or hashlib.sha256(f.read_bytes()).hexdigest()!=h.group(1):errors.append(key+": hash binario ausente o incorrecto")
            elif h:
                if hashlib.sha256(f.read_bytes()).hexdigest()!=h.group(1):errors.append(key+": SHA-256 incorrecto")
            elif not record or record.encode("utf-8") not in f.read_bytes():errors.append(key+": identificador ausente de "+str(c["path"]))
    return errors
def main():
    p=argparse.ArgumentParser(description=__doc__);subs=p.add_subparsers(dest="command",required=True);subs.add_parser("list")
    for cmd in ("start","validate"):
        a=subs.add_parser(cmd);a.add_argument("lab_id");a.add_argument("--output",required=True,type=Path)
    a=p.parse_args()
    if a.command=="list":
        for n in sorted(IDS):
            l=lab_for(n);print(n,l["level"],l["title"],sep=" | ")
        return 0
    lab=lab_for(a.lab_id);folder=a.output.resolve()/a.lab_id;doc=folder/"submission.json"
    if a.command=="start":
        folder.mkdir(parents=True,exist_ok=True)
        if doc.exists():print("Ya existe, se conserva:",doc);return 0
        doc.write_text(json.dumps(template(lab),indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
        print("Creada:",doc);return 0
    if not doc.is_file():print("Falta plantilla; usa start",file=sys.stderr);return 2
    errors=verify(lab,json.loads(doc.read_text(encoding="utf-8")))
    for e in errors:print("REVISAR:",e,file=sys.stderr)
    if errors:return 1
    print("PASS: 3 ejercicios documentados con referencias; revisión forense humana pendiente");return 0
if __name__=="__main__":
    try:sys.exit(main())
    except (OSError,ValueError,KeyError,json.JSONDecodeError) as exc:print("ERROR:",exc,file=sys.stderr);sys.exit(2)
