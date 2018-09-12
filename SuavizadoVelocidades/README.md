# Suavizando Velocidades y observando divergencia de velocidad

### makeVelocidades.py
* A partir de los datos RAW de la simulación con 7 parametros observados para cada objeto (x ,y , z , Vx , Vy , Vz , M)
 se construye una grilla 3D para cada eje de velocidad para la velocidad del centro de masa de cada voxel.
* Las grillas se almacenan en archivos binarios.

# suavizarVelocidades.py
* Dadas las grillas 3D  Vx, Vy, Vz se convoluciona cada una con un kernel gausiano con un sigma dado en celdas.
* Esto retorna una grilla 3D con la divergencia de velocidad para cada voxel.
* La grilla de divergencia se almacena en un archivo binario.

# Graficas_Test.py
* Dada la divergencia, construye imagenes correspondientes a un barrido en z de esta grilla y su color en intensidad.
* Retorna un numero dado de imágenes

# buildGif.py
* Construye un .GIF con el barrido en Z de la divergencia.
* Retorna un archo GIF.

# TryEstructura.py
* Dada la divergencia, hace un gráfico scatter de los puntos de la grilla que superen un umbral impuesto y su color
varia segun su valor de divergencia.
* Imprime imágenes a un intervalo dado para construir por capas la estructura formada.

# ShellGif.py
* Se construye un .GIF con las imagenes ya hechas de la reconstruccion por capas de las estructuras propouestas.
