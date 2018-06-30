# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 12:46:08 2018

@author: David
"""

import numpy as np
import matplotlib.pyplot as plt

Vx_grid=np.loadtxt("VectorVx.txt")
Vy_grid=np.loadtxt("VectorVy.txt")
Node_grid=np.loadtxt("MaximumNodeMap.txt")

N_nodes=int(np.sum(Node_grid))
n_side=Vx_grid.shape[0]

Revisado=np.zeros([n_side,n_side])
Pertenencia=np.zeros([n_side,n_side])
Borde=np.zeros([n_side,n_side])
g=np.where(Node_grid==1)

for i in range(N_nodes):
    xnodo=g[0][i]
    ynodo=g[1][i]
    n_pertenencia=i+1
    Pertenencia[xnodo][ynodo]=n_pertenencia
    Revisado[xnodo][ynodo]=1
def revisar_vecinos(i_o,j_o,numPert):
    iA=(i_o-1)%n_side
    iB=(i_o+1)%n_side
    jA=(j_o-1)%n_side
    jB=(j_o+1)%n_side
    Fizq=Vx_grid[iA,j_o]
    Fdef=Vx_grid[iB,j_o]
    Farr=Vy_grid[i_o,jA]
    Faba=Vy_grid[i_o,JB]
#    if((Fizq>0)&(Revisado[iA,j]==0)):
        
        

    