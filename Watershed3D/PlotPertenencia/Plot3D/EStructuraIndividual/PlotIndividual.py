"""
Created on Mon Sep 17 02:12:12 2018

@author: david
"""
import numpy as np
import matplotlib.pyplot as plt
#import imageio as imio
#from astropy.convolution import Gaussian2DKernel,convolve
#import scipy.linalg as linalg
from mpl_toolkits.mplot3d import Axes3D

DIV=np.load("Divergencia.npy")
PERT=np.load("Pertenencia.npy")
DIV=DIV[1:-1,1:-1,1:-1]
tam=np.shape(DIV)[0]
div_max=np.amax(DIV)
div_min=np.amin(DIV)
n_parches=np.amax(PERT)

#N=8
#cumulos=np.random.randint(1,20,10)
cumulos=[3]
umbral=-40

names=["Cronos","Rea","Poseidon","Hades","Zeus"]

fig=plt.figure(figsize=[12,12])
ax=fig.add_subplot(111,projection='3d')

for i in range (len(cumulos)):
    xx,yy,zz=np.where((DIV>umbral)&(PERT==cumulos[i]))
    cm = plt.cm.get_cmap('prism')
    ax.scatter([0,120],[0,120],[0,120],c='k',s=0.1)
    plt.xlabel("$10^7$ Pc",fontsize=15)
    plt.ylabel("$10^7$ Pc",fontsize=15)
    sc= ax.scatter(xx,yy,zz , c=PERT[xx,yy,zz], vmin=0 ,vmax=np.amax(cumulos) , s=0.6 ,cmap=cm,alpha=0.4)
  #  sc.set_label("Cumulo "+str(cumulos[i]))
    sc.set_label(names[i])
plt.legend(fontsize="large",markerscale=10)    
#plt.colorbar(sc)
fig.savefig("CumulosIndividalesRand.png")