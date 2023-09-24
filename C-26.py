from TBJ import BaseComun as bc
from funciones_basicas_circuitos import *

Re = 1 * 10 ** 3
Rc = 2 * 10 ** 3
Rl = 2 * 10 ** 3
Rb1 = 39 * 10 ** 3
Rb2 = 10 * 10 ** 3
Rs = 100

Vcc = 12
Beta = 290


Th = thevenin_divisor_de_tension(Vcc, Rb2, Rb1)
Vbb = Th[0]
Rb = Th[1]

Icq = 1.75 * 10 ** (-3)
Vceq = 6.75

BC = bc.BaseComun(Re, Icq, Beta)

Rie = BC.Rie()
Ri = paralelo(Rie, Re)

Roc = BC.Roc(Rs, 0)
Ro = paralelo(Roc, Rc)

Rca = paralelo(Ro, Rl)

Av = BC.gananciaAv(Rca)

print('Configuración : Re con cap')
print('Rb1 = ', Rb1 * 10 ** -3, 'K ohms')
print('Rb2 = ', Rb2 * 10 ** -3, 'K ohms')
print('Vbb = ', Vbb, 'V', 'Rb = ', Rb * 10 ** -3, 'K ohms')

print('Rc = ', Rc * 10 ** -3, 'K ohms')
print('Re = ', Re, 'ohms')

print('Polarización')
print('Punto Q = (', Vceq, 'V;', Icq * 10 ** 3, 'mA)')
print('Circuito de señal')
print('Ri = ', Ri)
print('Ro = ', Ro)
print('Av = ', Av)
print('Avs = ', BC.gananciaAvs(Rs,Rca))
BC.hibrido.imprimirParamtros()


