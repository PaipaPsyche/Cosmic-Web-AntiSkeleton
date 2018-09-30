"""
Created on Wed Sep 19 17:58:04 2018

@author: david
"""
import numpy as np
import pandas as pd
from time import gmtime, strftime


#=========================================================
param=pd.read_csv("parametros.csv")
sigma_i=param["SigmaInicial"][0]
sigma_f=param["SigmaFinal"][0]
#=========================FUNCIONES=======================
def vecinos3D(ii,jj,kk,tam_r):
    ii_a=(ii-1)%tam_r
    ii_b=(ii+1)%tam_r
    jj_a=(jj-1)%tam_r
    jj_b=(jj+1)%tam_r
    kk_a=(kk-1)%tam_r
    kk_b=(kk+1)%tam_r 
    return [ii_a,ii_b,ii,ii,ii,ii],[jj,jj,jj_a,jj_b,jj,jj],[kk,kk,kk,kk,kk_a,kk_b]

def revisarVecinos(ii,jj,kk,Pertenencia,tam_r):
    xx,yy,zz=vecinos3D(ii,jj,kk,tam_r)
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


def darVacios(Pertenencia):
    return len(np.where(Pertenencia==0)[0])

#===================WATERSHED==============================

def watershed(filename,filename_out,d_tolerancia,vacios_tolerancia):
    DIV=np.load(filename)
    DIV=DIV[1:-1,1:-1,1:-1]
    tam=np.shape(DIV)[0]
    N_intervalos=20*tam
    
    div_max=round(np.amax(DIV)+5,-1)
    div_min=round(np.amin(DIV)-5,-1)
    N_intervalos=7*tam
    
    
    barridoA=np.linspace(div_max,div_min,N_intervalos)
    barrido=np.concatenate((barridoA,barridoA))
    
    tam_b=len(barrido)
    delta=barrido[0]-barrido[1]
    Pertenencia=np.zeros([tam,tam,tam])
    
    
    x_nodos=[]
    y_nodos=[]
    z_nodos=[]
    cont_nodos=1
    
    cont_iteraciones=0
    
    
    vacios=[]
    vacios.append(darVacios(Pertenencia))
    while(vacios[-1]>=vacios_tolerancia):
        print(str(round((100*vacios[-1]/(tam**3)),2)) + " % del espacio está vacio")   
        c=0
        for lev in barrido:
            if(c%360==0):
                print(str(round(c*100/tam_b,2))+" % evaluado ")
            c+=1
            cota_inf=lev
            cota_sup=lev+delta
            aa=np.where((DIV<cota_sup)&(DIV>=cota_inf)&(Pertenencia==0))
            xx,yy,zz=aa[0],aa[1],aa[2]
            rec=len(xx)
            for i in range (rec):
                x,y,z=xx[i],yy[i],zz[i]
                pert=revisarVecinos(x,y,z,Pertenencia,tam)
                if(pert!=0):
                    Pertenencia[x,y,z]=pert
                else:
                    d,ii,jj,kk=dist_nodo_cercano(x,y,z,x_nodos,y_nodos,z_nodos)
                    if(d>d_tolerancia):
                        Pertenencia[x,y,z]=cont_nodos
                        cont_nodos+=1
                        x_nodos.append(x)
                        y_nodos.append(y)
                        z_nodos.append(z)
        cont_iteraciones+=1
        vacios.append(darVacios(Pertenencia))
    aa=np.where(Pertenencia==0)
    xx,yy,zz=aa[0],aa[1],aa[2]
    rec=len(xx)
    for i in range (rec):
        d,ii,jj,kk=dist_nodo_cercano(xx[i],yy[i],zz[i],x_nodos,y_nodos,z_nodos)
        Pertenencia[xx[i],yy[i],zz[i]]=Pertenencia[ii,jj,kk]

    np.save(filename_out,Pertenencia)
    return cont_nodos-1,cont_iteraciones
    

#**********************************************************
#==========================MAIN============================
#**********************************************************
tol_vacios=300


file_stats=open("STATS.csv","w")
file_stats.write("Sigma,Parches,Iteraciones,VaciosTol,DistanciaTol,FileIN,FileOut,Time"+"\n")

for i in range(sigma_i,sigma_f+1):
    print("sigma = "+str(i))

    
    name_in="div_"+str(i)+".npy"
    name_out="pert_"+str(i)+".npy"
    nodos,it=watershed(name_in,name_out,2*i,tol_vacios)
    file_stats.write(str(i)+","+str(nodos)+","+str(it)+","+str(tol_vacios)+","+str(2*i)+","+name_in+","+name_out+","+strftime("%Y.%m.%d-%H:%M:%S", gmtime())+"\n")
file_stats.close()

file=open("INFO.txt","w")
file.write("Sigma inferior = "+str(sigma_i)+"\n")
file.write("Sigma superior = "+str(sigma_f)+"\n")
file.write("Tolerancia de vacios = "+str(tol_vacios)+"\n")
file.write("Distancia de tolerancia = 2*sigma"+"\n")
file.close()
