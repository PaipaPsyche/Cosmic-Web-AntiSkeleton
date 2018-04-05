import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#from scipy.stats import gaussian_kde

#Data Loading========
data1 = np.loadtxt("Halo1.txt", skiprows=8)
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
n_side = 100
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
            ax=vxg[i,j_A]
            bx=vxg[i,j_B]
            ay=vyg[i_A,j]
            by=vyg[i_B,j]
            vx=vxg[i,j]
            vy=vyg[i,j]
            #flujo
            F_x=(ax-bx)-np.abs(vx)
            F_y=(by-ay)-np.abs(vy)
            
        
            div[i,j]=F_x+F_y
    return div
        
        
            
                
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
 
Divergencia=definir_divergencia(vx_grid,vy_grid)
plt.figure(figsize=(10,10))
plt.matshow(Divergencia)
plt.savefig('divergencia.png')

