from numpy import Infinity
from .cliente.cliente import Cliente

# Definicion de la clase ClienteBlack
class ClienteBlack(Cliente):
    def __init__(self, dicc):
        maximoNegativo = -10000
        cantMaxTarjetas = 5
        cantMaxChequeras = 2
        comisionTransferencia = 0
        maximoTransferenciaRecibida = Infinity
        super().__init__(
            dicc,
            maximoNegativo,
            cantMaxTarjetas,
            cantMaxChequeras,
            comisionTransferencia,
            maximoTransferenciaRecibida,
            puedeComprarDolar=True,
        )
