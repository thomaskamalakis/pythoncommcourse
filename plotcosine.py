# Import basic libraries
import numpy as np
from matplotlib import pyplot as plt
 
t = np.arange(0.0, 0.1, 1e-4)
A = 1
f0 = 50

x = A * np.cos( 2 * np.pi * f0 * t)

plt.close('all')
plt.figure(1)
plt.plot(t, x)