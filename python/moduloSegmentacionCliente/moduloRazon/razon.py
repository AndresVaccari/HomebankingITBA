from .tiposRazones.razonAltaChequera import RazonAltaChequera
from .tiposRazones.razonAltaTarjetaCredito import RazonAltaTarjetaCredito
from .tiposRazones.razonCompraDolar import RazonCompraDolar
from .tiposRazones.razonRetiroEfectivo import RazonRetiroEfectivo
from .tiposRazones.razonTransferenciaRecibida import RazonTransferenciaRecibida
from .tiposRazones.razonTransferenciaEnviada import RazonTransferenciaEnviada


class Razon:
    def __init__(self, dicc, cliente):
        if dicc["estado"] == "RECHAZADA":
            if dicc["tipo"] == "ALTA_CHEQUERA":
                self.__razon = RazonAltaChequera(cliente, dicc["totalChequerasActualmente"])
            elif dicc["tipo"] == "ALTA_TARJETA_CREDITO":
                self.__razon = RazonAltaTarjetaCredito(cliente, dicc["totalTarjetasDeCreditoActualmente"])
            elif dicc["tipo"] == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
                self.__razon = RazonRetiroEfectivo(dicc["monto"], dicc["cupoDiarioRestante"])
                pass
            elif dicc["tipo"] == "COMPRA_DOLAR":
                self.__razon = RazonCompraDolar(cliente)
            elif dicc["tipo"] == "TRANSFERENCIA_ENVIADA":
                self.__razon = RazonTransferenciaEnviada(dicc["saldoEnCuenta"], dicc["monto"])
                pass
            elif dicc["tipo"] == "TRANSFERENCIA_RECIBIDA":
                self.__razon = RazonTransferenciaRecibida(cliente, dicc["monto"])
                pass
        else:
            self.__razon = "No se puede realizar la operacion"

    def getRazon(self):
        if isinstance(self.__razon, str):
            return "OK"
        else:
            return f"{self.__razon.razon()}"
