from xml.dom.minidom import Element
from numpy import double
import requests
import json

RESULTADO = requests.get("https://www.dolarsi.com/api/api.php?type=valoresprincipales")
VALORES_DOLAR = json.loads(RESULTADO.text)
VALOR_DOLAR_TURISTA = double(
    (list(filter(lambda valor: valor["casa"]["nombre"] == "Dolar turista", VALORES_DOLAR))[0]["casa"]["venta"]).replace(
        ",", "."
    )
)


class RazonCompraDolar:
    def __init__(self, cliente, monto, saldoEnCuenta):
        if cliente.pueder_comprar_dolar():
            if monto * VALOR_DOLAR_TURISTA > saldoEnCuenta:
                self.__razon = "No tiene suficiente saldo"
            else:
                self.__razon = "Puede comprar dolar"
        else:
            self.__razon = "Este tipo de cliente no puede comprar dolar"

    def razon(self):
        return self.__razon
