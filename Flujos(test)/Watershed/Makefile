all: runpy moving doing

runpy:
	python watershed.py
moving:
	mv pertenencia.txt graficaVelocidades/
doing:
	cd graficaVelocidades/ && make
	
clean:
	rm *png	
	cd graficaVelocidades/ && make cleaning
	
