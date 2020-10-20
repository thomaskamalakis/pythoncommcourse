import numpy as np
from matplotlib import pyplot as plt

T = 10e-6   # signal duration (s)
Dt = 0.1e-6 # sampling interval (s)
T1 = 5e-6   # pulse "on" duration (s)
A = 1       # signal amplitude

t = np.arange(-T/2, T/2, Dt)       # time axis
x = np.zeros( np.size(t) )         # signal array with size equal to t

for i, tm in enumerate(t):         # for every value of t
    if -T1/2 <= tm < T1/2:         # if tm is inside the pulse
        x[i] = A                   #   signal must be equal to A
    else:                          # otherwise
        x[i] = 0                   #   signal must be zero
                
plt.close('all')                   # Close all figures
plt.figure(1)                      # open a new figure
plt.plot(t, x)                     # plot the signal

 