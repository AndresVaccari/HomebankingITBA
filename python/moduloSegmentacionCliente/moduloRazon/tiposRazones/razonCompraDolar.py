class RazonCompraDolar:
    def __init__(self, cliente):
        if cliente.pueder_comprar_dolar():
            self.__razon = "Puede comprar dolar"
        else:
            self.__razon = "Este tipo de cliente no puede comprar dolar"

    def razon(self):
        return self.__razon
