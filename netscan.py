from scapy.all import ARP , Ether , ls

def scan(ip):
    arp_req = ARP(pdst = ip)
    arp_req.show()
    broadcast = Ether(dst="a0:af:bd:e5:44:0d")
    broadcast.show()
    arp_req_broadcast = broadcast / arp_req
    arp_req_broadcast.show()
    #ls(Ether())
    # print(broadcast.summary()) 

scan("192.168.1.1/24")