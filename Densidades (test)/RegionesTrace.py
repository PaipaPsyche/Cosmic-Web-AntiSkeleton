# -*- coding: utf-8 -*-
"""
Created on Wed May 16 22:50:57 2018

@author: David
"""

import numpy as np
import matplotlib.pyplot as plt

nodes = np.loadtxt("MaximumNodeMap.txt")
vxg = np.loadtxt("VectorVx.txt")
vyg = np.loadtxt("VectorVy.txt")
n_side=nodes.shape[0]

N_nodes=int(nodes.sum())

class pixel:
    dimension=n_side
    def __init__(self,x,y,vx,vy,es_nodo):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.check=0
        self.group=0
        self.source=es_nodo
        self.up=0
        self.down=0
        self.left=0
        self.right=0

        
    def revisado(self):
        self.check=1
    def asignar(self,g):
        self.group=g
#    def dar_vecinos(self):
#        i_a=x-1
#        i_b=x+1
#        j_a=y-1
#        j_b=y+1
#        if(i_a==n_side):
#            i_a=n_side
#    
pixeles=[]

def encontrar(xx,yy,pixeles):
    found=''
    for pix in pixeles:
        if((pix.x==xx) & (pix.y==yy)):
            found=pix
    return found
            

for i in range (n_side):
    for j in range (n_side):
        pix=pixel(i,j,vxg[i,j],vyg[i,j],nodes[i,j])
        pixeles.append(pix)
for i in range (n_side):
    for j in range (n_side):
        IA=(i-1)%n_side
        IB=(i+1)%n_side
        JA=(j-1)%n_side
        JB=(j+1)%n_side
        pix=encontrar(i,j,pixeles)
        pix.down=encontrar(i,JA,pixeles)
        pix.up=encontrar(i,JB,pixeles)
        pix.left=encontrar(IA,j,pixeles)
        pix.right=encontrar(IB,j,pixeles)
        
        

            
        