from TBJ.HibridoPi import HibridoPi


class BaseComun:
    """Clase que crea con algunas funciones basicas de un base común
    el cual tiene la base con capacitores de desacople.
    Además crea un modelo hibrido pi el cual se inicializa con Va=100"""
    Va = 100

    def __init__(self, Re, Icq, beta):
        self.hibrido = HibridoPi(beta, self.Va, Icq)
        self.Re = Re


    def setIcq(self, Icq):
        self.hibrido.Icq = Icq

    def setBeta(self, beta):
        self.hibrido.beta = beta

    def setVa(self, Va):
        self.hibrido.Va = Va

    def Roc(self, Rs, Rb):
        RE = paralelo(Rs, self.Re)
        return self.hibrido.ro * (1 + self.hibrido.beta * RE / (RE + self.hibrido.rpi + Rb))

    def Rie(self):
        return 1 / self.hibrido.gm

    def gananciaAv(self, Rca):
        return self.hibrido.gm * Rca

    def gananciaAvs(self,  Rs,Rca):
        # ri es aprox rie
        return self.Rie()/(self.Rie() +Rs)*self.gananciaAv(Rca)
def paralelo(R1, R2):
    """Paralelo entre dos resistencias"""
    return (R2 * R1) / (R1 + R2)
