#include <stdio.h>
#include <stdlib.h>
#include <math.h>
//CONSTANTES Y ARREGLOS==========================
int n_side=120;

int Lbox= 600;
int l_side;


//variales de iteracion
int i;
int j;
int k;
int l;


double *x;
double *y;
double *z;
double *vx;
double *vy;
double *vz;
double *m;
//double Vx_grid[n_side][n_side][n_side];
//double Vy_grid[n_side][n_side][n_side];
//7double vz_grid[n_side][n_side][n_side];

//sobre parametros
FILE *parametros;
int MAXCOLS;
int MAXROWS;

//sobre input
FILE *sampleIN;



//double y*;
//double z*;



//sobre output



//FILE *sampleOUT;


//FUNCIONES (DECLARE)====================

void reconocerParametros();
void cargarArreglosIniciales(int mrows);

//MAIN==========================
int main()
{
reconocerParametros();
printf("max rows = %d , max cols = %d, l_side = %d\n",MAXROWS,MAXCOLS,l_side);
cargarArreglosIniciales(MAXROWS);





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
sampleIN=fopen("Halo3D_600.txt","r");
for(int i=0; i < mrows ;i++){
fscanf(sampleIN,"%lf %lf %lf %lf %lf %lf %lf",&x[i],&y[i],&z[i],&vx[i],&vy[i],&vz[i],&m[i]);
printf("%lf %lf %lf",x[i],y[i],z[i]);
}
fclose(sampleIN);
}

