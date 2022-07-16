class RazonAltaTarjetaCredito:
    def __init__(self, cliente, cantidadTarjetas):
        if cliente.pueder_crear_chequera(cantidadTarjetas):
            return "Puede crear chequera"
        else:
            return "Cantidad maxima de chequeras alcanzada"
