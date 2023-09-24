class HibridoPi:

    def __init__(self, beta, Va, Icq):
        self.beta = beta
        self.Va = Va
        self.Icq = Icq
        self.ro = self.calcularRo()
        self.rpi = self.calcularRPi()
        self.gm = self.calcularGm()


    def calcularRo(self):
        self.ro = self.Va / self.Icq
        return self.ro

    def calcularGm(self):
        self.gm = self.Icq / (25.9 * 10 ** (-3))
        return self.gm

    def calcularRPi(self):
        self.rpi = self.beta / self.calcularGm()
        return self.rpi

    def imprimirParamtros(self):
        print('gm = ',self.gm*10**3,'mA/V')
        print('ro = ',self.ro,'kohms')
        print('rpi =', self.rpi,'ohms')