# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 13:06:41 2018

@author: David
"""

import numpy as np
import matplotlib.pyplot as plt
from astropy.convolution import Gaussian2DKernel,convolve




#Data Loading========
data1 = np.loadtxt("Halo.txt")
data1=np.transpose(data1)


prints=0#Define si se hacen los prints de calculo y plot

dataX=data1[0]
dataY=data1[1]
dataZ=data1[2]
dataVx=data1[3]
dataVy=data1[4]
dataVz=data1[5]
dataM=data1[6]
Mseg=[]


def segregar_corte_z(x, y, z, vx, vy, vz, mass, minz, dz):
	ii = (z>minz) & (z<(minz+dz))
	return x[ii], y[ii], z[ii], vx[ii], vy[ii], vz[ii], mass[ii]

X, Y, Z,VX, VY, VZ, MASS = segregar_corte_z(dataX, dataY, dataZ, dataVx, dataVy, dataVz, dataM, 80,10)

L_box  = 1200
n_side = 100
l_side = L_box/n_side
vx_grid = np.zeros([n_side, n_side])
vy_grid = np.zeros([n_side, n_side])



for i in range (n_side):
    print('calculo ',i)
    for j in range (n_side):

        min_x = i * l_side
        min_y = j * l_side

        ii = (X>min_x) & (X<min_x + l_side) & (Y>min_y) & (Y<min_y+l_side)
        
        tmp_vx = VX[ii]
        tmp_vy = VY[ii]
        tmp_m = MASS[ii] 
        masa_total = np.sum(tmp_m) + 1E-10
        vx_grid[i,j] = np.sum(tmp_m * tmp_vx) / masa_total
        vy_grid[i,j] = np.sum(tmp_m * tmp_vy) / masa_total

        
#==========================================
def definir_divergencia(vxg,vyg):
    div=np.zeros([n_side,n_side])
    div[1:-1,1:-1] = (vxg[:-2,1:-1] - vxg[2:,1:-1]) + (vyg[1:-1,:-2] - vyg[1:-1,2:])
    return div

def puntos_criticos(div,Vmax,Vmin):
    PuntosC=np.zeros([n_side,n_side])
    ii=(div<=Vmin)
    jj=(div>Vmax)
    
    PuntosC[ii]=-1
    PuntosC[jj]=1
    return PuntosC


    
#========================================================00
Divergencia=definir_divergencia(vx_grid,vy_grid)
divplot=plt.figure(figsize=(10,10))
plt.imshow(Divergencia.T)

axARR=plt.axes()
Dlim=220
Dmin=Dlim
Dmax=Dlim
PC=puntos_criticos(Divergencia,Dmax,Dmin)

for i in range(n_side):
    print('plot ',i)
    for j in range(n_side):
        
        xi = i 
        yi = j 
        v_div=200
        xf = vx_grid[i,j]/v_div
        yf = vy_grid[i,j]/v_div
        axARR.arrow(xi,yi,xf,yf,head_width=0.5,head_length=0.1,fc='k',ec='k', alpha=0.5 )
        

divplot.savefig('divergenciaOD.png')


CPplot=plt.figure(figsize=(10,10))
axPC=plt.axes()
plt.imshow(PC.T)
for i in range(n_side):
    for j in range(n_side):
        xi = i 
        yi = j 
        v_div=200
        xf = vx_grid[i,j]/v_div
        yf = vy_grid[i,j]/v_div
        axPC.arrow(xi,yi,xf,yf,head_width=0.5,head_length=0.1,fc='k',ec='k', alpha=0.5 )



CPplot.savefig("PuntosCriticos.png")
gauss=Gaussian2DKernel(3)
    
    



