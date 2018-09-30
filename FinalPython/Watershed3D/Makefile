all:  doDiv doPert move


doDiv:
	python Divergencia_sigmas.py

doPert:
	python Watershed3D.py

move:
	mv *.npy Binaries/


clean:
	rm div*.npy
