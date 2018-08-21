all: parametros makegrid compile clean

parametros:
	python parametros.py

makegrid:
	gcc -o MakingGrid Making_grid.c -lm

compile:
	./MakingGrid

clean:
	rm parametros.txt MakingGrid
