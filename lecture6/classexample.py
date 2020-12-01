import matplotlib.pyplot as plt
import commlibv2 as cl
import numpy as np

# Parameters
TS = 1e-6
samples_per_symbol = 20
tinitial = 0
tguard = 10 * TS
f0 = 1 / TS

# system transfer function
H = lambda f : np.exp( -f**2.0 / f0 ** 2.0 / 2)

# Signal constellation
c = cl.pam_constellation(16, title = '16-PAM')

# Plot PAM constellation
plt.close('all')
c.plot()
c.plot_map()

# set bits to be transmitted
bits = cl.random_bits(32)

# build input waveform and plot
x = cl.digital_signal(TS = TS, samples_per_symbol = samples_per_symbol, 
                      tinitial = tinitial, tguard = tguard, constellation = c)

x.modulate_from_bits( bits, constellation = c )
x.plot()

# create channel system and apply
s = cl.system(input_signal = x, transfer_function = H)
s.apply()

# get output signal and plot
y = s.get_output()
y.plot()
