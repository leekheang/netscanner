#conda install -c pdrops scapy
#run as root
import scapy.all as  scapy
import argparse 
# import optparse 

# def get_arguments():
#         parser = optparse.OptionParser()
#         parser.add_option("-t", "--target", dest="target", help="Target IP/ IP range .")
#         (options , arguments) = parser.parse_args()
#         return options


def get_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("-t", "--target", dest="target", help="Target IP/ IP range .")
        options  = parser.parse_args()
        return options

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
options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)