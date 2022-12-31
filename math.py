#Find The Optimal Point

from textwrap import indent
import numpy as np 
import matplotlib.pyplot as plt
from numpy.core.defchararray import index

x = np.linspace(0,300,3000)
y =-x**2+100*x+60000
plt.plot(x,y) 

ymax = np.max(y)
index = np.argmax (y)

plt.plot(x[index],ymax, 'or')

xmax = np.round (x[index],0)
s = 'Max Point = '+str (xmax)
plt.text (x[index],ymax+1000, s) 
plt.show ()

#print (xmax)
