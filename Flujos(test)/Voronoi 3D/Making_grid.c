#include <stdio.h>
#include <stdlib.h>
#include <math.h>
//CONSTANTES Y ARREGLOS==========================
int n_side=60;

int Lbox= 300;
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
double *vx;
double *vy;
double *vz;
double *m;

//sobre output

FILE *sampleOUT;
int *X;
int *Y;
int *Z;
double *VX;
double *VY;
double *VZ;

//FUNCIONES (DECLARE)====================

void reconocerParametros();
void cargarArreglosIniciales(int mrows);
int construirGrid(int longitud);

//MAIN==========================
int main()
{
reconocerParametros();
//printf("max rows = %d , max cols = %d, l_side = %d\n",MAXROWS,MAXCOLS,l_side);
cargarArreglosIniciales(MAXROWS);
int numero_voxeles=l_side * l_side * l_side;
int control=construirGrid(numero_voxeles);




return 0;
}
//FUNCIONES==========================
void reconocerParametros(){
parametros=fopen("parametros.txt","r");
fscanf(parametros,"%d %d",&MAXROWS,&MAXCOLS);
fclose(parametros);
l_side = Lbox/n_side;
x=malloc(MAXROWS * sizeof(double));
y=malloc(MAXROWS * sizeof(double));
z=malloc(MAXROWS * sizeof(double));
vx=malloc(MAXROWS * sizeof(double));
vy=malloc(MAXROWS * sizeof(double));
vz=malloc(MAXROWS * sizeof(double));
m=malloc(MAXROWS * sizeof(double));
}


void cargarArreglosIniciales(int mrows){
sampleIN=fopen("Halo3D_300.txt","r");
for(int i=0; i < mrows ;i++){
fscanf(sampleIN,"%lf %lf %lf %lf %lf %lf %lf",&x[i],&y[i],&z[i],&vx[i],&vy[i],&vz[i],&m[i]);
//if(i % 10000 == 0){
//printf(" | %lf %lf %lf %lf %lf %lf %lf |\n",x[i],y[i],z[i],vx[i],vy[i],vz[i],m[i]);}
}
fclose(sampleIN);
}


int construirGrid(int longitud){
X=malloc(longitud * sizeof(int));
Y=malloc(longitud * sizeof(int));
Z=malloc(longitud * sizeof(int));
VX=malloc(longitud * sizeof(double));
VY=malloc(longitud * sizeof(double));
VZ=malloc(longitud * sizeof(double));
//if((X==NULL)||(Y==NULL)||(Z==NULL)||(VX=NULL)||(VY=NULL)||(VZ=NULL)){
//printf("Error allocating\n");
//return 1;}

sampleOUT=fopen("grid3D.txt","w");


for(int i=0;i<n_side;i++){
for(int j=0;j<n_side;j++){
for(int k=0;k<n_side;k++){
double M = 0;
double vx_m=0;
double vy_m=0;
double vz_m=0;
for(int l=0;l<MAXROWS;l++){



if( (x[l]>=(i * l_side)) && (x[l]< ((i * l_side)+l_side)) && (y[l]>=(j * l_side)) && (y[l]< ((j * l_side)+l_side)) && (z[l]>=(k * l_side)) && (z[l]< ((k * l_side)+l_side)) ){

M+=m[l];
vx_m+=(m[l] * vx[l]);
vy_m+=(m[l] * vy[l]);
vz_m+=(m[l] * vz[l]);
}

}
int num_unidim=k+(l_side*j)+(l_side*l_side*i);
X[num_unidim]= i;
Y[num_unidim]= j;
Z[num_unidim]= k;
VX[num_unidim]=vx_m/(M+1);
VY[num_unidim]=vy_m/(M+1);
VZ[num_unidim]=vz_m/(M+1);

fprintf(sampleOUT,"%d %d %d %lf %lf %lf\n",X[num_unidim],Y[num_unidim],Z[num_unidim],VX[num_unidim],VY[num_unidim],VZ[num_unidim]);
}
}
printf("x=%d",i);
}
fclose(sampleOUT);
return 0;
}





//END=========================================================================
