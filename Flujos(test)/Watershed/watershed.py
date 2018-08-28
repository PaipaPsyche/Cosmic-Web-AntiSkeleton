import numpy as np
import matplotlib.pyplot as plt

Data=np.loadtxt("ScalarGauss.txt")
nodos=np.loadtxt("MaximumNodeMap.txt")
n_nodos=len(np.where(nodos==1)[0])
n_side=int(Data.shape[0])


valor_max=0
valor_min=0
cuenta_datos=n_side*n_side
pertenencia=np.zeros([n_side,n_side])


precoord=np.where(nodos==1)
for i in range(n_nodos):
    x=precoord[0][i]
    y=precoord[1][i]
    pertenencia[x,y]=i+1
#        print(x,y,i+1)

def extraccionParametros():
	maxval=0
	minval=0
	
	for line in Data:
		for element in line:
			
			#print(element)
			if(element>maxval):
				maxval=element
			if(element<minval):
				minval=element
		
	return maxval,minval
def printMatrix(M):
	plt.figure(figsize=[12,12])
	plt.imshow(M)
	plt.savefig("printedMatrix.png")
##printMatrix(pertenencia)			


valor_max,valor_min=extraccionParametros()
#definirCondicionesIniciales()	
delta=(valor_max-valor_min)/cuenta_datos
barrido_watershed=np.linspace(valor_max+(2*delta),valor_min-(2*delta),int(cuenta_datos/2))

#print(valor_max,valor_min,delta)
#print(barrido_watershed)


def sup(n):
	return (n+1)%n_side
def inf(n):
	return(n-1)%n_side

def elegirMasCercano(ii,jj):
    dmenor=cuenta_datos
    xmen=0
    ymen=0
    
    for i in range(n_nodos):
        x=precoord[0][i]
        y=precoord[1][i]
        d=np.sqrt((y-jj)**2 + (x-ii)**2)
        
        if(d<dmenor):
            dmenor=d
            xmen=x
            ymen=y
            
    return pertenencia[xmen,ymen]


def revisarPertenenciaVecinos(ii,jj):


    i_a=inf(ii)
    i_b=sup(ii)
    j_a=inf(jj)
    j_b=sup(jj)
    vecinos=[]
    arr=pertenencia[i_a,jj]
    abb=pertenencia[i_b,jj]
    izq=pertenencia[ii,j_a]
    der=pertenencia[ii,j_b]
    vecinos.append(arr)
    vecinos.append(abb)
    vecinos.append(izq)
    vecinos.append(der)
#    print(arr,abb,izq,der)
    suma=arr+abb+izq+der
#    print(suma)
        	
    if(suma==0):
        c=elegirMasCercano(ii,jj)
        print("choice rand "+str(c))
        return c,1
    else:
        nz=[]
        for elem in vecinos:
            if (elem!=0):
                nz.append(elem)
        p=np.random.choice(nz)
        print("choice "+str(p))
        return p,0
#    		
#print(revisarPertenenciaVecinos(92,132))	
#print(elegirMasCercano(92,130))

#	===============================================
# PRIMER INTENTO PROPAGAR
#===================================================
#def propagar():
#    cota_inf=0
#    cota_sup=0
#    for nivel in range(len(barrido_watershed)-1):
#        if(nivel%200==0):
#            print(str(int(nivel*100/(len(barrido_watershed)-1)))+"%")
#        cota_sup=barrido_watershed[nivel]
#        cota_inf=barrido_watershed[nivel+1]
#        for i in range(n_side):
#            for j in range(n_side):
#                if(pertenencia[i,j]==0):
#                    if((Data[i,j]>=cota_inf)and(Data[i,j]<cota_sup)):    
#                        pertenencia[i,j]=revisarPertenenciaVecinos(i,j)


#	===============================================
# SEGUNDO INTENTO PROPAGAR
#===================================================
def contarPixelesNoIdentificados(cinf,csup):
    iii=(Data>cinf)&(Data<=csup)&(pertenencia==0)
    return (sum(sum(iii)))



def propagar():
    total=0
    contador=0
    cota_inf=0
    cota_sup=0
    for nivel in range(len(barrido_watershed)-1):
        if(nivel%600==0):
            print("=======================   "+str(int(nivel*100/(len(barrido_watershed)-1)))+"%   ============================")
        cota_sup=barrido_watershed[nivel]
        cota_inf=barrido_watershed[nivel+1]
        
        vacios=contarPixelesNoIdentificados(cota_inf,cota_sup)
        
        while(vacios!=0):
            for i in range (n_side):
                for j in range(n_side):
                    if((pertenencia[i,j]==0)&(Data[i,j]<=cota_sup)&(Data[i,j]>cota_inf)):
                        pertenencia[i,j],cont=revisarPertenenciaVecinos(i,j)
                        total+=1
                        contador+=cont
                        
            vacios=contarPixelesNoIdentificados(cota_inf,cota_sup)
    return contador/total
#        iii=(Data<=valor_max)&(Data>cota_inf)&(pertenencia==0)
#        kk=sum(sum(iii))
#        print("kk=",kk) 
#        while(kk!=0):
#            for i in range(n_side):
#                for j in range(n_side):
#                    if(pertenencia[i,j]==0):
#                        pertenencia[i,j]=revisarPertenenciaVecinos(i,j)
#            iii=(Data<=valor_max)&(Data>cota_inf)&(pertenencia==0)
#            kk=sum(sum(iii))
        
perc=propagar()
#ss=propagar()
#print(sum(ss))
#plt.hist(ss)
#
plt.figure(figsize=[12,12])
#plt.subplot(2,1,1)
#propagar()
plt.imshow(pertenencia)
#plt.subplot(2,1,2)
#propagar()
#plt.imshow(pertenencia)
porcentajeAleatorio=perc*100
plt.title("matriz de pertenencia ( "+str(porcentajeAleatorio) +" % aleatorio)")
plt.savefig("Pertneencia.png")

#def hayZero(M):
#	r=False
#	for line in M:
#		for element in line:
#			if(element==0):
#				r=True
#	return r
#
#k=0
#while(k<(n_side**2)):
#    k+=1
#    print(k)
#    propagar()					
#		
#		
#
#	
#
##print(a)
##print(b)
##print(c)
##print(d)
