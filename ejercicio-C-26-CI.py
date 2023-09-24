import numpy as np
import matplotlib.pyplot as plt

Vcc = 12
Vbb = 2.45
vs = 0.2
Rs = 100
Rc = 2 * 10 ** 3
Re = 1 * 10 ** 3
Rl = 2 * 10 ** 3
Rb = 8 * 10 ** 3
v_ce = np.arange(-0.5, Vcc + 2, 0.2)
ICq=1.75*10**(-3)
VceQ=6.75
Rca = 1/(1/Rc+1/Rl)

print(Vcc / (Rc + Re))
def RCE(x):
    y = []
    for i in x:
        ic = Vcc / (Rc + Re) - i / (Rc + Re)
        y.append(ic*10**3)
    return y
def RCD(x):
    y=[]
    for i in x:
        ic =-i/(Re+Rca) +VceQ/(Re+Rca)+ICq
        y.append(ic*10**3)
    return y
rce= RCE(v_ce)
rcd=RCD(v_ce)


plt.plot(v_ce,rce, label = 'Recta de carga estática', color = 'red')
plt.plot(v_ce,rcd,label = 'Recta de carga dinámica', color = 'green')
plt.text(VceQ+1/3,ICq*10**3+1/3, 'Q')
plt.title('Rectas de carga')
plt.ylabel("Corriente [mA]")
plt.axhline(0,color='black')
plt.axvline(0,color='black')
plt.axhline(ICq*10**3,linestyle= ':')
plt.axvline(VceQ,linestyle= ':')
plt.axvline(0.6,linestyle= ':',color ='orange')
plt.text(0.8,-1.5,'Vce(sat)')
plt.xlabel("Vce [V]")
plt.grid(True)
plt.legend()
plt.show()