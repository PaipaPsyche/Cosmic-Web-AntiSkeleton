"""
Created on Wed Sep 19 16:53:12 2018

@author: david
"""
import numpy as np
import scipy.ndimage as scpimg
import pandas as pd



VX=np.load("Vx_grid.npy")
VY=np.load("Vy_grid.npy")
VZ=np.load("Vz_grid.npy")
n_side=np.shape(VX)[0]


param=pd.read_csv("parametros.csv")
sigma_i=param["SigmaInicial"][0]
sigma_f=param["SigmaFinal"][0]


#convolucion gaussiana 3D

#escalar de flujo


def DivergenciaSigma(vx,vy,vz,sigma):
    vx_conv=scpimg.filters.gaussian_filter(vx,sigma)
    vy_conv=scpimg.filters.gaussian_filter(vy,sigma)
    vz_conv=scpimg.filters.gaussian_filter(vz,sigma)
    
    vx_gridConv=np.array(vx_conv)
    vy_gridConv=np.array(vy_conv)
    vz_gridConv=np.array(vz_conv)
    
    div=np.zeros([n_side,n_side,n_side])
    div[1:-1,1:-1,1:-1] = (vx_gridConv[:-2,1:-1,1:-1] - vx_gridConv[2:,1:-1,1:-1]) + (vy_gridConv[1:-1,:-2,1:-1] - vy_gridConv[1:-1,2:,1:-1])+ (vz_gridConv[1:-1,1:-1,:-2] - vz_gridConv[1:-1,1:-1,2:])
    
    name="div_"+str(sigma)+".npy"
    np.save(name,div)
    
    

    
for i in range(sigma_i,sigma_f+1):
    DivergenciaSigma(VX,VY,VZ,i)
    
    










