#conda instal -c pdrop scapy
#run as root
import scapy.all as scapy

def scan(ip):
    arp_req = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broadcast = broadcast / arp_req
    answered_list = scapy.srp(arp_req_broadcast, timeout=1, verbose=False)[0]
    
    print("IP\t\t\tMac Address\n-----------------------------------------")
    client_list = []
    for el in answered_list:
        client_dict = {"ip": el[1].psrc, "mac": el[1].hwsrc}
        client_list.append(client_dict)
        print(el[1].psrc + "\t\t" + el[1].hwsrc)
        print("-----------------------------------------")
    print(client_list)

scan("192.168.1.1/24")