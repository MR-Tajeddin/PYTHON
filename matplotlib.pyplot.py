from os import MFD_CLOEXEC
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace (0,10000,100000)
Cost = 0.001*x**2 - 5*x + 5000
plt.plot (x,Cost)


MC = np.min(Cost)
Index = np.argmin(Cost)
MCx = x[Index]
plt.plot (MCx,MC,'o')
plt.show()
print (MCx)
