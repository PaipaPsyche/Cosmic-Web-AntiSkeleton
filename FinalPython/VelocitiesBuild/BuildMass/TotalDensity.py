"""
Created on Thu Oct 18 17:54:29 2018

@author: david
"""
import numpy as np
import matplotlib.pyplot as plt
#from astropy.convolution import Gaussian2DKernel,convolve
#import scipy.linalg as linalg
#from mpl_toolkits.mplot3d import Axes3D
from decimal import Decimal



DATA=np.load("MassGrid.npy")


totalMass=np.sum(DATA)#[1:-1,1:-1,1:-1]
totalVol=1200**3 #mpc

print("Densidad Total = ",'%.2E' % Decimal(totalMass/totalVol))