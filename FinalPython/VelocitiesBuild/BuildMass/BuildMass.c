#include <stdio.h>
#include <stdlib.h>
#include <math.h>
//CONSTANTES Y ARREGLOS==========================
int n_side=120;

int Lbox= 1200;
int l_side;


//variales de iteracion
int i;
int j;
int k;
int l;


//sobre parametros
FILE *parametros;
int MAXCOLS;
int MAXROWS;

//sobre input
FILE *sampleIN;
double *x;
double *y;
double *z;
double *m;

//sobre output

FILE *sampleOUT;
int *X;
int *Y;
int *Z;
double *M;


//FUNCIONES (DECLARE)====================

void reconocerParametros();
void cargarArreglosIniciales(int mrows);
int construirGrid(int longitud);
//MAIN==========================
int main()
{
reconocerParametros();
printf("max rows = %d , max cols = %d, l_side = %d\n",MAXROWS,MAXCOLS,l_side);
//printf("size of x= %lu , y = %lu z = %lu \n",sizeof(x),sizeof(y),sizeof(z));
cargarArreglosIniciales(MAXROWS); //aqui esta el error
int numero_voxeles=n_side * n_side * n_side;
int control=construirGrid(numero_voxeles);




return 0;
}
//FUNCIONES==========================
void reconocerParametros(){
parametros=fopen("parametros.txt","r");
fscanf(parametros,"%d %d",&MAXROWS,&MAXCOLS);
fclose(parametros);

l_side = Lbox/n_side;
printf("R = %d , C = %d , lside = %d \n",MAXROWS,MAXCOLS,l_side);
x=(double*) malloc(MAXROWS * sizeof(double));
y=(double*) malloc(MAXROWS * sizeof(double));
z=(double*) malloc(MAXROWS * sizeof(double));
m=(double*) malloc(MAXROWS * sizeof(double));

if((x==NULL)||(y==NULL)||(z==NULL)||(m==NULL)){
printf("malloc failed ,damn");
exit(1);

}


}


void cargarArreglosIniciales(int mrows){
sampleIN=fopen("HaloMassCpt.txt","r");
for(int i=0; i < mrows ;i++){
printf("scan row %d \n",i);
fscanf(sampleIN,"%lf %lf %lf %lf", &x[i], &y[i], &z[i], &m[i]);
//if(i % 10000 == 0){
//printf(" | %lf %lf %lf %lf %lf %lf %lf |\n",x[i],y[i],z[i],vx[i],vy[i],vz[i],m[i]);}
}
fclose(sampleIN);
}


int construirGrid(int longitud){
X=(int*) malloc(longitud * sizeof(int));
Y=(int*) malloc(longitud * sizeof(int));
Z=(int*) malloc(longitud * sizeof(int));
M=(double*) malloc(longitud * sizeof(double));

//if((X==NULL)||(Y==NULL)||(Z==NULL)||(VX=NULL)||(VY=NULL)||(VZ=NULL)){
//printf("Error allocating\n");
//return 1;}

sampleOUT=fopen("grid3D_16.txt","w");


for(int i=16;i<n_side;i++){
printf("printing %d\n",i);
for(int j=0;j<n_side;j++){
for(int k=0;k<n_side;k++){
double Masa = 0;

for(int l=0;l<MAXROWS;l++){



if( (x[l]>=(i * l_side)) && (x[l]< ((i * l_side)+l_side)) && (y[l]>=(j * l_side)) && (y[l]< ((j * l_side)+l_side)) && (z[l]>=(k * l_side)) && (z[l]< ((k * l_side)+l_side)) ){

Masa=Masa+m[l];

}

}
int num_unidim=k+(l_side*j)+(l_side*l_side*i);
X[num_unidim]= i;
Y[num_unidim]= j;
Z[num_unidim]= k;
M[num_unidim]= Masa;


fprintf(sampleOUT,"%d %d %d %lf\n",X[num_unidim],Y[num_unidim],Z[num_unidim],M[num_unidim]);
}
}
printf("x = %d",i);
}
fclose(sampleOUT);
return 0;
}




