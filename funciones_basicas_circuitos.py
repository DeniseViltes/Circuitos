def paralelo(R1, R2):
    """Paralelo entre dos resistencias"""
    return (R2 * R1) / (R1 + R2)


def thevenin_divisor_de_tension(Vcc, R1, R2):
    """Thevenin para dos resistencias, donde se toma la tension de thevenin en R1, y Rth el paralelo de las
    resistencias"""
    Rth = paralelo(R1, R2)
    Vth = Vcc * R1 / (R1 + R2)
    return [Vth, Rth]
