"""
Created on Fri Sep 14 11:49:21 2018

@author: david
"""
import numpy as np
import matplotlib.pyplot as plt

#===========CARGANDO DATOS ====================
#VX_grid=np.load("Vx_grid.npy")
#VY_grid=np.load("Vy_grid.npy")
#VZ_grid=np.load("Vz_grid.npy")
DIV=np.load("Divergencia.npy")


tam = np.shape(DIV)[0]
tam_r=tam-2
DIV=DIV[1:-1,1:-1,1:-1]
#Definiendo las cotas para el barrido de watershed 
div_max=round(np.amax(DIV)+1,-1)
div_min=round(np.amin(DIV)-1,-1)
N_intervalos=10*tam_r

barridoA=np.linspace(div_max,div_min,N_intervalos)
#barridoB=np.linspace(div_min,div_max,N_intervalos/2)
barrido=np.concatenate((barridoA,barridoA))
tam_b=len(barrido)
delt=barrido[0]-barrido[1]
Pertenencia=np.zeros([tam_r,tam_r,tam_r])
Revisado=np.zeros([tam_r,tam_r,tam_r])

#=====Resultado=================================

def vecinos3D(ii,jj,kk):
    ii_a=(ii-1)%tam_r
    ii_b=(ii+1)%tam_r
    jj_a=(jj-1)%tam_r
    jj_b=(jj+1)%tam_r
    kk_a=(kk-1)%tam_r
    kk_b=(kk+1)%tam_r 
    return [ii_a,ii_b,ii,ii,ii,ii],[jj,jj,jj_a,jj_b,jj,jj],[kk,kk,kk,kk,kk_a,kk_b]

def revisarVecinos(ii,jj,kk):
    xx,yy,zz=vecinos3D(ii,jj,kk)
    tam=len(xx)
    pert=[]
    for i in range (tam):
        p_i=Pertenencia[xx[i],yy[i],zz[i]]
        pert.append(p_i)
    suma=np.sum(pert)
    if(suma==0):
        return 0
    else:
        pert=np.array(pert)
        return int(np.random.choice(pert[pert!=0]))
        


def dist_nodo_cercano(ii,jj,kk,x,y,z):
    d=np.inf
    xx=0
    yy=0
    zz=0
    for i in range (len(x)):
        dist=np.sqrt((x[i]-ii)**2+(y[i]-jj)**2+(z[i]-kk)**2)
        if (dist<d):
            d=dist
            xx=x[i]
            yy=y[i]
            zz=z[i]
    return d,xx,yy,zz
    


#Se recorre watershed hacia arriba y despues hacia abajo

#
        





d_tolerancia=30 #distancia de tolerancia minimoa entre cualesquiera 2 nodos
#
x_nodos=[]
y_nodos=[]
z_nodos=[]
cont_nodos=1


def darVacios():
    return len(np.where(Pertenencia==0)[0])

vacios=[]
vacios.append(darVacios())
while(vacios[-1]>=150):
    print(str(round((100*vacios[-1]/(tam_r**3)),2)) + " % del espacio está vacio")   
    c=0
    for lev in barrido:
        if(c%360==0):
            print(str(round(c*100/tam_b,2))+" % evaluado ")
        c+=1
        cota_inf=lev
        cota_sup=lev+delt
        aa=np.where((DIV<cota_sup)&(DIV>=cota_inf)&(Pertenencia==0))
        xx,yy,zz=aa[0],aa[1],aa[2]
        rec=len(xx)
        for i in range (rec):
            x,y,z=xx[i],yy[i],zz[i]
            pert=revisarVecinos(x,y,z)
            if(pert!=0):
                Pertenencia[x,y,z]=pert
            else:
                d,ii,jj,kk=dist_nodo_cercano(x,y,z,z_nodos,y_nodos,z_nodos)
                if(d>d_tolerancia):
                    Pertenencia[x,y,z]=cont_nodos
                    cont_nodos+=1
                    x_nodos.append(x)
                    y_nodos.append(y)
                    z_nodos.append(z)
        vacios.append(darVacios())
aa=np.where(Pertenencia==0)
xx,yy,zz=aa[0],aa[1],aa[2]
rec=len(xx)
for i in range (rec):
    d,ii,jj,kk=dist_nodo_cercano(xx[i],yy[i],zz[i],x_nodos,y_nodos,z_nodos)
    Pertenencia[xx[i],yy[i],zz[i]]=Pertenencia[ii,jj,kk]
np.save("Pertenencia",Pertenencia)




