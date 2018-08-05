import socket
import struct
import binascii
from lights import lights
# Written by Bob Steinbeiser (https://medium.com/@xtalker)

rawSocket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW,
                          socket.htons(0x0003))
MAC = '50f5da0efe74'

while True:
    packet = rawSocket.recvfrom(2048)

    ethernet_header = packet[0][0:14]
    ethernet_detailed = struct.unpack('!6s6s2s', ethernet_header)

    # skip non-ARP packets
    ethertype = ethernet_detailed[2]
    if ethertype != '\x08\x06':
        continue

    arp_header = packet[0][14:42]
    arp_detailed = struct.unpack('2s2s1s1s2s6s4s6s4s', arp_header)


    source_mac = binascii.hexlify(arp_detailed[5])
    dest_ip = socket.inet_ntoa(arp_detailed[8])
    print(source_mac)
    if source_mac == MAC:
        print "Dash button pressed!, IP = " + dest_ip
        lights()

