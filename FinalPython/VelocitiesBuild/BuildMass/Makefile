all: fake

fake:
	echo "Select an order"




doingall:
	filered param gridC execute makemass 

filered:
	awk '{print($1" "$2" "$3" "$7)}' HaloCpt.txt > HaloMassCpt.txt

param:
	python parametrosC.py

gridC:
	gcc -o exec BuildMass.c -lm

execute:
	./exec

makemass:
	python MakeMass.py







