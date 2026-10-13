#!/usr/bin/env python3
"""Validate deterministic synthetic PCAP against the repository NetFlow data; no spoilers."""
from pathlib import Path
import csv,struct
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from tools.generate_synthetic_pcap import construct,PCAP,INDEX
trace,index,total=construct()
assert PCAP.read_bytes()==trace, "Committed PCAP is not reproducible"
assert INDEX.read_bytes()==index, "Committed fixture index differs from generator"
assert trace[:4]==bytes.fromhex("d4c3b2a1")
assert struct.unpack_from("<HH",trace,4)==(2,4)
assert struct.unpack_from("<I",trace,20)[0]==1, "PCAP linktype must be Ethernet"
offset=24;packet_count=0;first_syn=set();udp_count=0;last_sec=0
while offset<len(trace):
    assert offset+16<=len(trace), "Incomplete packet header"
    sec,micros,size,actual=struct.unpack_from("<IIII",trace,offset);offset+=16
    assert size==actual and size<=65535 and micros<1000000
    assert offset+size<=len(trace), "Packet truncated"
    packet=trace[offset:offset+size];offset+=size
    assert packet[12:14]==bytes.fromhex("0800"),"Only IPv4 expected"
    assert packet[14]>>4==4,"IP protocol version"
    ihl=(packet[14]&15)*4
    assert ihl>=20
    assert struct.unpack_from("!H",packet,16)[0]==size-14,"IP length differs from Ethernet frame"
    proto=packet[23]
    src=".".join(str(x) for x in packet[26:30])
    dst=".".join(str(x) for x in packet[30:34])
    sport,dport=struct.unpack_from("!HH",packet,14+ihl)
    if proto==6:
        flags=packet[14+ihl+13]
        if flags==2:first_syn.add((src,str(sport),dst,str(dport)))
    elif proto==17:udp_count+=1
    else:raise AssertionError("Unsupported generated packet protocol")
    packet_count+=1
assert packet_count==total and packet_count>=380
assert udp_count>=6 and len(first_syn)>=120
with (ROOT/"evidence/05_network/netflow.csv").open(newline="",encoding="utf-8") as f:
    anchors=list(csv.DictReader(f))
assert len(anchors)>=4
for row in anchors:
    assert (row["src_ip"],row["src_port"],row["dst_ip"],row["dst_port"]) in first_syn, "Missing fixture tuple for case flow"
with INDEX.open(newline="",encoding="utf-8") as f:
    rows=list(csv.DictReader(f))
assert len(rows)>=120
assert len({r["fixture_id"] for r in rows})==len(rows)
print(f"PASS: synthetic PCAP validated, {packet_count} packets, {len(rows)} indexed modeled conversations, no native capture claim")
