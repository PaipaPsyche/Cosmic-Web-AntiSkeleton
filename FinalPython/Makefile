all: del doDiv doPert move

del:
	rm -r Binaries

doDiv:
	python Divergencia_sigmas.py

doPert:
	python Watershed3D.py

move:
	mv *.npy Binaries/
