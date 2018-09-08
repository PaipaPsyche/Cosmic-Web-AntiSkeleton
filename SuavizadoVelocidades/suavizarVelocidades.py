import numpy as np
import scipy.ndimage as scpimg

#importar el campo de velocidades
vx_grid=np.load("Vx_grid.npy")
vy_grid=np.load("Vy_grid.npy")
vz_grid=np.load("Vz_grid.npy")

n_side=np.shape(vx_grid)[0]

#convolucion gaussiana 3D
sigma=10

vx_gridConv=scpimg.filters.gaussian_filter(vx_grid,sigma)
vy_gridConv=scpimg.filters.gaussian_filter(vy_grid,sigma)
vz_gridConv=scpimg.filters.gaussian_filter(vz_grid,sigma)

vx_gridConv=np.array(vx_gridConv)
vy_gridConv=np.array(vy_gridConv)
vz_gridConv=np.array(vz_gridConv)

#escalar de flujo
def definirDivergencia(vx,vy,vz):
    div=np.zeros([n_side,n_side,n_side])
    div[1:-1,1:-1,1:-1] = (vx[:-2,1:-1,1:-1] - vx[2:,1:-1,1:-1]) + (vy[1:-1,:-2,1:-1] - vy[1:-1,2:,1:-1])+ (vz[1:-1,1:-1,:-2] - vz[1:-1,1:-1,2:])
    return div

Div=definirDivergencia(vx_gridConv,vy_gridConv,vz_gridConv)