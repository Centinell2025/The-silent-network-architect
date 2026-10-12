#!/usr/bin/env python3
"""Read-only analyst workbench for Northbridge Sherlock evidence.

Offline, dependency-free: Python 3.10+; no network access; never modifies evidence.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
from datetime import datetime, timedelta, timezone
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "evidence"
TIME_COLUMNS = ("timestamp_utc", "start_utc", "created_utc", "valid_from_utc")
ID_COLUMNS = (
    "event_id", "alert_id", "request_id", "query_id", "flow_id", "session_id",
    "lease_id", "ticket_id", "receipt_id", "catalog_id", "task_event_id",
    "health_id", "counter_id", "edge_record_id", "snapshot_id", "sample_id",
)

def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()

def safe_path(value: str) -> Path:
    path = (ROOT / value).resolve()
    if not path.is_relative_to(EVIDENCE.resolve()):
        raise ValueError("Only repository-relative evidence/ paths are permitted.")
    if not path.is_file():
        raise ValueError(f"Evidence file not found: {value}")
    return path

def utc(value: str) -> datetime:
    return datetime.fromisoformat(value.strip().replace("Z", "+00:00")).astimezone(timezone.utc)

def show_dt(value: datetime) -> str:
    return value.isoformat(timespec="seconds").replace("+00:00", "Z")

def offset_seconds() -> int:
    path = EVIDENCE / "06_control_plane" / "ntp_samples.csv"
    with path.open(newline="", encoding="utf-8") as f:
        matches = [r for r in csv.DictReader(f) if r["device"] == "NB-EDGE-01"]
    if len(matches) != 1:
        raise ValueError("Expected one bounded clock-calibration sample for NB-EDGE-01")
    return int(matches[0]["offset_seconds_device_ahead"])

def inventory(args: argparse.Namespace) -> None:
    print("Repository evidence inventory (synthetic, read-only)")
    for path in sorted(EVIDENCE.rglob("*")):
        if path.is_file():
            print(f"{rel(path):72} {path.stat().st_size:>8} B")

def search(args: argparse.Namespace) -> None:
    count = 0
    needle = args.term.casefold()
    if not needle:
        raise ValueError("Search term cannot be empty.")
    for path in sorted(EVIDENCE.rglob("*")):
        if path.suffix.lower() not in {".csv", ".log", ".txt", ".md"}:
            continue
        if args.source and args.source.casefold() not in rel(path).casefold():
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            if needle in line.casefold():
                print(f"{rel(path)}:{number}: {line[:240]}")
                count += 1
                if count >= args.limit:
                    print(f"[truncated at {args.limit} matches]")
                    return
    print(f"Matches displayed: {count}")

def inspect(args: argparse.Namespace) -> None:
    path = safe_path(args.path)
    if path.suffix.lower() != ".csv":
        raise ValueError("Inspect supports CSV evidence sources only.")
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        columns = reader.fieldnames or []
        rows = sum(1 for _ in reader)
    print(f"Evidence: {rel(path)}\nRows: {rows}\nFields: {', '.join(columns)}")

def hash_file(args: argparse.Namespace) -> None:
    path = safe_path(args.path)
    print(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {rel(path)}")

def timeline(args: argparse.Namespace) -> None:
    since = utc(args.after) if args.after else None
    until = utc(args.before) if args.before else None
    events = []
    edge_offset = timedelta(seconds=offset_seconds())
    for path in sorted(EVIDENCE.rglob("*.csv")):
        filename = rel(path)
        if args.source and args.source.casefold() not in filename.casefold():
            continue
        with path.open(newline="", encoding="utf-8") as f:
            for i, row in enumerate(csv.DictReader(f), 2):
                raw = next((row.get(k) for k in TIME_COLUMNS if row.get(k)), None)
                corrected = False
                if raw is None and row.get("edge_local_time"):
                    raw = row["edge_local_time"] + "Z"
                    corrected = True
                if not raw:
                    continue
                try:
                    stamp = utc(raw)
                except ValueError:
                    continue
                if corrected:
                    stamp -= edge_offset
                if since and stamp < since:
                    continue
                if until and stamp > until:
                    continue
                label = next((row[k] for k in ID_COLUMNS if row.get(k)), "row")
                detail = " ".join(f"{k}={v}" for k, v in list(row.items())[:10] if v)
                if args.contains and args.contains.casefold() not in detail.casefold():
                    continue
                events.append((stamp, filename, i, label, corrected))
    events.sort(key=lambda z: (z[0], z[1], z[2]))
    if not events:
        print("No matching timeline records.")
        return
    for stamp, name, rownum, label, corrected in events[:args.limit]:
        note = " [edge clock normalized]" if corrected else ""
        print(f"{show_dt(stamp)}  {label:18} {name}:{rownum}{note}")
    print(f"Displayed {min(args.limit, len(events))} of {len(events)} matches. This timeline is not a verdict.")

def parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description="Offline evidence triage — no answers or network activity.")
    sp = ap.add_subparsers(dest="command", required=True)
    a = sp.add_parser("inventory", help="List synthetic evidence artifacts and sizes")
    a.set_defaults(fn=inventory)
    a = sp.add_parser("search", help="Case-insensitive line search across text evidence")
    a.add_argument("term")
    a.add_argument("--source", help="Limit to a filename/path fragment")
    a.add_argument("--limit", type=int, default=25)
    a.set_defaults(fn=search)
    a = sp.add_parser("inspect", help="Show CSV columns and row count")
    a.add_argument("path")
    a.set_defaults(fn=inspect)
    a = sp.add_parser("hash", help="Calculate SHA-256 of a repository evidence file")
    a.add_argument("path")
    a.set_defaults(fn=hash_file)
    a = sp.add_parser("timeline", help="UTC-sort table events, normalizing edge timestamps")
    a.add_argument("--after", help="ISO-8601 UTC start, inclusive")
    a.add_argument("--before", help="ISO-8601 UTC end, inclusive")
    a.add_argument("--source", help="Limit to a file/path fragment")
    a.add_argument("--contains", help="Filter row values; not only event IDs")
    a.add_argument("--limit", type=int, default=40)
    a.set_defaults(fn=timeline)
    return ap

def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    if getattr(args, "limit", 1) < 1:
        raise ValueError("--limit must be a positive integer")
    args.fn(args)
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, OSError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(2)
