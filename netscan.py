#conda instal -c pdrop scapy
#run as root
import scapy.all as scapy

def scan(ip):
    arp_req = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broadcast = broadcast / arp_req
    answered_list = scapy.srp(arp_req_broadcast, timeout=1, verbose=False)[0]
    
    
    client_list = []
    for el in answered_list:
        client_dict = {"ip": el[1].psrc, "mac": el[1].hwsrc}
        client_list.append(client_dict)
    return client_list

def print_result(result_list):
        print("IP\t\t\tMac Address\n-----------------------------------------")
        for client in result_list:
                print(client["ip"] + "\t\t" + client["mac"])

scan_result = scan("192.168.1.1/24")
print_result(scan_result)