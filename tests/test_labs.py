#!/usr/bin/env python3
"""Pruebas de los 14 laboratorios sin publicar soluciones."""
from pathlib import Path
import sys,hashlib,tempfile,subprocess
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from labs.runner import lab_for,template,verify,source_path
cases=[lab_for(f"LAB-{n:02}") for n in range(1,15)]
assert len(cases)==14 and sum(len(c["checkpoints"]) for c in cases)==42
for lab in cases:
    assert (ROOT/"labs"/lab["id"]/"README.md").is_file()
    assert len(lab["objective"])>55
    sheet=template(lab)
    assert verify(lab,sheet), "Blank responses must be rejected"
    for question,answer in zip(lab["checkpoints"],sheet["checkpoints"]):
        assert len(question["sources"])==2 and len(set(question["sources"]))==2
        answer["claim"]="A valid structure test that makes no forensic assertion or secret disclosure."
        answer["alternative"]="An independent native capture might contradict this synthetic source."
        answer["confidence"]="low"
        for citation in answer["citations"]:
            f=source_path(citation["path"])
            citation["observation"]="This file is included for controlled case evidence inspection."
            if f.suffix in (".pcap",".zip"):
                citation["record"]="sha256:"+hashlib.sha256(f.read_bytes()).hexdigest()
            else:
                txt=f.read_text(encoding="utf-8").splitlines()
                line=next(x for x in txt if x.strip() and not x.startswith("#"))
                citation["record"]=line[:min(12,len(line))]
    assert not verify(lab,sheet), f"Structured citation check: {lab['id']} - {verify(lab,sheet)}"
    sheet["checkpoints"][0]["citations"][0]["record"]="NONEXISTENT_EVIDENCE_TOKEN"
    assert verify(lab,sheet),"Fictitious record must be rejected"
with tempfile.TemporaryDirectory() as temp:
    cmd=[sys.executable,str(ROOT/"labs/runner.py")]
    listing=subprocess.run(cmd+["list"],capture_output=True,text=True,check=True).stdout
    assert listing.count("LAB-")==14
    subprocess.run(cmd+["start","LAB-14","--output",temp],check=True,capture_output=True)
    path=Path(temp)/"LAB-14"/"submission.json"
    assert path.is_file()
    assert subprocess.run(cmd+["validate","LAB-14","--output",temp],capture_output=True).returncode==1
print("PASS: 14 labs, 42 checkpoints, cited-source structure, rejects blank/fake claims, CLI smoke test")
