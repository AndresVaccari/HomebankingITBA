from operator import truediv
from numpy import Infinity
from cliente import Cliente


class ClienteBlack(Cliente):
    def __init__(self, nombre, apellido, dni, direccion, telefono, email):
        maximoNegativo = -10000
        cantMaxTarjetas = 5
        cantMaxChequeras = 2
        comisionTransferencia = 0
        super().__init__(
            nombre,
            apellido,
            dni,
            direccion,
            telefono,
            email,
            maximoNegativo,
            cantMaxTarjetas,
            cantMaxChequeras,
            comisionTransferencia,
        )

    def pueder_crear_chequera(self, totalChequeras):
        if totalChequeras < self.__cantMaxChequeras:
            return True
        else:
            return False

    def pueder_crear_tarjeta_credito(self, totalTarjetasDeCredito):
        if totalTarjetasDeCredito < self.__cantMaxTarjetas:
            return True
        else:
            return False

    def pueder_comprar_dolar(self):
        return True
