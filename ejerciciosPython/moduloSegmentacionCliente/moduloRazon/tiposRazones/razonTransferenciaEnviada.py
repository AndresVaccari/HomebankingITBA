class RazonTransferenciaEnviada:
    def __init__(self, SaldoEnCuenta, MontoEnviado):
        if SaldoEnCuenta > MontoEnviado:
            self.__razon = "Puede realizar la transferencia"
        else:
            self.__razon = "No puede realizar la transferencia, el monto enviado supera el saldo"

    def razon(self):
        return self.__razon
