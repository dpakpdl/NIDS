#!/usr/bin/python

import matplotlib.pyplot as plt
from pca import principal_component_analysis
from display import prettyPicture
from numpy import *
import operator
from numpy import inf
from os import listdir
import numpy as np
# load training data points
raw_data = loadtxt('/home/deepak/Major/nrmlTffTrngMdfd.txt',delimiter=' ', skiprows=1)
samples,features = shape(raw_data)

#load testing data points
raw_data2 = loadtxt('/home/deepak/Major/SVM/anomalousTrafficTestModified.txt',delimiter=' ', skiprows=1)
samples2,features2 = shape(raw_data2)

#normalize and remove mean
traindata = mat(log10(raw_data[:,:5]))
testdata = mat(log10(raw_data2[:,:5]))
N = 2
if np.isnan(traindata).any():
	traindata = np.nan_to_num(traindata)
elif np.isinf(traindata).any():
	traindata[traindata == -inf] = 0

if np.isnan(testdata).any():
	testdata = np.nan_to_num(testdata)
elif np.isinf(testdata).any():
	testdata[testdata == -inf] = 0
	
features_train, labels_train = principal_component_analysis (traindata,N)
features_test, labels_test = principal_component_analysis (testdata,N)


### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
var_y_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
var_x_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
var_y_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
var_x_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]



from sklearn import svm

### create classifier
#clf = svm.SVC(C=1000, gamma = 0.4)#TODO
clf = joblib.load('/home/deepak/Major/SVM/trained_data/clf.pkl')

### fit the classifier on the training features and labels
clf.fit(features_train,labels_train)#TODO

### use the trained classifier to predict labels for the test features
pred = clf.predict(features_test)#TODO


### calculate and return the accuracy on the test data
### this is slightly different than the example, 
### where we just print the accuracy
### you might need to import an sklearn module
accuracy = clf.score(features_test,labels_test)#TODO
print accuracy

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
