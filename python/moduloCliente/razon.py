from razonAltaChequera import RazonAltaChequera
from razonAltaTarjetaCredito import RazonAltaTarjetaCredito
from razonCompraDolar import RazonCompraDolar
from razonRetiroEfectivo import RazonRetiroEfectivo
from razonTransferenciaRecibida import RazonTransferenciaRecibida 
from razonTransferenciaEnviada import RazonTransferenciaEnviada

class Razon:
    def __init__(self, dicc, cliente):
        if dicc["estado"] == "RECHAZADA":
            if dicc("tipo") == "ALTA_CHEQUERA":
                self.razon = RazonAltaChequera(cliente, dicc["totalChequerasActualmente"])
            elif dicc("tipo") == "ALTA_TARJETA_CREDITO":
                self.razon = RazonAltaTarjetaCredito(cliente, dicc["totalTarjetasDeCreditoActualmente"])
            elif dicc("tipo") == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
                pass
            elif dicc("tipo") == "COMPRA_DOLAR":
                self.razon = RazonCompraDolar(cliente)
            elif dicc("tipo") == "TRANSFERENCIA_ENVIADA":
                pass
            elif dicc("tipo") == "TRANSFERENCIA_RECIBIDA":
                pass
