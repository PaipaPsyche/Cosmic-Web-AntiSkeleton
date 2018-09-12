"""
Created on Sat Sep  1 15:01:58 2018

@author: david
"""
import imageio as imio

filenames=[]
images=[]
num_img=20
for i in range(num_img):
    texto="IMGestructura_"+str(i+1)+".png"
    filenames.append(texto)
for i in range (5):
    filenames.append("IMGestructura_"+str(num_img)+".png")
cont=0
for filename in filenames:
    cont+=1
    images.append(imio.imread(filename))
    print(str(cont)+" appended.")
print("compiling gif...")
imio.mimsave("DivGifcbar.gif",images)
print("gif done.")
