#conda instal -c pdrop scapy
#run as root
import scapy.all as scapy

def scan(ip):
    arp_req = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broadcast = broadcast / arp_req
    answered_list = scapy.srp(arp_req_broadcast, timeout=1, verbose=False)[0]
    
    for el in answered_list:
        print(el[1].psrc)
        print(el[1].hwsrc)
        print("----------------------------------")

scan("192.168.1.1/24")