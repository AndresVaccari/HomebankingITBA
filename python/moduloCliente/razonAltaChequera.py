class RazonAltaChequera:
    def resolver(self, cliente, cantidadChequeras):
        if cliente.pueder_crear_chequera(cantidadChequeras):
            return "Puede crear chequera"
        else:
            return "Cantidad maxima de chequeras alcanzada"
