# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 12:23:12 2018

@author: David
"""
import numpy as np
import matplotlib.pyplot as plt
from astropy.convolution import Gaussian2DKernel,convolve

gauss = np.loadtxt("ScalarGauss.txt")
n_side=gauss.shape[0]

gaussKer=Gaussian2DKernel(9)

new=convolve(gauss,gaussKer,boundary='extend')


def matmean(A):
    n=A.shape[0]
    return A.sum()/n**2


meanV=matmean(new)
new[:,:]=new[:,:]-meanV
#=================================
#definiendo puntos máximos de aciumulacion
#aca se definen (ineficientemente) los nodos máximos 

Mx=new.max()
Mn=new.min()
n_steps=500
nodes=np.zeros([2,n_side,n_side])
DensitySweep=np.linspace(Mx,0,n_steps)
for dens in DensitySweep:
    for i in range (n_side):
        for j in range (n_side):
            if(new[i,j]>=dens):
                if(nodes[0,i,j]==0):
                    ia=(i-1)%n_side
                    ib=(i+1)%n_side
                    ja=(j-1)%n_side
                    jb=(j+1)%n_side
                    
                    S1=nodes[1,ia,ja]+nodes[1,ia,j]+nodes[1,ia,jb]
                    S2=nodes[1,i,ja]+nodes[1,i,j]+nodes[1,i,jb]
                    S3=nodes[1,ib,ja]+nodes[1,ib,j]+nodes[1,ib,jb]
                    S4=nodes[0,ia,ja]+nodes[0,ia,j]+nodes[0,ia,jb]
                    S5=nodes[0,i,ja]+nodes[0,i,j]+nodes[0,i,jb]
                    S6=nodes[0,ib,ja]+nodes[0,ib,j]+nodes[0,ib,jb]
                    
                    S=S1+S2+S3+S4+S5+S6
                    if(S==0):
                        nodes[1,i,j]=1
                    nodes[0,i,j]=1

fileNodes=open("MaximumNodeMap.txt","w")
for i in range (n_side):
    for j in range (n_side):
        fileNodes.write(str(nodes[1,i,j])+" ")
    fileNodes.write("\n")
fileNodes.close()
            
        
    



plt.figure(figsize=(12,12))
plt.subplot(2,2,1)
plt.imshow(gauss.T)

plt.subplot(2,2,2)
plt.imshow(new.T)

plt.subplot(2,2,3)
plt.imshow(new.T,cmap='nipy_spectral')

plt.subplot(2,2,4)
plt.imshow(nodes[1].T,cmap='nipy_spectral')

#

