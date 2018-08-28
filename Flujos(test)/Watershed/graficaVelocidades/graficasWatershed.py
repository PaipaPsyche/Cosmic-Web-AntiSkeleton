import numpy as np
import matplotlib.pyplot as plt


Parches=(np.loadtxt("pertenencia.txt")).T
Vx_data=np.loadtxt("VectorVx.txt")
Vy_data=np.loadtxt("VectorVy.txt")
n_side=int(Parches.shape[0])



plt.figure(figsize=(15, 15))
plt.imshow(Parches)
axARR=plt.axes()
Vmin=110
for i in range(n_side):
    print('plot', i)
    for j in range(n_side):
        modular=2
        if((i%modular==0)&(j%modular==0)):
            v_divx=np.abs(50*np.log10(np.abs(Vx_data[i,j])))+0.01
            v_divy=np.abs(50*np.log10(np.abs(Vy_data[i,j])))+0.01
            xf = Vx_data[i,j]/v_divx
            yf = Vy_data[i,j]/v_divy
            axARR.arrow(i,j,xf,yf,head_width=0.5,head_length=0.5,fc='k',ec='k')
plt.savefig("parchesVelocidades.png")