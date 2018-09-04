import numpy as np
import matplotlib.pyplot as plt

#Datos iniciales ===================
Data=np.loadtxt("ScalarGauss.txt")
nodos=np.loadtxt("MaximumNodeMap.txt")
n_nodos=len(np.where(nodos==1)[0])
n_side=int(Data.shape[0])
valor_max=0
valor_min=0 #Definiendo límites del barrido de watershed
cuenta_datos=n_side*n_side #datos
pertenencia=np.zeros([n_side,n_side]) #mapa de pertenecia colores

precoord=np.where(nodos==1)
for i in range(n_nodos):
    x=precoord[0][i]
    y=precoord[1][i]
    pertenencia[x,y]=int(i+1)   #cargando las coordenadas de los nodos iniciales 


def extraccionParametros():
	maxval=0
	minval=0
	
	for line in Data:
		for element in line:
			if(element>maxval):
				maxval=element
			if(element<minval):
				minval=element
		
	return maxval,minval   #cargar datos valor_max , valor_min
def printMatrix(M):
	plt.figure(figsize=[12,12])
	plt.imshow(M)
	plt.savefig("printedMatrix.png")#imprimir un areglo 2D


valor_max,valor_min=extraccionParametros()
delta=(valor_max-valor_min)/cuenta_datos
#delta para ajustar los limites inferiores y superiores del barrido 
barrido_watershed=np.linspace(valor_max+(2*delta),valor_min-(2*delta),int(cuenta_datos/2))


def sup(n):
	return (n+1)%n_side
def inf(n):
	return(n-1)%n_side
#pixeles vecinos en condiciones periódicas

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

#elige la pertenencia del pixel mas cercano
#Solo lo uso provisionalmente para watershed cuando no se tiene una solucion
#por pixeles vecinos


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
#pixeles vecinos
    
    
    vecinos.append(arr)
    vecinos.append(abb)
    vecinos.append(izq)
    vecinos.append(der)

    suma=arr+abb+izq+der
#    al menos un vecino tiene pertenencia definida
        	
    if(suma==0):
        c=elegirMasCercano(ii,jj)
#   si no hay vecinos con pertenencia definida, elige la pertenencia del 
        #nodo mas cercano
        return c,1
    else:
        nz=[]
        for elem in vecinos:
            if (elem!=0):
                nz.append(elem)
        p=np.random.choice(nz)
        return int(p),0
    
    
#retorna la pertenencia del pixel evaluado y 
#retorna  1 si tomo una desicion aleatoria
        # 0 si tomó una desición basada en los vecinos


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
#cuenta los pixeles sin asignar


#Propagar las manchas, el plano de watershed recorre todo el mapa 
#Gaussiano de el nivel máximo al nivel mínimo propagando la pertenencia
#de los nodos. para cada intervalo, intenta coloear los pixeles segun sus vecinos
#no obstante, cuando el pixel no tiene vecinos con pertenencia definida, se le
#asigna la del nodo más cercano
#
#
def propagar():
    total=0  #total de decisiones tomadas
    contador=0 #contador veces que se tomo una desición aleatoria
    cota_inf=0
    cota_sup=0
    #cotas inferior y superior para seccion transversal por watershed
    for nivel in range(len(barrido_watershed)-1):
        if(nivel%600==0):
            print(str(int(nivel*100/(len(barrido_watershed)-1)))+"%")
        cota_sup=barrido_watershed[nivel]
        cota_inf=barrido_watershed[nivel+1]
        #define las cotas inferior y superior        
        vacios=contarPixelesNoIdentificados(cota_inf,cota_sup)
        
        while(vacios!=0): #hay que asignar pertenencia a todos los pixeles de la "tajada"
            for i in range (n_side):
                for j in range(n_side):
                    if((pertenencia[i,j]==0)&(Data[i,j]<=cota_sup)&(Data[i,j]>cota_inf)):
                        pertenencia[i,j],cont=revisarPertenenciaVecinos(i,j)
                        total+=1
                        contador+=cont
            
            vacios=contarPixelesNoIdentificados(cota_inf,cota_sup)

    return contador/total #retorna rata de decisiones aleatorias

    
perc=propagar()


#guardar el mapa de pertenencia en  un archivo de texto
def printPertenencia(textname,M):
    np.savetxt(textname,M)
#    file=open(textname,"w")
#    for i in range(n_side):
#        for j in range(n_side):
#            file.write(str(pertenencia[i,j]))
#        print("\n")


plt.figure(figsize=[12,12])

plt.imshow(pertenencia)

porcentajeAleatorio=perc*100
plt.title("matriz de pertenencia ( "+str(porcentajeAleatorio) +" % aleatorio)", fontsize=18)
plt.savefig("Pertenencia.png")


printPertenencia("pertenencia.txt",pertenencia)
