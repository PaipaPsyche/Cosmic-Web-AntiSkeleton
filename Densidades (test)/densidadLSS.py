import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
#============================
#Limits definition
Lzi=np.amin(np.ceil(dataZ))
Lzs=np.amax(np.ceil(dataZ))
lim=len(dataZ)-1
#============================
#Segregating 
Xseg=[]
Yseg=[]
Zseg=[]
Vxseg=[]
Vyseg=[]
Vzseg=[]
Mseg=[]

def segregar_corte_z(z,dz):
	for i in range(lim):
		zact=dataZ[i]
		if((zact>z)&(zact<(z+dz))):
			Xseg.append(dataX[i])
			Yseg.append(dataY[i])
			Zseg.append(dataZ[i])
			Vxseg.append(dataVx[i])
			Vyseg.append(dataVy[i])
			Vzseg.append(dataVz[i])
			Mseg.append(dataM[i])
#============================
segregar_corte_z(200,10)
#============================
#graph
fig=plt.figure(figsize=(10,10))
ax=Axes3D(fig)
ax.set_zlim(Lzi,Lzs)
ax.scatter(Xseg,Yseg,Zseg,c='b',s=0.3,depthshade=False)
segregar_corte_z(1000,10)
ax.scatter(Xseg,Yseg,Zseg,c='g',s=0.3,depthshade=False)
#Graphing 2 slides
ax.set_xlabel("eje X")
ax.set_ylabel("eje Y")
ax.set_zlabel("eje Z")
fig.savefig('secton3D.png')
#============================
#graph of the cut
figP=plt.figure(figsize=(10,10))
ax2D = figP.gca()
ax2D.set_xticks(np.arange(0, 1260, 60))
ax2D.set_yticks(np.arange(0, 1260,60))
plt.scatter(Xseg,Yseg,s=0.4)
plt.xlabel("eje X")
plt.ylabel("eje Y")
plt.grid()
figP.savefig('secton2D.png')
#============================
#NEXT: sectionate the 2D cut into pixels with density data and CM velocity.
#============================

#============================


