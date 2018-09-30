"""
Created on Wed Sep 26 10:27:53 2018

@author: david
"""
import numpy as np
import matplotlib.pyplot as plt
#from astropy.convolution import Gaussian2DKernel,convolve
#import scipy.linalg as linalg
#from mpl_toolkits.mplot3d import Axes3D

#Datos relevantes
L_box  = 1200
n_side = 120
#cargando datos 
data1 = np.loadtxt("HaloCpt.txt")
data1=np.transpose(data1)


# cargando variables (arreglos)
X=np.array(data1[0])
Y=np.array(data1[1])
Z=np.array(data1[2])
M=np.array(data1[6])

l_side = int(L_box/n_side)



m_grid = np.ones([n_side, n_side, n_side])


for i in range (n_side):
    for j in range (n_side):
        print("calculo",i,j)
        for k in range(n_side):
            min_x = i * l_side
            min_y = j * l_side
            min_z = k * l_side
            ii = (X>min_x) & (X<min_x + l_side) & (Y>min_y) & (Y<min_y+l_side)& (Z>min_z) & (Z<min_z+l_side)
            

            tmp_m = M[ii]k,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,76y6yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
            
            m_grid[i,j,k] = np.sum(tmp_m)
            
np.save("M_grid",m_grid)
