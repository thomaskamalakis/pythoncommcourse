import numpy as np
from matplotlib import pyplot as plt

T = 10e-6   # signal duration (s)
Dt = 0.1e-6 # sampling interval (s)
T1 = 5e-6   # pulse "on" duration (s)
A = 1       # signal amplitude

t = np.arange(-T/2, T/2, Dt)       # time axis

x = Α * (np.abs(t) <= T1/2).astype(float)
                
plt.close('all')                   # Close all figures
plt.figure(1)                      # open a new figure
plt.plot(t, x)                     # plot the signal

 