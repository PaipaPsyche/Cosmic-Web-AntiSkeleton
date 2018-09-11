"""
Created on Mon Sep 10 16:20:34 2018

@author: david
"""
import numpy as np
import matplotlib.pyplot as plt
#from astropy.convolution import Gaussian2DKernel,convolve
#import scipy.linalg as linalg
#from mpl_toolkits.mplot3d import Axes3D

vx_grid=np.load("Vx_grid.npy")
vy_grid=np.load("Vy_grid.npy")
vz_grid=np.load("Vz_grid.npy")

n_side=len(vx_grid)

#
#def segregarCorteZ(z_o,delta_z=10):
#    VX=vx_grid[:,:,z_o:z_o+delta_z]
#    VY=vy_grid[:,:,z_o:z_o+delta_z]
#    
#    vx=np.zeros([n_side,n_side])
#    vy=np.zeros([n_side,n_side])
#
#    for i in range (delta_z):
#        vx[:,:]=vx[:,:]+VX[:,:,i]
#        vy[:,:]=vx[:,:]+VY[:,:,i]   
#    return vx , vy 
#
#VX,VY=segregarCorteZ(0)
#
#
#
#
#
#
#
#
#
#def plotTajadaZ(z_o,delta_z=10):
#    vx , vy = segregarCorteZ(z_o,delta_z)
#    
#    
#    plot=plt.figure(figsize=[10,10])
#    axARR=plt.axes()
#    plt.xlim(0,n_side)
#    plt.ylim(0,n_side)
#    for i in range(n_side):
#        print('plot ',i)
#        for j in range(n_side):
#            xi = i 
#            yi = j 
#            v_div=50
#            xf = vx[i,j]/v_div
#            yf = vy[i,j]/v_div
#            axARR.arrow(xi,yi,xf,yf,head_width=0.5,head_length=0.1,fc='k',ec='k', alpha=0.5 )
#    plot.savefig("plotTajadaZ"+str(int(z_o))+".png")
#    
#plotTajadaZ(30)
###    
###    
###
#
#plotTajadaZ(80,vx_grid,vy_grid)
  
#    for  i in range (n_side):
#        for j in range (n_side):
#            vyi=vy[x_o,i,j]
#            vzi=vz[x_o,i,j]
    
    
    
    
    
    