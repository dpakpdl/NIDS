from numpy import *
import operator
from os import listdir
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from numpy.linalg import *
import scipy
from scipy.stats.stats import pearsonr
 
# load data points
raw_data = loadtxt('/home/deepak/Major/irisdataset',delimiter=',',skiprows=1)
samples,features = shape(raw_data)
  
   
#normalize and remove mean
data = mat(log10(raw_data[:,:4]))
N = 2

#function defination
def PCA (data,N):
        means = mean(data,axis=0)
        data = data - means;
                              
        # Covariance matrix
        covar = cov(data,rowvar=0)
                                       
        #eigvalues
        eigvalues,eigvectors = eig(covar)
                                                
        #sort it from big to small
        index = argsort(eigvalues)
        index = index[:-(N+1):-1]
        eigvector_sorted = eigvectors[:,index]
                                                                 
        # summary it transfor into low Dimensions 
        newdata = data*eigvector_sorted
                                                                              
        return newdata;
                                                                           
newdata = PCA(data,N)
#print newdata[0.0]                                                                           
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
colors = ['blue','red','black']
for i in xrange(samples):
        ax.scatter(newdata[i,0],newdata[i,1], color= colors[int(raw_data[i,-1])])

plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.show()
