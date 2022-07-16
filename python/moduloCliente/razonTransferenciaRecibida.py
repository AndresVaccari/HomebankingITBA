class RazonTransferenciaRecibida:
    def __init__(cliente, monto):
        if cliente.puedeRecibirTransferencia(monto):
            return "Puede recibir la transferencia"
        else:
            return "Monto maximo de transferencia recibida superado"
