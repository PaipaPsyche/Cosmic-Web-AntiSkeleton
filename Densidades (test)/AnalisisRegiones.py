# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 14:10:13 2018

@author: David
"""
import numpy as np
import matplotlib.pyplot as plt
from astropy.convolution import Gaussian2DKernel,convolve


reg_data=np.loadtxt("RegionMap.txt")
gauss_data=np.loadtxt("ScalarGauss.txt")
node_data=np.loadtxt("MaximumNodeMap.txt")
vxg=np.loadtxt("VectorVx.txt")
vyg=np.loadtxt("VectorVy.txt")

gaussK=Gaussian2DKernel(5)
new=convolve(gauss_data,gaussK,boundary='extend')
n_side=node_data.shape[0]

plt.figure(figsize=(16,16))

plt.subplot(2,2,1)
plt.imshow(gauss_data.T)
plt.title("Distribucion de masa")

plt.subplot(2,2,2)
plt.imshow(new.T,cmap='nipy_spectral')
plt.title("Distribucion de masa suavizada")

plt.subplot(2,2,3)
plt.imshow(node_data.T)
plt.title("Nodos de atraccion ")

plt.subplot(2,2,4)
plt.imshow(reg_data.T)
plt.title("Diferenciacion de regiones")
plt.savefig("RegionMapDiferentiation.png")



plt.figure(figsize=(10,10))
axarr=plt.axes()
plt.imshow(reg_data.T)
for i in range(n_side):
    for j in range(n_side):
        xi = i 
        yi = j 
        v_div=200
        xf = vxg[i,j]/v_div
        yf = vyg[i,j]/v_div
        axarr.arrow(xi,yi,xf,yf,head_width=0.5,head_length=0.1,fc='k',ec='k', alpha=0.5 )
plt.savefig('RegionsArrows.png')
