class RazonAltaChequera:
    def __init__(self, cliente, cantidadChequeras):
        if cliente.pueder_crear_chequera(cantidadChequeras):
            self.__razon = "Puede crear chequera"
        else:
            self.__razon = "Cantidad maxima de chequeras alcanzada"

    def razon(self):
        return self.__razon
