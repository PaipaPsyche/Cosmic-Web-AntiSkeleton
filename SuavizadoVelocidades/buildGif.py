"""
Created on Sat Sep  1 15:01:58 2018

@author: david
"""
import imageio as imio

filenames=[]
images=[]
for i in range(118):
    texto="plotdiv_"+str(i+1)+".png"
    filenames.append(texto)
cont=0
for filename in filenames:
    cont+=1
    images.append(imio.imread(filename))
    print(str(cont)+" appended.")
print("compiling gif...")
imio.mimsave("DivGif.gif",images)
print("gif done.")
