"""
Created on Sun Sep 16 13:54:17 2018

@author: david
"""
import numpy as np
import matplotlib.pyplot as plt
import imageio as imio
PERT=np.load("Pertenencia.npy")
 
n_side=np.shape(PERT)[0]
p_min=np.amin(PERT)
p_max=np.amax(PERT)
z_sweep=np.arange(n_side)


images=[]
for i in z_sweep:
    pert=np.zeros([n_side,n_side])
    pert[:,:]=PERT[:,:,i]
    
    fig=plt.figure(figsize=[12,12])
    ax=fig.add_subplot(111)
    cm = plt.cm.get_cmap('jet')
    plt.xlabel("$10^7$ Pc",fontsize=15)
    plt.ylabel("$10^7$ Pc",fontsize=15)
    sc= ax.imshow(pert, cmap="jet", vmin=p_min ,vmax=p_max)
    plt.colorbar(sc)
    name="PlotPert_"+str(i)+".png"
    plt.savefig(name)
    images.append(imio.imread(name))
    
imio.mimsave("Pertenencia.gif",images)