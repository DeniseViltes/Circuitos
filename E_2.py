import numpy as np
import matplotlib.pyplot as plt
from funciones_basicas_circuitos import *

Vcc = 30
Rc = 1.5 * 10 ** 3
Re = 6.8 * 10 ** 3
Rl = 10 * 10 ** 3

v_ce = np.arange(-0.5, Vcc + 2, 0.2)
ICq = 3.1 * 10 ** (-3)
VceQ = 4.3
Rca = 1 / (1 / Rc + 1 / Rl)

print(ICq*paralelo(Rc, Rl))


def RCE(x):
    y = []
    for i in x:
        ic = Vcc / (Rc + Re) - i / (Rc + Re)
        y.append(ic * 10 ** 3)
    return y


gm = 67.7 * 10 ** -3


def RCD(x):
    y = []
    for i in x:
        ic = VceQ / paralelo(Rc, Rl) - i / paralelo(Rc, Rl) + ICq
        y.append(ic * 10 ** 3)
    return y


rce = RCE(v_ce)
rcd = RCD(v_ce)

plt.plot(v_ce, rce, label='Recta de carga estática', color='red')
plt.plot(v_ce, rcd, label='Recta de carga dinámica', color='green')


plt.title('Rectas de carga E-2')
plt.ylabel("Corriente [mA]")
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.axhline(ICq * 10 ** 3, linestyle=':')
plt.axvline(ICq*paralelo(Rc, Rl)+VceQ, linestyle=':')
plt.axvline(VceQ, linestyle=':')
plt.xlabel("Vce [V]")
plt.ylim([-3, 9])
plt.grid(True)
plt.legend()
plt.show()
