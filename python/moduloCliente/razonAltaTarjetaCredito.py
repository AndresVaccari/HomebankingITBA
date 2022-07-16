class RazonAltaTarjetaCredito:
    def __init__(self, cliente, cantidadTarjetas):
        if cliente.pueder_crear_chequera(cantidadTarjetas):
            self.__razon = "Puede crear chequera"
        else:
            self.__razon = "Cantidad maxima de chequeras alcanzada"

    def razon(self):
        return self.__razon
