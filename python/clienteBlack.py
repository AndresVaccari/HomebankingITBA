from operator import truediv
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
        maximoRetirarCajero = Infinity
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
            maximoRetirarCajero,
        )

    def pueder_crear_chequera(self):
        if self.__totalChequeras < 2:
            return True
        else:
            return False

    def pueder_crear_tarjeta_credito(self):
        if self.__totalTarjetasDeCretido < 5:
            return True
        else:
            return False

    def pueder_comprar_dolar(self):
        return True
