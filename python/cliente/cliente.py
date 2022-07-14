from abc import ABC, abstractmethod

# Clase abstracta que representa a un cliente
class Cliente(ABC):
    def __init__(
        self,
        nombre,
        apellido,
        numeroCliente,
        dni,
        direccion,
        maximoNegativo,
        cantMaxTarjetas,
        cantMaxChequeras,
        comisionTransferencia,
    ):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__numeroCliente = numeroCliente
        self.__dni = dni
        self.__direccion = direccion
        self.__transacciones = []
        self.__maximoNegativo = maximoNegativo
        self.__cantMaxTarjetas = cantMaxTarjetas
        self.__cantMaxChequeras = cantMaxChequeras
        self.__comisionTransferencia = comisionTransferencia

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
