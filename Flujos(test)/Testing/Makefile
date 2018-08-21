all: generate compile graph clean

generate: matrix.c
	gcc matrix.c -o matrix -lm
compile:
	./matrix
graph:
	python testing.py
clean:
	rm TestMatrix.txt matrix
