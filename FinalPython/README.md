# Python : Watershed complete

## Files

### Divergencia_sigmas.py
Given the velocity binary files in all 3 Dimensions, The divergence 3D array is calculated for determined sigmas.


## RUN

### Makefile
With just a simple 
```
make
```
you may start the process of making new data.

#### IMPORTANT
In order to RUN the sequence you need the following files in the Directory:
-**Binaries/** (DIR) *Directory where binary files will be moved*
-**Vx_grid.npy** (binary) *Binary file that contains the 3D grid corresponding to speed in X - Axis*
-**Vy_grid.npy** (binary) *Binary file that contains the 3D grid corresponding to speed in Y - Axis*
-**Vz_grid.npy** (binary) *Binary file that contains the 3D grid corresponding to speed in Z - Axis*
-**parameters.csv** (CSV) *CSV file that contains the sigmas that will be evaluated . Integer sigmas from SigmaInicial to SigmaFinal with step of 1 *
-**Divergencia_Sigmas.py** (python) *Python code that uses speed binary files mentioned before to calculate the Divergence scalar, creating this way div_XX.py*
-**Watershed3D.py** (python) *Python code that runs the watershed algorithms and segregate groups, creating this way pert_XX.py*
-**Makefile** (Makefile) *Secuence that compiles the whole code*

### More ...
To remove every binary file from main directory, you just 
```
make clean
```
