class RazonCompraDolar:
    def resolver(self, cliente):
        if cliente.puede_comprar_dolar():
            return "Puede comprar dolar"
        else:
            return "Este tipo de cliente no puede comprar dolar"