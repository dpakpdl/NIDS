#!/usr/bin/python
"""list of libraries and functions imported"""
from numpy import*
#from os import listdir
import numpy as np
#from sklearn.multiclass import OneVsRestClassifier
from sklearn.externals import joblib
#from sklearn.metrics import confusion_matrix
from sklearn import svm
from pca import principal_component_analysis
import os
from random import randint
from scapy.all import sniff

# attributes in our dataset CSIC 2010
attributes = ["Host", "Content-Length", "Content-Type", "Method"]
features = {'typ': ["Content-Type"], 'host': ["Host"], 'methods': ["Method"]}

# usual kinds of request and their numbering in order
methods = ["GET", "POST", "DELETE", "HEAD", "PUT", "TRACE", "CONNECT"]

#usual kinds of Content-Type and their numbering in order
typ = [" application/x-www-form-urlencoded"," application/json"," multipart/form-data", " application/ocsp-request", " text/plain;charset=UTF-8"]

#usual type of host
host = [" localhost:8080"," localhost:9090"," localhost:8090"," onlineparikshya.com", " localhost"]

#store key value pair of HTTP payload
dictionary = {}


#child function to write to a pipe
def child(pipeout):
    def search(searchFor):
        for k in features:
            for v in features[k]:
                if searchFor in v:
                    return k
        return None

    def isHttp(packet):
        packet = str(packet)
        return "HTTP" in packet and any(i in packet for i in methods)

# filters the payload on basis of only the attributes required to us
    def filter(load):
        lv = load.split('\r\n')
        for i in lv:
            p = i.find(':')
            if p != -1:
                key = i[:p]
                value = i[p+1:]
                #provide numerical value to content-type
                if key=='Content-Type' or key=='Host':
                    #EVAL CONverts string to preexisting variable name
                    dictionary[key]=str(eval(search(key)).index(value)+1)
                elif key in attributes: dictionary[key]=str(value)
                #assign default value
                for k in attributes:
                    if k not in dictionary:
                        dictionary[k]=str('0')
               # calculation of Payload
                if dictionary['Method']=='0':
                    try:
                        start=load.index('?')
                        end=load.index('HTTP/')
                        dictionary['Payload']=str(len(load[start:end-2]))
                    except ValueError:
                        return ""
                else:
                    dictionary['Payload']=dictionary['Content-Length']

        # writing data in file
                """
        for k,v in dictionary.items():
            f.flush()
            print >> f,k+': '+v,
        print >> f
        dictionary.clear()
        """
        print dictionary.values()
        print dictionary.keys()
        os.write(pipeout, str(dictionary.values())+'a')
#        os.write(pipeout,'\n')

    def pfunc(packet):
        if isHttp(packet):
            for att in methods:
                if att in str(packet):
                    dictionary['Method'] = str(methods.index(att))
            load = packet.load
            filter(packet.load)

    sniff(prn=pfunc)

"""parent function to read fron the pipe"""
def parent():
    pipein, pipeout = os.pipe()
    if os.fork() == 0:
        child(pipeout)
    else:
        while True:
            verse = os.read(pipein,500)
            verse1 = verse.split('a')
            res = []
            for myList in verse1:
                if myList != '':
                    data1 = eval(myList)
                    k = list(map(int, data1))
                    res.append(k)
            data2 = [1, 237, 1, 237, 1]
            data = np.asarray(res + [data2])
            live_data = mat(log10(data[:, :5]))
            N = 2
            features_live = principal_component_analysis(live_data, N)
            classifier = joblib.load(
                '/home/deepak/Major/SVM/trained_data/clf.pkl')
            preds_live = classifier.predict(features_live)
            print '--------->', preds_live

parent()
