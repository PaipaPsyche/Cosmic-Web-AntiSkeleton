# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 12:15:57 2018

@author: David
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as linalg
from astropy.convolution import Gaussian2DKernel,convolve


#===========================
#crea la matriz de probabilidades y adquiere coordenadas
#de los puntos criticos
nodes = np.loadtxt("MaximumNodeMap.txt")
vxg = np.loadtxt("VectorVx.txt")
vyg = np.loadtxt("VectorVy.txt")
n_side=nodes.shape[0]

N_nodes=int(nodes.sum())
NodeList=np.zeros([2,N_nodes])
Probabilty=np.zeros([N_nodes,n_side,n_side])
count=0
for i in range(n_side):
    for j in range(n_side):
        if(nodes[i,j]==1):
            Probabilty[count,i,j]=1
            NodeList[0,count]=i
            NodeList[1,count]=j
            count+=1
#================================
#se define distancia como atenunate de probabilidad
#asigna un coeficiente entre 0 y 1 que describe que 
#cerca se encuentran 2 puntos y un coeficiente de ganancia
def CoeficienteDistancia(i1,j1,i2,j2):
    x=np.abs(i1-i2)
    y=np.abs(j1-j2)
    d=np.sqrt(x*x+y*y)
    return 1-(d/(np.sqrt(2)*(n_side-1)))
#define que tanto el punto de interes se acerca al nodo actual
def CoeficienteDireccionalidad(i1,j1,i2,j2):
    res=0
    if((i1==i2)&(j1==j2)):
        res=1
    else:
        a=[i2-i1,j2-j1]
        b=[vxg[i2,j2],vyg[i2,j2]]
        na=linalg.norm(a)
        nb=linalg.norm(b)
        Cos=np.vdot(a,b)/(na*nb+0.0000001)
        res=(1-Cos)/2
    return res

GainDist=0.01
GainDir=1-GainDist

def CoeficiennteProbabilidad(i1,j1,i2,j2):
    dist=CoeficienteDistancia(i1,j1,i2,j2)
    direc=CoeficienteDireccionalidad(i1,j1,i2,j2)
    return GainDist*dist+GainDir*direc




for n in range(N_nodes):
    i_n=NodeList[0,n]
    j_n=NodeList[1,n]
    for i in range (n_side):
        for j in range(n_side):
            Probabilty[n,i,j]=CoeficiennteProbabilidad(i_n,j_n,i,j)

            
regiones=np.zeros([n_side,n_side])

for i in range(n_side):
    for j in range(n_side):
        higher=0
        reg=0
        for n in range(N_nodes):
            p=Probabilty[n,i,j]
            if(p>higher):
                higher=p
                reg=n
        regiones[i,j]=reg*5


gaussK=Gaussian2DKernel(0.5)
new=convolve(regiones,gaussK,boundary='extend')
new=new.round()

fileR=open("RegionMap.txt","w")
for i in range (n_side):
    for j in range (n_side):
        fileR.write(str(regiones[i,j])+" ")
    fileR.write("\n")
fileR.close()


plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(new.T,cmap='jet')
plt.subplot(1,2,2)
plt.imshow(nodes.T)



            
           
            
            
