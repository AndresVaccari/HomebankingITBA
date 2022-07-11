from numpy import Infinity
from cliente import Cliente


class ClienteBlack(Cliente):
    def __init__(self, nombre, apellido, dni, direccion, telefono, email):
        maximoExtraccion = 100000
        maximoNegativo = -10000
        puedeCrearChequera = True
        puedeCrearTarjeta = True
        puedeComprarDolar = True
        cantMaxTarjetas = 5
        cantMaxChequeras = 2
        comisionTransferencia = 0
        maximoTransferencia = Infinity
        super().__init__(
            nombre,
            apellido,
            dni,
            direccion,
            telefono,
            email,
            maximoExtraccion,
            maximoNegativo,
            puedeCrearChequera,
            puedeCrearTarjeta,
            puedeComprarDolar,
            cantMaxTarjetas,
            cantMaxChequeras,
            comisionTransferencia,
            maximoTransferencia,
        )
