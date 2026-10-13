#!/usr/bin/env python3
"""Read-only synthetic PCAP triage, using Python standard library only."""
from pathlib import Path
import argparse,datetime as dt,ipaddress,struct
PCAP=Path(__file__).resolve().parents[1]/"evidence/11_packet_fixture/synthetic_network_fixture.pcap"
def entries():
    data=PCAP.read_bytes()
    if len(data)<24 or data[:4]!=bytes.fromhex("d4c3b2a1"):raise ValueError("Invalid little-endian PCAP")
    if struct.unpack_from("<HH",data,4)!=(2,4):raise ValueError("Unsupported PCAP version")
    i=24
    while i<len(data):
        if i+16>len(data):raise ValueError("Truncated packet header")
        sec,usec,size,original=struct.unpack_from("<IIII",data,i);i+=16
        if size>65535 or size!=original or i+size>len(data):raise ValueError("Invalid packet length")
        pkt=data[i:i+size];i+=size
        if len(pkt)<34 or pkt[12:14]!=bytes.fromhex("0800"):continue
        ihl=(pkt[14]&15)*4
        if len(pkt)<14+ihl+4:continue
        proto=pkt[23]
        src=str(ipaddress.IPv4Address(pkt[26:30]))
        dst=str(ipaddress.IPv4Address(pkt[30:34]))
        sp,dp=struct.unpack_from("!HH",pkt,14+ihl)
        flags=pkt[14+ihl+13] if proto==6 and len(pkt)>=14+ihl+14 else 0
        yield sec,usec,src,sp,dst,dp,proto,flags,size
def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command",choices=("summary","flows","dns"))
    parser.add_argument("--limit",type=int,default=30)
    a=parser.parse_args()
    if a.limit<1:raise SystemExit("Positive --limit required")
    rows=list(entries())
    if a.command=="summary":
        print(f"Synthetic offline PCAP: {len(rows)} packets; {sum(x[6]==6 and x[7]==2 for x in rows)} TCP SYNs; {sum(x[6]==17 for x in rows)} UDP/DNS packets")
        print("Not a live capture. The TCP streams contain no genuine TLS application payload.")
    else:
        n=0
        for s,m,src,sp,dst,dp,proto,flags,size in rows:
            if a.command=="flows" and not (proto==6 and flags==2):continue
            if a.command=="dns" and proto!=17:continue
            print(f"{dt.datetime.fromtimestamp(s,dt.timezone.utc).isoformat()} {src}:{sp} -> {dst}:{dp} {'TCP SYN' if proto==6 else 'UDP/DNS synthetic'}")
            n+=1
            if n>=a.limit:break
if __name__=="__main__":main()
