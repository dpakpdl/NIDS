#!/bin/python2.7

from scapy.all import *

# usual kinds of request
words = ["GET", "POST", "DELETE", "HEAD", "PUT", "TRACE", "CONNECT"]
# attributes in our dataset CSIC 2010
attributes= ["User-Agent", "Pragma", "Cache-Control", "Accept",
            "Accept-Encoding", "Accept-Charset", "Accept-Language",
            "Host", "Cookie", "Content-Type", "Connection",
            "Content-Length", "id", "modo", "idA", "errorMsg",
            "errorMsgA", "B2", "B2A", "modoA", "nombre", "nombreA"]

#file to store data offline
f = open('httpdata', 'w')
#store key value pair of HTTP payload 
dictionary = {}

def isHttp(packet):
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
        load = packet.load
        filter(load)
        f.flush()

sniff(prn=pfunc)
