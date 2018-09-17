"""
Created on Mon Sep 17 00:11:42 2018

@author: david
"""
import numpy as np
import matplotlib.pyplot as plt
import imageio as imio
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

n_imagenes=30
umbral=15





delta=(div_max-umbral)/n_imagenes
images=[]

for i in range (n_imagenes):
    cota_inf=(div_max-(i*delta))-delta
    
    xx,yy,zz=np.where(DIV>cota_inf)
    fig=plt.figure(figsize=[24,12])
    
    ax1=fig.add_subplot(1,2,1,projection='3d')
    cm = plt.cm.get_cmap('prism')
    ax1.scatter([0,120],[0,120],[0,120],c='k',s=0.1)
    plt.xlabel("$10^7$ Pc",fontsize=15)
    plt.ylabel("$10^7$ Pc",fontsize=15)
    sc= ax1.scatter(xx,yy,zz , c=PERT[xx,yy,zz], vmin=0 ,vmax=n_parches , s=0.6 ,cmap=cm,alpha=cota_inf/div_max)
    plt.colorbar(sc)
    
    ax2=fig.add_subplot(1,2,2,projection='3d')
    cm = plt.cm.get_cmap('jet')
    ax2.scatter([0,120],[0,120],[0,120],c='k',s=0.1)
    plt.xlabel("$10^7$ Pc",fontsize=15)
    plt.ylabel("$10^7$ Pc",fontsize=15)
    sc= ax2.scatter(xx,yy,zz , c=DIV[xx,yy,zz], vmin=umbral ,vmax=div_max , s=0.6 ,cmap=cm,alpha=0.4)
    plt.colorbar(sc)
    
    
    
    name="umbral"+str(umbral)+"_IM"+str(i)+".png"
    plt.savefig(name)
    images.append(imio.imread(name)) 

imio.mimsave("PertEstructura.gif",images)







#################################

