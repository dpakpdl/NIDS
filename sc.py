#!/bin/python2.7

from scapy.all import *

words = ["GET", "POST", "DELETE", "HEAD", "PUT", "TRACE", "CONNECT"]

def isHttp(packet):
    packet = str(packet)
    return "HTTP" in packet and any(i in packet for i in words)


f = open('httpdata', 'w')

def pfunc(packet): 
    if isHttp(packet):
        load = packet.load
        f.write(load)
        f.flush()
        lv = load.split('\r\n')
        dictionary = {}
        for i in lv:
            p = i.find(':')
            if p != -1:
                key = i[:p]
                value = i[p + 1:]
                dictionary[key] = value

        for key in dictionary:
           print key,": ",dictionary[key]
        print


sniff(prn=pfunc)
