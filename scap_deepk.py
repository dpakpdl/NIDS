#!/bin/python2.7

from scapy.all import *

# usual kinds of request
words = ["GET", "POST", "DELETE", "HEAD", "PUT", "TRACE", "CONNECT"]
# attributes in our dataset CSIC 2010
attributes= ["Method", "Host", "Content-Type","Content-Length","Length1","Length2","Length3","Length4","Length11"]

#file to store data offline
f = open('httpdatadeepak', 'w')
#store key value pair of HTTP payload 
dictionary = {}

def isHttp(packet):
    # print packet[IP].len-40 // load = total -(IP+tcp)
    packet = str(packet)
    return "HTTP" in packet and any(i in packet for i in words)

# filters the payload on basis of only the attributes required to us
def filter(load):
    lv = load.split('\r\n')
    for i in lv:
        p = i.find(':')
        if p != -1:
            key = i[:p]
            value = i[p+1:]
            if key in attributes:
               dictionary[key]=value
    for k,v in dictionary.items():
        print >> f,k+': '+v
    print >> f

def pfunc(packet): 
    if isHttp(packet):
        print packet[TCP].payload
        for att in words:
            if att in str(packet):
                dictionary['Method'] = att
                dictionary['Length1']= str(len(packet[TCP].payload))
                dictionary['Length11']= str(packet.len)
                dictionary['Length2']= str(len(packet.payload.load))
                dictionary['Length3']= str(len(packet[TCP])-40)
                dictionary['Length4']= str(packet[IP].len-len(packet[IP].options)-len(packet[TCP].options))
        load = packet.load
        filter(load)
        f.flush()

sniff(prn=pfunc)
