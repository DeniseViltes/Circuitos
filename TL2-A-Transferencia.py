import ltspice
import os
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True
plt.rcParams['figure.constrained_layout.use'] = True

l = ltspice.Ltspice(os.path.dirname(__file__)+'/TL2_A.raw')
l.parse()


freq = l.get_frequency()
V_out = l.get_data('V(vo)')


Vout_amplitude = 20 * np.log10(np.abs(V_out))
Vout_angle = np.angle(V_out, deg=True)
Vout_angle= np.unwrap(Vout_angle)


#
datos_simul = np.genfromtxt('resources/TL2_transferencia_medicion.txt', delimiter='\t', skip_header=1)
frecuencia_m = datos_simul[:, 0]
magn_m = datos_simul[:, 1]

fl = 10
fh = 9*10**6
fhm = 300000

hmax = 19.5

fig, ax1 = plt.subplots(layout="constrained")
plt.grid(True)
xticks = [10**1,10**3, 10**5,fhm,10**7,10**9]
xlabels = [r'$10^1$',r'$10^3$',r'$10^5$',r'$3\;10^6$',r'$10^7$',r'$10^9$']
ax1.set_xlabel('Frecuencia [Hz]')
ax1.set_ylabel('Ganancia [dB]', color='tab:red')
plot_1 = ax1.plot(freq, Vout_amplitude,linestyle = '-', color='tab:red', label = 'Magnitud simulada')
ax1.plot(frecuencia_m, magn_m,linestyle = '--', color='tab:blue', label = 'Magnitud medida')
ax1.scatter(frecuencia_m,magn_m, color = 'tab:blue',marker = 'x', label = 'Puntos de la magnitud medidos')
ax1.axhline(y = hmax-3, linestyle = '--', color = 'tab:cyan')
ax1.axvline(x= fl, linestyle = '--', color = 'tab:cyan')
ax1.axvline(x= fh, linestyle = '--', color = 'tab:cyan')
ax1.axvline(x= fhm, linestyle = '--', color = 'tab:cyan')
plt.semilogx()
plt.title('Respuesta en frecuencia')
plt.grid(True)

plt.text(1000, hmax-2.5, 'Caída de 3dB',color = 'tab:cyan')

ax1.xaxis.set_ticks(xticks, labels=xlabels)
ax1.set_ylim([-2,23])

ax1.legend()

plt.show()