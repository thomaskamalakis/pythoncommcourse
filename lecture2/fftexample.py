import numpy as np
import matplotlib.pyplot as plt

# function to create the square pulse
def square(t1 , T1):  
    f = np.logical_and( t1 <= T1 / 2.0 , t1 >= -T1/2.0 )
    return f.astype('float')
     
# time axis
T = 4;
Tmax = 30.0
N = 1024
n = np.arange(-N / 2.0, N / 2.0, 1)
Dt = 2 * Tmax / N
t = n * Dt

# frequency axis
Df = 1.0 / ( N * Dt)
f = n * Df

# signal in the time domain
x=square(t, T)
#
# signal in the frequency domain
X = Dt * np.fft.fftshift( np.fft.fft( np.fft.fftshift(x) ) )

# Analytical expression for the spectrum
X2= T * np.sinc( f * T )

# Plot results
plt.close('all')

plt.figure(1)
plt.xlabel('t [msec]')
plt.ylabel('x(t)')
plt.plot(t,x)

plt.figure(2)
plt.plot(f, X2 , f , np.real(X), 'o')
plt.xlim(-1.5, 1.5)
plt.legend(['analytical','numerical'])
plt.xlabel('f [kHz]')
plt.ylabel('X(f)')
