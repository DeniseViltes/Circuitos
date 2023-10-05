import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.rcParams['text.usetex'] = True

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
yticks=[0,0.1,0.5,1.0,1.5,2.0,2.5]
ax.xaxis.set_ticks(xtiks,label=xtiks)
ax.yaxis.set_ticks(yticks,label=yticks)
ax.axhline(0, color='black')
ax.axvline(0, color='black')
ax.axhline(ICq * 10 ** 3, linestyle=':', color='tab:red')
ax.axhline(ICqm * 10 ** 3, linestyle=':', color='tab:green')

ax.axvline(VceQ, linestyle=':', color='tab:red')
ax.axvline(0.7, linestyle='--', color='tab:orange')
ax.axhline(0.1, linestyle='--', color='tab:orange')
ax.axvline(VceQm, linestyle=':', color='tab:green')


ax.plot(v_ce, rce, label='Recta de carga estática teorica', color='red')
ax.plot(v_ce, rcd, linestyle = '--',label='Recta de carga estatica medida', color='green')


plt.title('Recta de carga teórica vs medida')

ax.set_ylabel("Corriente [mA]")

ax.set_xlabel("Vce [V]")

plt.grid(True)
ax.scatter(VceQ, ICq* 10 ** 3,marker='o', color='red', zorder=10, label= 'Punto de reposo teórico')
ax.scatter(VceQm, ICqm* 10 ** 3,marker='o', color='green', zorder=11,label= 'Punto de reposo medido')


arr = mpatches.FancyArrowPatch((0.7,0.12), (VceQ, 0.12),
                               arrowstyle='<->,head_width=.15', mutation_scale=20)
ax.add_patch(arr)
ax.annotate(r"$V_{CQ} - V_{CE_k}$", (.5, .5), xycoords=arr, ha='center', va='bottom')


arr2= mpatches.FancyArrowPatch((VceQ,0.12), (VceQ+(ICq-0.1e-3)*(Rc+Re), 0.12),
                               arrowstyle='<->,head_width=.15', mutation_scale=20)
ax.add_patch(arr2)
ax.annotate(r"$(I_{CQ}-I_{\min})\cdot (R_c+R_e)$", (.5, .5), xycoords=arr2, ha='center', va='bottom')

plt.legend()
plt.show()
