import numpy as np
import matplotlib.pyplot as plt
#from scipy.stats import gaussian_kde

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


def dar_puntos_quietos(vxg,vyg,dv):
    pc=np.zeros([n_side,n_side])
    
    for i in range (n_side):
        for j in range (n_side):
            x=vxg[i,j]
            y=vyg[i,j]
            speed=np.sqrt((x*x)+(y*y))
            if(speed<=dv):
                 pc[i,j]=1
#                
            
    return pc


        
            
                
#===================================
plt.figure(figsize=(10, 10))
axARR=plt.axes()
Vmin=110
for i in range(n_side):
    for j in range(n_side):
        print('plot', i,j)
        xi = i * l_side
        yi = j * l_side
        v_div=20
        xf = vx_grid[i,j]/v_div
        yf = vy_grid[i,j]/v_div
        axARR.arrow(xi,yi,xf,yf,head_width=5,head_length=10,fc='k',ec='k')
        
        
plt.xlim([0,1200])
plt.ylim([0,1200])
plt.savefig('arrowspoints.png')   
 


