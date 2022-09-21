class RazonRetiroEfectivo:
    def __init__(self, cantidadARetirar, MontoMaximo, saldoEnCuenta):
        if cantidadARetirar > MontoMaximo:
            self.__razon = "Cantidad maxima de retiro de efectivo alcanzada"
        elif cantidadARetirar >= saldoEnCuenta:
            self.__razon = "No hay saldo suficiente en la cuenta"
        else:
            self.__razon = "Puede retirar efectivo"

    def razon(self):
        return self.__razon
