# Python : Watershed complete

## Directories

### Watershed3D/
Runs the watershed on the given velocities according to a sigma previously set to interpolate the speeds.

#### IMPORTANT
In order to RUN the main sequence you need the following files in the Directory:

- **Binaries/** (DIR) *Directory where binary files will be moved*

- **Vx_grid.npy** (binary) *Binary file that contains the 3D grid corresponding to speed in X - Axis* (if not, refer to VelocitiesBuild/)

- **Vy_grid.npy** (binary) *Binary file that contains the 3D grid corresponding to speed in Y - Axis* (if not, refer to VelocitiesBuild/)

- **Vz_grid.npy** (binary) *Binary file that contains the 3D grid corresponding to speed in Z - Axis* (if not, refer to VelocitiesBuild/)

- **parameters.csv** (CSV) *CSV file that contains the sigmas that will be evaluated . Integer sigmas from SigmaInicial to SigmaFinal with step of 1 *

- **Divergencia_Sigmas.py** (python) *Python code that uses speed binary files mentioned before to calculate the Divergence scalar, creating this way div_XX.py*

- **Watershed3D.py** (python) *Python code that runs the watershed algorithms and segregate groups, creating this way pert_XX.py*

- **Makefile** (Makefile) *Secuence that compiles the main sequence code* 

#### RUN

##### Makefile

With just a simple 

```
make
```
you may start the process of making new data.

#### More ...

To remove every binary file from **Watershed3D/** directory, you just:

```
make clean
```






### VelocitiesBuild/
Takes a file with the *Mass, 3D postion and 3D Speed* variables and build a grid of 120 x 120 x 120 (adjustable) for every axis for the components of the speed. This speed is the speed of the center of mass.


#### IMPORTANT
In order to RUN the main sequence you need the following files in the Directory:



- **HaloCpt.txt** (Text) *Data file with the positions, velocities and mass of every object* 

- **BuildVelocities.py** (python) *Python that build the speed binaries*

- **Makefile** (Makefile) *Secuence that compiles the code for building velocity binaries*


#### RUN

##### Makefile

For building the binaries for the Velocities in X,Y,Z, you should :
```
make
```

Once built the binaries, you must copy them into the **Watershed3D/** directory.


