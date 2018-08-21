import numpy as np
import matplotlib.pyplot as plt

Data=np.loadtxt("TestMatrix.txt")

plt.figure(figsize=[12,12])
plt.imshow(Data)
plt.savefig("testing.png")
