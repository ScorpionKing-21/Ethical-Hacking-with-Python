#!/bin/usr/env python3

import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
	scapy.sniff(iface=interface, store=False, prn=sniffed_packets)

def sniffed_packets(packet):
	print(packet.show())

sniff("Intel(R) Wireless-AC 9560 160MHz")