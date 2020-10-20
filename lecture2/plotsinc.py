import numpy as np
from matplotlib import pyplot as plt

T = 10e-6     # signal duration (s)
T1 = T / 2.0  # pulse on duration (s)
A = 1         # signal amplitude
Nf = 20       # number of Fourier components to be calculated

k = np.arange(-Nf, Nf + 1)              # Fourier indices
fk = k / T                              # Fourier frequencies
Ak = A * T1 / T * np.sinc( k * T1 / T)  # Fourier coefficients

plt.close('all')
plt.figure(1)
plt.plot(fk, Ak)

Ta = T 
Ta1 = T1 / 2.0
fka = k / Ta                                   # Fourier frequencies
Aka = A * Ta1 / Ta * np.sinc( k * Ta1 / Ta )   # Fourier coefficients

plt.figure(2)
plt.plot(fka, Aka)
