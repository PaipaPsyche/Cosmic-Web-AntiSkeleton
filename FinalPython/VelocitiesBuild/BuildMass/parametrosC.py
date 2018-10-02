"""
Created on Mon Oct  1 10:08:50 2018

@author: david
"""
import numpy as np

data=np.loadtxt("HaloMassCpt.txt")
row=data.shape[0]
col=data.shape[1]
arch=open("parametros.txt","w")
arch.write(str(row)+" "+str(col))

arch.close()
