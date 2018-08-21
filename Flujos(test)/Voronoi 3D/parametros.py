import numpy as np

data=np.loadtxt("Halo3D_300.txt")
row=data.shape[0]
col=data.shape[1]
arch=open("parametros.txt","w")
arch.write(str(row)+" "+str(col))

arch.close()

