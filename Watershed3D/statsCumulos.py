"""
Created on Sun Sep 16 15:55:40 2018

@author: david
"""
import numpy as np
import matplotlib.pyplot as plt
#from astropy.convolution import Gaussian2DKernel,convolve
#import scipy.linalg as linalg
from mpl_toolkits.mplot3d import Axes3D

#Se  carga el archivo de pertenencia y sus respectivos datos
#se redimensiona y se definen nuevos arreglos

PERT=np.load("Pertenencia.npy")
dim=np.shape(PERT)[0]
PERT_lin=np.reshape(PERT,(dim**3))

PERT_list=list(PERT_lin)
n_parches=int(np.amax(PERT_lin))

#
###========================================================
volumen=np.zeros([n_parches,2])
for i in range(n_parches):
    volumen[i,1]=PERT_list.count(i+1)
    volumen[i,0]=i+1
sorted_vol=sorted(volumen,key = lambda x:x[1],reverse=True)
sorted_vol=np.array(sorted_vol)





n_tiles=3

plt.figure(figsize=[50,8*n_tiles])
plt.suptitle("Histogramas de masa",fontsize=30)
for i in range(n_tiles):
    plt.subplot(n_tiles,1,i+1)
    Bins=np.arange(n_parches) + 0.5
    vals,bins,ptchs=plt.hist(PERT_lin,bins=Bins,edgecolor='black', linewidth=1.2,density=True)
    n_inf=i*(n_parches/n_tiles)
    n_sup=(i+1)*(n_parches/n_tiles)
    plt.xticks(np.arange(n_inf,n_sup))
    plt.xlim(n_inf+0.5,n_sup)
    plt.ylim(0,np.amax(vals)*1.1)
    plt.xlabel("numero de cumulo",fontsize=15)
    plt.ylabel("Volumen comparativo",fontsize=15)

plt.savefig("MassHistogram.png")



n_superiores=n_parches
File=open(str(n_superiores)+"CumulosSuperiores.txt","w")
for i in range (n_superiores):
    File.write("Cumulo_"+str(int(sorted_vol[i,0]))+" "+str(sorted_vol[i,1])+"\n")
File.close()