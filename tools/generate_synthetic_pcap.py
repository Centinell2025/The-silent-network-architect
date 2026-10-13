#!/usr/bin/env python3
"""Deterministic, offline packet fixture. NOT a real packet capture or TLS content."""
from __future__ import annotations
import argparse,csv,datetime as dt,hashlib,io,ipaddress,random,struct
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"evidence/11_packet_fixture"
PCAP=OUT/"synthetic_network_fixture.pcap"
INDEX=OUT/"CAPTURE_PROVENANCE.csv"
def checksum(buf):
    if len(buf)%2: buf+=b"\x00"
    total=sum((buf[i]<<8)+buf[i+1] for i in range(0,len(buf),2))
    while total>>16:total=(total&65535)+(total>>16)
    return (~total)&65535
def address(s):return ipaddress.IPv4Address(s).packed
def ip(src,dst,content,proto,ident):
    h=struct.pack("!BBHHHBBH4s4s",69,0,20+len(content),ident&65535,16384,64,proto,0,address(src),address(dst))
    h=h[:10]+struct.pack("!H",checksum(h))+h[12:]
    return bytes.fromhex("0200420010010200420010020800")+h+content
def tcp(src,sport,dst,dport,seq,ack,flags,ident):
    h=struct.pack("!HHIIHHHH",sport,dport,seq,ack,(5<<12)|flags,4096,0,0)
    pseudo=address(src)+address(dst)+struct.pack("!BBH",0,6,len(h))
    h=h[:16]+struct.pack("!H",checksum(pseudo+h))+h[18:]
    return ip(src,dst,h,6,ident)
def udp(src,sport,dst,dport,payload,ident):
    h=struct.pack("!HHHH",sport,dport,8+len(payload),0)
    pseudo=address(src)+address(dst)+struct.pack("!BBH",0,17,len(h)+len(payload))
    h=h[:6]+struct.pack("!H",checksum(pseudo+h+payload) or 65535)
    return ip(src,dst,h+payload,17,ident)
def qname(host):
    return b"".join(bytes([len(p)])+p.encode("ascii") for p in host.split("."))+b"\x00"
def stamp(s):return int(dt.datetime.fromisoformat(s.replace("Z","+00:00")).timestamp())
def utc(t):return dt.datetime.fromtimestamp(t,dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
def construct():
    rng=random.Random(20261006);packets=[];entries=[["fixture_id","source_record","time_utc","source_ip","source_port","destination_ip","destination_port","protocol","source_class"]]
    def append(sec,usec,data):packets.append((sec,usec,data))
    with (ROOT/"evidence/05_network/netflow.csv").open(encoding="utf-8",newline="") as f:
        flows=list(csv.DictReader(f))
    anchored=set()
    for i,f in enumerate(flows):
        s,d=f["src_ip"],f["dst_ip"];sport,dport=int(f["src_port"]),int(f["dst_port"]);at=stamp(f["start_utc"])
        seq=rng.randrange(1000,2**31);other=rng.randrange(1000,2**31)
        for n,(src,sp,dst,dp,serial,ack,flags) in enumerate([
            (s,sport,d,dport,seq,0,2),(d,dport,s,sport,other,seq+1,18),
            (s,sport,d,dport,seq+1,other+1,16),
            (s,sport,d,dport,seq+1,other+1,17),
            (d,dport,s,sport,other+1,seq+2,17)]):
            append(at+(n//3),[120000,260000,390000,200000,550000][n],tcp(src,sp,dst,dp,serial,ack,flags,i*8+n+1))
        anchored.add((s,sport,d,dport))
        entries.append([f"F-PCAP-{i+1:03}",f["flow_id"],f["start_utc"],s,sport,d,dport,"tcp","modeled_netflow_tuple"])
    srcs=["10.42.10.44","10.42.10.77","10.42.20.40","10.42.30.12","10.42.10.25"]
    dsts=["198.51.100.28","198.51.100.55","203.0.113.20","192.0.2.44","198.51.100.88"]
    start=stamp("2026-10-06T01:30:00Z")
    for i in range(120):
        s=srcs[(i*5+i//3)%len(srcs)];d=dsts[(i*7+i//5)%len(dsts)]
        sp=41000+i;dp=[443,8443,80,443][i%4];t=start+i*29
        assert (s,sp,d,dp) not in anchored
        seq=rng.randrange(1000,2**31);other=rng.randrange(1000,2**31)
        append(t,i%1000,tcp(s,sp,d,dp,seq,0,2,1000+3*i))
        append(t,100000+i%1000,tcp(d,dp,s,sp,other,seq+1,18,1001+3*i))
        append(t,240000+i%1000,tcp(s,sp,d,dp,seq+1,other+1,16,1002+3*i))
        entries.append([f"F-BG-{i+1:03}",f"generated_background_{i+1:03}",utc(t),s,sp,d,dp,"tcp","modeled_background"])
    for i,(src,host,dst) in enumerate([
        ("10.42.30.12","health.status-sync.example","198.51.100.28"),
        ("10.42.10.25","collector.telemetry-audit.example","203.0.113.77"),
        ("10.42.10.44","updates.internal.northbridge.example","10.42.30.12")]):
        sec=start+i*1000+60;name=qname(host);txid=3500+i
        query=struct.pack("!HHHHHH",txid,256,1,0,0,0)+name+struct.pack("!HH",1,1)
        response=struct.pack("!HHHHHH",txid,33152,1,1,0,0)+name+struct.pack("!HH",1,1)+b"\xc0\x0c"+struct.pack("!HHIH",1,1,60,4)+address(dst)
        append(sec,100000,udp(src,53000+i,"10.42.10.10",53,query,5000+i))
        append(sec,130000,udp("10.42.10.10",53,src,53000+i,response,5004+i))
        entries.append([f"F-DNS-{i+1:03}","modeled_dns_pair",utc(sec),src,53000+i,"10.42.10.10",53,"udp","modeled_dns_fixture"])
    packets.sort(key=lambda x:(x[0],x[1]))
    f=io.BytesIO();f.write(struct.pack("<IHHIIII",0xa1b2c3d4,2,4,0,0,65535,1))
    for sec,micro,data in packets:
        f.write(struct.pack("<IIII",sec,micro,len(data),len(data)));f.write(data)
    index=io.StringIO();csv.writer(index,lineterminator="\n").writerows(entries)
    return f.getvalue(),index.getvalue().encode("utf-8"),len(packets)
def main():
    parser=argparse.ArgumentParser(description=__doc__)
    g=parser.add_mutually_exclusive_group(required=True);g.add_argument("--write",action="store_true");g.add_argument("--check",action="store_true")
    args=parser.parse_args()
    pcap,idx,n=construct()
    if args.write:
        OUT.mkdir(parents=True,exist_ok=True);PCAP.write_bytes(pcap);INDEX.write_bytes(idx)
    if not PCAP.exists() or not INDEX.exists() or PCAP.read_bytes()!=pcap or INDEX.read_bytes()!=idx:
        raise SystemExit("FAIL: fixture does not match deterministic source; use --write")
    print(f"PASS: {n} synthetic Ethernet packets, {len(idx.splitlines())-1} index rows, SHA256={hashlib.sha256(pcap).hexdigest()}")
if __name__=="__main__":main()
