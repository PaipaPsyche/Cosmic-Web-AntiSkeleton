"""
Created on Tue Oct  2 16:33:29 2018

@author: david
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as scpimg
#from astropy.convolution import Gaussian2DKernel,convolve
#import scipy.linalg as linalg
#from mpl_toolkits.mplot3d import Axes3D

MASS=np.load("MassGrid.npy")
n_side=np.shape(MASS)[0]

for i in range (1,21):
    m_conv=scpimg.filters.gaussian_filter(MASS,i)
    m_conv=np.array(m_conv)
    
    name="Mass_"+str(i)+".npy"
    np.save(name,m_conv)