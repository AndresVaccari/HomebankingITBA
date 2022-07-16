class RazonRetiroEfectivo:
    def __init__(self, cantidadARetirar, MontoMaximo):
        if cantidadARetirar < MontoMaximo:
            self.__razon = "Puede retirar efectivo"
        else:
            self.__razon = "Cantidad maxima de retiro de efectivo alcanzada"

    def razon(self):
        return self.__razon        
