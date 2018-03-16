import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#from scipy.stats import gaussian_kde

#Data Loading========
data1 = np.loadtxt("input_slice.dat", skiprows=8)
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

X, Y, Z,VX, VY, VZ, MASS = segregar_corte_z(dataX, dataY, dataZ, dataVx, dataVy, dataVz, dataM, 200,10)

L_box  = 1200
n_side = 80
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
plt.figure(figsize=(10, 10))
axARR=plt.axes()

for i in range(n_side):
    for j in range(n_side):
        print('plot', i,j)
        xi = i * l_side
        yi = j * l_side
        xf = vx_grid[i,j]/20
        yf = vy_grid[i,j]/20
        axARR.arrow(xi,yi,xf,yf,head_width=10,head_length=10,fc='k',ec='k')

plt.xlim([0,1200])
plt.ylim([0,1200])
plt.savefig('arrows.png')


