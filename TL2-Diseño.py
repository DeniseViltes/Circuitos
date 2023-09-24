from TBJ import EmisorComun as ec
from funciones_basicas_circuitos import *


k = 10 ** 3

# componentes
Rs = 0
Rb1 = 82 * k
Rb2 = 10 * k
Rc = 4.7 * k
Re1 = 470  # Desacoplado
Re2 = 0  # Acoplado
Vcc = 12

Re = Re1 + Re2

B = [200, 374, 490]
Vt = 25.9 * 10 ** (-3)
Btyp = B[1]
VA = 100

# Thevenin
Th = thevenin_divisor_de_tension(Vcc, Rb2, Rb1)
Vbb = Th[0]
Rb = Th[1]

#  --------------------------------Polarización --------------------------------


Vbe = 0.7  # MAD
Ve = Vbb - Vbe
Icq = Ve / Re
Vceq = Vcc - Icq * Rc
Ib = 0
for i in range(20):
    Ib = Icq / Btyp
    Vrb = Rb * Ib
    Vb = Vbb - Vrb
    Ve = Vb - Vbe
    Icq = Ve / Re

# --------------------------------Análisis de señal --------------------------------


EC = ec.EmisorComun(Re1, Icq,Btyp)
EC.sinAcople()
Rib = EC.Rib()
Roc = EC.Roc()

Ri = paralelo(Rib, Rb)
Ro = paralelo(Roc, Rc)

Av = EC.av(Ro)

print('Configuración : Re con cap')
print('Rb1 = ', Rb1 * 10 ** -3, 'K ohms')
print('Rb2 = ', Rb2 * 10 ** -3, 'K ohms')
print('Vbb = ', Vbb, 'V', 'Rb = ', Rb * 10 ** -3, 'K ohms')

print('Rc = ', Rc * 10 ** -3, 'K ohms')
print('Re = ', Re, 'ohms')

print('Polarización')
print('Punto Q = (', Vceq, 'V;', Icq * 10 ** 3, 'mA)')
print('Ib = ', Ib*10**6, 'uA')
print('Circuito de señal')
print('Ri = ', Ri)
print('Ro = ', Ro)
print('Av = ', Av)
print('Avs = ', EC.avs(0, Ro))
print('Av aprox ->(-Rca/Re) = ', EC.aproximacionGanancia(Rc))

EC.hibrido.imprimirParamtros()

