import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#from scipy.stats import gaussian_kde

#Data Loading========
data1 = np.loadtxt("HaloListV.0136.0001.DAT", skiprows=8)
data1=np.transpose(data1)

dataX=data1[0]
dataY=data1[1]
dataZ=data1[2]
dataVx=data1[3]
dataVy=data1[4]
dataVz=data1[5]
dataM=data1[6]

def segregar_corte_z(x, y, z, minz, dz):
	ii = (z>minz) & (z<(minz+dz))
	return x[ii], y[ii], z[ii]
#============================
X, Y, Z = segregar_corte_z(dataX, dataY, dataZ, 200,10)


#2D densitiy 
figD=plt.figure(figsize=(10,10))
plt.hist2d(X,Y,bins=30)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Density of 2D Cut in Z axis ", fontsize=20)
figD.savefig("Density2D-30b.png")
