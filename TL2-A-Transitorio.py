import matplotlib.pyplot as plt
import os
import ltspice

plt.rcParams['text.usetex'] = True

l = ltspice.Ltspice(os.path.dirname(__file__)+'/resources/TL2_transitorio.raw')
l.parse()

time= l.get_time()
time = time*10**6
vo =l.get_data('V(vo)')
vi = l.get_data('V(vi)')

fig, ax1 = plt.subplots()
plt.grid(True)

ax1.set_xlabel('Tiempo [$\mu$ s]')
ax1.set_ylabel('Tensión [V]',color = 'tab:purple')
plt.title('Etapa amplificadora con un transistor')

plot_1 = ax1.plot(time,vo,color = 'tab:purple', label = 'Señal de salida')

ax2 = ax1.twinx()
ax2.set_ylabel('Tensión [mV]',color = 'tab:orange')
plot_2 = ax2.plot(time,vi*10**3,color = 'tab:orange', label = 'Señal de entrada')

lns = plot_1 + plot_2
labels = [l.get_label() for l in lns]
plt.legend(lns, labels, loc=0)

plt.show()