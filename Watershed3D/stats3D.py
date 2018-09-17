"""
Created on Fri Sep 14 17:16:50 2018

@author: david
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stat
import scipy.optimize as optim
#from astropy.convolution import Gaussian2DKernel,convolve
#import scipy.linalg as linalg
#from mpl_toolkits.mplot3d import Axes3D


VX_grid=np.load("Vx_grid.npy")
VY_grid=np.load("Vy_grid.npy")
VZ_grid=np.load("Vz_grid.npy")
DIV=np.load("Divergencia.npy")
tamano=np.shape(DIV)[0]

#se ingoran los bordes  pues son 0 por definición
DIV_lin=np.reshape(DIV[1:-1,1:-1,1:-1],((tamano-2)**3))
nz_box=tamano-2

minimo=np.amin(DIV_lin)
maximo=np.amax(DIV_lin)




Kurt=round(stat.kurtosis(DIV_lin),2)
#sigm=stat.si
def modelo(x,a,b,c,d):
    return a*np.exp(-((x-b)**2)/(c**2))+d
def modelo2(x,a,b,c,d):
    return a*np.exp(-b*x)*(x**c)+d

#graficar DISTRIBUCION DIVERGENCIAS==========================
plt.figure(figsize=[10,10])
vals,bins,ptchs=plt.hist(DIV_lin,bins=200,density=True)
x=np.zeros([len(vals)])
x[:]=bins[:-1]+((bins[1:]-bins[:-1])/2)

X=np.linspace(minimo-1,maximo+1,1000)
popt, pcov = optim.curve_fit(modelo,x , vals)
Y=modelo(X,popt[0],popt[1],popt[2],popt[3])
popt=np.round(popt,2)

plt.plot(X,Y,c='r',linestyle="--",linewidth=3)
plt.suptitle("Distribución de flujos",fontsize=20)
plt.title("Kurtosis = "+str(Kurt)+" , $F_{expected}$ = "+str(popt[1])+" , $\sigma$ = "+str(popt[2])+" , b = "+str(popt[3]),fontsize=15)
plt.savefig("DistFlux.png")


#Graficar DISTRIBUCION VMAG=====================================


plt.figure(figsize=[10,10])

Vmag=np.zeros([nz_box,nz_box,nz_box])
Vmag[:,:,:]=np.sqrt(VX_grid[1:-1,1:-1,1:-1]**2 + VY_grid[1:-1,1:-1,1:-1]**2 +VZ_grid[1:-1,1:-1,1:-1]**2)
Vmag=np.reshape(Vmag,(nz_box**3))
Vmag=np.sort(Vmag)
Vmag_new=Vmag[Vmag!=0]


vals,bins,ptchs=plt.hist(Vmag_new,bins=115,density=True)
expected_v=round(bins[np.where(vals==np.amax(vals))][0],2)
x=np.zeros([len(vals)])
x[:]=bins[:-1]+((bins[1:]-bins[:-1])/2)



delta=0.00005
altura_media=(np.amax(vals)/2)
xx=x[(vals<altura_media+delta) & (vals>=altura_media-delta)]
FWHM=xx[-1]-xx[0]
sigma_F=round(FWHM/2.35482,2)

sup_v=expected_v+sigma_F
inf_v=expected_v-sigma_F
vv_min=(Vmag_new<(inf_v))
vv_sup=(Vmag_new>(sup_v))
vv_in=(Vmag_new<=sup_v)&(Vmag_new>=inf_v)

perc_sup=round(len(Vmag_new[vv_sup])/len(Vmag_new),2)
perc_inf=round(len(Vmag_new[vv_min])/len(Vmag_new),2)
perc_in=round(len(Vmag_new[vv_in])/len(Vmag_new),2)
Kurt=round(stat.kurtosis(Vmag_new),2)


plt.suptitle("Distribución de Velocidad",fontsize=20)
plt.title("Kurtosis = "+str(Kurt)+" , $\sigma$ = "+str(sigma_F)+" Km/s , $V_{expected}$ = "+str(expected_v) + " Km/s",fontsize=15)
plt.plot(x,vals,c='red',linestyle="--",linewidth=3)
plt.savefig("DistVmag.png")




#fig, ax = plt.subplots()
#data = np.random.rand(1000)
#
#N, bins, patches = ax.hist(data, edgecolor='white', linewidth=1)
#
#for i in range(0,3):
#    patches[i].set_facecolor('b')
#for i in range(3,5):    
#    patches[i].set_facecolor('r')
#for i in range(5, len(patches)):
#    patches[i].set_facecolor('black')
#
#plt.show()fig, ax = plt.subplots()
#data = np.random.rand(1000)
#
#N, bins, patches = ax.hist(data, edgecolor='white', linewidth=1)
#
#for i in range(0,3):
#    patches[i].set_facecolor('b')
#for i in range(3,5):    
#    patches[i].set_facecolor('r')
#for i in range(5, len(patches)):
#    patches[i].set_facecolor('black')
#
#plt.show()



