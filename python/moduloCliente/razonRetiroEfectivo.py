class RazonRetiroEfectivo:
    def __init__(self, cantidadARetirar, MontoMaximo):
        if cantidadARetirar < MontoMaximo:
            return "Puede retirar efectivo"
        else:
            return "Cantidad maxima de retiro de efectivo alcanzada"
