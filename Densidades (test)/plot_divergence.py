# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 13:06:41 2018

@author: David
"""

import numpy as np
import matplotlib.pyplot as plt


#Data Loading========
data1 = np.loadtxt("Halo.txt")
data1=np.transpose(data1)

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
n_side = 120
l_side = L_box/n_side
vx_grid = np.ones([n_side, n_side])
vy_grid = np.ones([n_side, n_side])



for i in range (n_side):
    for j in range (n_side):
        print('calculo', i,j)
        min_x = i * l_side
        min_y = j * l_side

        ii = (X>min_x) & (X<min_x + l_side) & (Y>min_y) & (Y<min_y+l_side)
        
        tmp_vx = VX[ii]
        tmp_vy = VY[ii]
        tmp_m = MASS[ii]
        vx_grid[i,j] = np.sum(tmp_m * tmp_vx) / np.sum(tmp_m)
        vy_grid[i,j] = np.sum(tmp_m * tmp_vy) / np.sum(tmp_m)

        
#==========================================
def definir_divergencia(vxg,vyg):
    div=np.zeros([n_side,n_side])
    where_are_NaNs = np.isnan(vxg)
    vxg[where_are_NaNs] = 0
    where_are_NaNs = np.isnan(vyg)
    vyg[where_are_NaNs] = 0
    for i in range(n_side):
        for j in range(n_side):
            #correcciones para condiciones periodicas
            i_A=i-1
            i_B=i+1
            j_A=i-1
            j_B=j+1
            if(i_A<0):
                i_A=n_side-1
            if(j_A<0):
                j_A=n_side-1
            if(j_B==(n_side)):
                j_B=0
            if(i_B==(n_side)):
                i_B=0
        #Divergencia=flujo entrante-flujo saliente
        #Div<0 saliente; Div>0 entrante
           
            #flujo
            F_x=(vxg[i,j_A]-vxg[i,j_B])-np.abs(vxg[i,j])
            F_y=(vyg[i_B,j]-vyg[i_A,j])-np.abs(vyg[i,j])
            
            
            if(((vxg[i_A,j_A]>0) & (vyg[i_A,j_A]<0))|((vxg[i_A,j_A]<0) & (vyg[i_A,j_A]>0))):
                F_x+=vxg[i_A,j_A]
                F_y-=vyg[i_A,j_A]            
            if(((vxg[i_A,j_B]>0) & (vyg[i_A,j_B]<0))|((vxg[i_A,j_B]<0) & (vyg[i_A,j_B]>0))):
                F_x-=vxg[i_A,j_A]
                F_y-=vyg[i_A,j_A]
            if(((vxg[i_B,j_A]>0) & (vyg[i_B,j_A]<0))|((vxg[i_B,j_A]<0) & (vyg[i_B,j_A]>0))):
                F_x+=vxg[i_A,j_A]
                F_y+=vyg[i_A,j_A]
            if(((vxg[i_B,j_B]>0) & (vyg[i_B,j_B]<0))|((vxg[i_B,j_B]<0) & (vyg[i_B,j_B]>0))):
                F_x-=vxg[i_A,j_A]
                F_y+=vyg[i_A,j_A]
                
                
                
            
                
        
            
        
            div[i,j]=F_x+F_y
    return div
#========================================================00
Divergencia=definir_divergencia(vx_grid,vy_grid)
divplot=plt.figure(figsize=(10,10))
plt.imshow(Divergencia)

divplot.savefig('divergenciaOD.png')