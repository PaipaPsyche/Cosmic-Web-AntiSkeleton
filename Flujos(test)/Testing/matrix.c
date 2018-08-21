#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define TAMANO 120

int i;
int j;
FILE *out;




int main(){
out = fopen("TestMatrix.txt","w");
double mid= TAMANO/2;
for(i = 0;i<TAMANO;i++){
for(j = 0;j<TAMANO;j++){


double x = pow((i-mid),2);
double y = pow((j-mid),2);

double new = pow((x+y),0.5f) - 60;

fprintf(out,"%lf ",new);




}
fprintf(out,"\n");
}

fclose(out);
return 0;
}
