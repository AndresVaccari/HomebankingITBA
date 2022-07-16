class RazonAltaChequera:
    def resolver(self, cliente, cantidadChequeras):
        if cliente.pueder_crear_tarjeta_credito(cantidadChequeras):
            return "Puede crear tarjeta de credito"
        else:
            return "Cantidad maxima de tarjetas de credito alcanzada"
