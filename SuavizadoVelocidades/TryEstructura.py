"""
Created on Tue Sep 11 14:11:44 2018

@author: david
"""
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib
#from astropy.convolution import Gaussian2DKernel,convolve
#import scipy.linalg as linalg
from mpl_toolkits.mplot3d import Axes3D



div=np.load("Divergencia.npy")
maximo_div=np.amax(div)
minimo_div=0


#structure [patches,voids]
def plotStructure( umbral,filename, structure="patches"):
    x,y,z=[[],[],[]]
#    struc="Patch"
    if(structure=="patches"):
        x,y,z=np.where(div>umbral)
    else:
        x,y,z=np.where(div<umbral)
#        struc="Voids"
    fig=plt.figure(figsize=[12,12])
    ax=fig.add_subplot(111,projection='3d')
    cm = plt.cm.get_cmap('jet')
#    normalize = matplotlib.colors.Normalize(vmin=minimo_div, vmax=maximo_div)
#    colors = [cmap(normalize(value)) for value in div]
    ax.scatter([0,120],[0,120],[0,120],c='k',s=0.1)
    plt.xlabel("$10^7$ Pc",fontsize=15)
    plt.ylabel("$10^7$ Pc",fontsize=15)
#    plt.zlabel("$10^5$ Pc")
    sc= ax.scatter(x , y , z , c=div[x,y,z], vmin=minimo_div ,vmax=maximo_div , s=0.6 ,cmap=cm,alpha=0.4)
    
    plt.colorbar(sc)
#    cax, _ = matplotlib.colorbar.make_axes(ax)
#    cbar = matplotlib.colorbar.ColorbarBase(cax, cmap=cmap, norm=normalize)
    fig.savefig(filename)

#plotStructure(40,"prueba.png",structure="patches")

z=55
for i in range (20):
    fn="IMGestructura_"+str(i+1)+".png"
    plotStructure(z,fn,structure="patches")
    z=z-2

    
#    
#
