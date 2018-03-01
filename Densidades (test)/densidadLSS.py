import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data1 = np.loadtxt("Halo1.txt", skiprows=8)
data1=np.transpose(data1)

dataX=data1[0]
dataY=data1[1]
dataZ=data1[2]
dataVx=data1[3]
dataVy=data1[4]
dataVz=data1[5]
dataM=data1[6]

Lxi=np.amin(dataX)
Lxs=np.amax(dataX)



lim=len(dataX)-1

Xseg=[]
Yseg=[]
Zseg=[]
Vxseg=[]
Vyseg=[]
Vzseg=[]
Mseg=[]

def segregar_corte_x(dx,x):
	for i in range(lim):
		xact=dataX[i]
		if((xact>=x)and(xact<=(x+dx))):
			Xseg.append(dataX[i])
			Yseg.append(dataY[i])
			Zseg.append(dataZ[i])
			Vxseg.append(dataVx[i])
			Vyseg.append(dataVy[i])
			Vzseg.append(dataVz[i])
			Mseg.append(dataM[i])
			

