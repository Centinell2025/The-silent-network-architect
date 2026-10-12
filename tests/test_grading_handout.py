#!/usr/bin/env python3
"""Reject missing/duplicate reviewer question IDs without exposing answers."""
from pathlib import Path
import re
R=Path(__file__).resolve().parents[1]
main=(R/"questions/INVESTIGATION.md").read_text(encoding="utf-8")
alternative=(R/"questions/STATIC_GRADING_CANDIDATE.md").read_text(encoding="utf-8")
primary=re.findall(r"\[Q([0-9]{2})\]",main)
assert primary==[f"{i:02}" for i in range(1,31)],primary
for x in range(25,31):
    assert re.search(rf"\| Q{x} \|",alternative),f"Missing alternate Q{x}"
assert "HTB staff" in alternative
print("PASS: 30 primary questions and all six optional exact-format alternatives")
