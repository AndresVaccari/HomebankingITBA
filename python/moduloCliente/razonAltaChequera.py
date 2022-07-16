class RazonAltaChequera:
    def __init__(self, cliente, cantidadChequeras):
        if cliente.pueder_crear_tarjeta_credito(cantidadChequeras):
            self.__razon = "Puede crear tarjeta de credito"
        else:
            self.__razon = "Cantidad maxima de tarjetas de credito alcanzada"

    def razon(self):
        return self.__razon
