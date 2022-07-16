class RazonRetiroEfectivo:
    def resolver(self, cliente, cantidadARetirar, MontoMaximo):
        if cliente.cantidadARetirar > MontoMaximo():
            return "Puede retirar efectivo"
        else:
            return "Cantidad maxima de retiro de efectivo alcanzada"

