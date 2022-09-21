class RazonCompraDolar:
    def __init__(self, cliente, monto, saldoEnCuenta, valorDolarTurista):
        if cliente.pueder_comprar_dolar():
            if monto * valorDolarTurista > saldoEnCuenta:
                self.__razon = "No tiene suficiente saldo"
            else:
                self.__razon = "Puede comprar dolar"
        else:
            self.__razon = "Este tipo de cliente no puede comprar dolar"

    def razon(self):
        return self.__razon
