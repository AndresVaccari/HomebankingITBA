from abc import ABC, abstractmethod

# Clase abstracta que representa a un cliente
class Cliente(ABC):
    def __init__(
        self,
        dicc,
        maximoNegativo,
        cantMaxTarjetas,
        cantMaxChequeras,
        comisionTransferencia,
        puedeComprarDolar,
    ):
        self.__nombre = dicc["nombre"]
        self.__apellido = dicc["apellido"]
        self.__numeroCliente = dicc["numero"]
        self.__dni = dicc["dni"]
        self.__direccion = dicc["direccion"]
        self.__transacciones = dicc["transacciones"]
        self.__maximoNegativo = maximoNegativo
        self.__cantMaxTarjetas = cantMaxTarjetas
        self.__cantMaxChequeras = cantMaxChequeras
        self.__comisionTransferencia = comisionTransferencia
        self.__puedeComprarDolar = puedeComprarDolar

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
        return self.__puedeComprarDolar

    def getTransacciones(self):
        return self.__transacciones
