import ltspice
import os
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True
l = ltspice.Ltspice(os.path.dirname(__file__)+'/resources/oscilador.raw')
l.parse()

time = l.get_time()
Vo= l.get_data('V(vo)')

fig, ax = plt.subplots()
plt.grid(True)

ax.set_xlabel('Tiempo [ms]')
ax.set_ylabel('Tensión [V]')

plt.title('Salida del Oscilador')

ax.plot(time*10**3,Vo, color = 'tab:purple')

plt.show()