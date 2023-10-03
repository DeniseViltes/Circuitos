import numpy as np
import matplotlib.pyplot as plt

Vcc = 12
Rc = 4.7 * 10 ** 3
Re =  470


v_ce = np.arange(-0.5, Vcc + 2, 0.2)
ICq = 1.28 * 10 ** (-3)
VceQ = 5.4


def RCE(x):
    y = []
    for i in x:
        ic = Vcc / (Rc + Re) - i / (Rc + Re)
        y.append(ic * 10 ** 3)
    return y




ICqm = 1.36 * 10 ** (-3)
VceQm = 5.2


def RCD(x):
    y = []
    for i in x:
        ic = VceQm /(Rc+Re) - i / (Rc+Re) + ICqm
        y.append(ic * 10 ** 3)
    return y


rce = RCE(v_ce)
rcd = RCD(v_ce)
fig, ax = plt.subplots()

xtiks = [0,0.7,2,4,5.4,6,8,10,12,14]
ax.xaxis.set_ticks(xtiks,labels=xtiks)
ax.axhline(0, color='black')
ax.axvline(0, color='black')
ax.axhline(ICq * 10 ** 3, linestyle=':', color='tab:red')
ax.axhline(ICqm * 10 ** 3, linestyle=':', color='tab:green')

ax.axvline(VceQ, linestyle=':', color='tab:red')
ax.axvline(0.7, linestyle='--', color='tab:orange')
ax.axvline(VceQm, linestyle=':', color='tab:green')


ax.plot(v_ce, rce, label='Recta de carga estática teorica', color='red')
ax.plot(v_ce, rcd, linestyle = '--',label='Recta de carga estatica medida', color='green')


plt.title('Recta de carga teórica vs medida')

ax.set_ylabel("Corriente [mA]")

ax.set_xlabel("Vce [V]")

plt.grid(True)
ax.scatter(VceQ, ICq* 10 ** 3,marker='o', color='red', zorder=10, label= 'Punto de reposo teórico')
ax.scatter(VceQm, ICqm* 10 ** 3,marker='o', color='green', zorder=11,label= 'Punto de reposo medido')


plt.legend()
plt.show()
