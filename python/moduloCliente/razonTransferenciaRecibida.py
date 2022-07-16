class RazonTransferenciaRecibida:
    def __init__(cliente, monto):
        if cliente.puedeRecibirTransferencia(monto):
            self.__razon = "Puede recibir la transferencia"
        else:
            self.__razon =  "Monto maximo de transferencia recibida superado"

    def razon(self):
        return self.__razon        
