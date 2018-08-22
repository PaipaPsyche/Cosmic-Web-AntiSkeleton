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


def defnirCondicionesIniciales():
	precoord=np.where(nodos==1)
	for i in range(n_nodos):
		x=precoord[0][i]
		y=precoord[1][i]
		pertenencia[x,y]=i

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
#printMatrix(pertenencia)			


valor_max,valor_min=extraccionParametros()
#print(valor_max,valor_min)	
delta=(valor_max-valor_min)/cuenta_datos
barrido_watershed=np.linspace(valor_min-(2*delta),valor_max+(2*delta),4*cuenta_datos)
#print(barrido_watershed)
def sup(n):
	return (n+1)%n_side
def inf(n):
	return(n-1)%n_side

def revisarPertenenciaVecinos(ii,jj):
	i_a=inf(ii)
	i_b=sup(ii)
	j_a=inf(jj)
	j_b=sup(jj)
	vecinos=np.array(4)	
	arr=pertenencia[i_a,jj]
	abb=pertenencia[i_b,jj]
	izq=pertenencia[ii,j_a]
	der=pertenencia[ii,j_b]
	vecinos[0]=arr
	vecinos[1]=abb
	vecinos[2]=izq
	vecinos[3]=der
	
	
	if((arr+abb+izq+der)==0):
		return 0
	else:
		nz=vecinos[np.nonzero(vecinos)]
		print( np.random.choice(nz))
		
		
	
def propagar():
	cota_inf=0
	cota_sup=0
	for nivel in range(len(barrido_watershed)-1):
		cota_inf=barrido_watershed[nivel]
		cota_sup=barrido_watershed[nivel+1]
		for i in range(n_side):
			for j in range(n_side):
				if((Data[i,j]>=cota_inf)and(Data[i,j]<cota_sup)):
					if(pertenencia[i,j]==0):
						pertenencia[i,j]=revisarPertenenciaVecinos(i,j)


def hayZero(M):
	r=False
	for line in M:
		for element in line:
			if(element==0):
				r=True
	return r

while(hayZero(pertenencia)):
	propagar()					
		
		

	


