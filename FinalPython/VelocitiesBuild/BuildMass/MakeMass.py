"""
Created on Tue Oct  2 01:10:08 2018

@author: david
"""
import numpy as np
import matplotlib.pyplot as plt


DATA=np.loadtxt("grid3D.txt").T



n_side=int(round(np.cbrt(np.shape(DATA)[1])))
l_data=np.shape(DATA)[1]

ii=DATA[0,:]
jj=DATA[1,:]
kk=DATA[2,:]
mm=DATA[3,:]

mass_grid=np.zeros([n_side,n_side,n_side])

for l in range(l_data):
    x,y,z=int(ii[l]),int(jj[l]),int(kk[l])
    print(x)
    mass_grid[x,y,z]=mm[l]

np.save("MassGrid.npy",mass_grid)

