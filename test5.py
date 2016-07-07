
# attributes in our dataset CSIC 2010
attributes= ["Host","Content-Length","Length1"]

dictionary={}
dictionary['Host']='localhost'

for k in attributes:
    if k not in dictionary:
        dictionary[k]=0
   
for key in dictionary:
    print key,": ", dictionary[key]


