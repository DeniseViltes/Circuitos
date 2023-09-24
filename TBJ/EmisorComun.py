from TBJ.HibridoPi import HibridoPi


class EmisorComun:
    """Clase que crea con algunas funciones basicas de un emisor comun
    el cual se inicializa con Re acoplado.
    Además crea un modelo hibrido pi el cual se inicializa con Va=100"""
    Va = 100

    def __init__(self, Re, Icq, beta):
        self.emisor_acoplado = True
        self.hibrido = HibridoPi(beta, self.Va, Icq)
        self.Re = Re

    def sinAcople(self):
        self.emisor_acoplado = False

    def conAcople(self):
        self.emisor_acoplado = True

    def setIcq(self, Icq):
        self.hibrido.Icq = Icq

    def setBeta(self, beta):
        self.hibrido.beta = beta

    def setVa(self, Va):
        self.hibrido.Va = Va

    def Roc(self):
        if not self.emisor_acoplado:
            return self.hibrido.ro * (1 + self.hibrido.gm * self.Re)
        else:
            return self.hibrido.ro

    def Rib(self):
        if not self.emisor_acoplado:
            return self.hibrido.rpi + self.Re * (1 + self.hibrido.beta)
        else:
            return self.hibrido.rpi

    def av(self, Rca):
        if not self.emisor_acoplado:
            return -(self.hibrido.gm * Rca) / (1 + self.hibrido.gm * self.Re)
        else:
            return -self.hibrido.gm * Rca

    def aproximacionGanancia(self, Rca):
        if not self.emisor_acoplado:
            return -Rca / self.Re
        else:
            return -self.hibrido.gm * Rca

    def avs(self, Rs, Rca):
        # ri es aprox rie
        return self.Rib()/(self.Rib() +Rs)*self.av(Rca)