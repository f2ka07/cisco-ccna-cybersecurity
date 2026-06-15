#!/usr/bin/env python3
"""Generate synthetic lab PCAP files for CCNA Cybersecurity book."""

from scapy.all import (
    DNS,
    DNSQR,
    Ether,
    IP,
    Raw,
    TCP,
    UDP,
    wrpcap,
)

OUT = __file__.replace("generate_pcaps.py", "")


def demo_tls_pcap():
    """DNS + TCP/443 with TLS Client Hello (Module 2 visibility demo)."""
    client = "192.168.56.101"
    resolver = "8.8.8.8"
    server = "93.184.216.34"
    pkts = []

    eth = Ether(src="00:11:22:33:44:55", dst="00:aa:bb:cc:dd:ee")
    dns = (
        eth
        / IP(src=client, dst=resolver)
        / UDP(sport=54321, dport=53)
        / DNS(rd=1, qd=DNSQR(qname="example.com"))
    )
    pkts.append(dns)

    tls_client_hello = bytes(
        [
            0x16,
            0x03,
            0x01,
            0x00,
            0x2F,
            0x01,
            0x00,
            0x00,
            0x2B,
            0x03,
            0x03,
        ]
        + [0xAB] * 32
        + [0x00, 0x00, 0x04, 0xC0, 0x2F, 0x00, 0xFF, 0x01, 0x00]
    )

    syn = (
        eth
        / IP(src=client, dst=server)
        / TCP(sport=49876, dport=443, flags="S", seq=1000)
    )
    synack = (
        eth
        / IP(src=server, dst=client)
        / TCP(sport=443, dport=49876, flags="SA", seq=2000, ack=1001)
    )
    ack = (
        eth
        / IP(src=client, dst=server)
        / TCP(sport=49876, dport=443, flags="A", seq=1001, ack=2001)
    )
    client_hello = (
        eth
        / IP(src=client, dst=server)
        / TCP(sport=49876, dport=443, flags="PA", seq=1001, ack=2001)
        / Raw(load=tls_client_hello)
    )
    pkts.extend([syn, synack, ack, client_hello])

    path = OUT + "demo-tls.pcap"
    wrpcap(path, pkts)
    print("Wrote", path, len(pkts), "packets")


def intrusion_lab_pcap():
    """HTTP download of update.exe (Module 4 file extraction lab)."""
    client = "192.168.56.101"
    server = "198.51.100.10"
    sport = 49152
    body = b"MZ" + b"\x00" * 62  # minimal PE-like stub for export exercise

    req = (
        "GET /download/update.exe HTTP/1.1\r\n"
        "Host: cdn.lab-intrusion.test\r\n"
        "User-Agent: Mozilla/5.0 LabBrowser/1.0\r\n"
        "Connection: close\r\n\r\n"
    )
    resp = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: application/octet-stream\r\n"
        f"Content-Length: {len(body)}\r\n"
        "Connection: close\r\n\r\n"
    ).encode() + body

    eth = Ether(src="00:11:22:33:44:55", dst="00:aa:bb:cc:dd:ee")
    pkts = []
    seq_c, seq_s = 1000, 5000

    pkts.append(
        eth / IP(src=client, dst=server) / TCP(sport=sport, dport=80, flags="S", seq=seq_c)
    )
    pkts.append(
        eth
        / IP(src=server, dst=client)
        / TCP(sport=80, dport=sport, flags="SA", seq=seq_s, ack=seq_c + 1)
    )
    seq_c += 1
    pkts.append(
        eth
        / IP(src=client, dst=server)
        / TCP(sport=sport, dport=80, flags="A", seq=seq_c, ack=seq_s + 1)
    )

    req_pkt = (
        eth
        / IP(src=client, dst=server)
        / TCP(sport=sport, dport=80, flags="PA", seq=seq_c, ack=seq_s + 1)
        / Raw(load=req.encode())
    )
    pkts.append(req_pkt)
    seq_c += len(req.encode())

    resp_pkt = (
        eth
        / IP(src=server, dst=client)
        / TCP(sport=80, dport=sport, flags="PA", seq=seq_s + 1, ack=seq_c)
        / Raw(load=resp)
    )
    pkts.append(resp_pkt)

    path = OUT + "intrusion-lab.pcap"
    wrpcap(path, pkts)
    print("Wrote", path, len(pkts), "packets")


if __name__ == "__main__":
    demo_tls_pcap()
    intrusion_lab_pcap()
