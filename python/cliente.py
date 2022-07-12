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
        maximoExtraccion,
        maximoNegativo,
        puedeCrearChequera,
        puedeCrearTarjeta,
        puedeComprarDolar,
        cantMaxTarjetas,
        cantMaxChequeras,
        comisionTransferencia,
        maximoRetirarCajero,
    ):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__numeroCliente = numeroCliente
        self.__dni = dni
        self.__direccion = direccion
        self.__transacciones = []
        self.__saldo = 0
        self.__maximoExtraccion = maximoExtraccion
        self.__maximoNegativo = maximoNegativo
        self.__puedeCrearChequera = puedeCrearChequera
        self.__puedeCrearTarjeta = puedeCrearTarjeta
        self.__puedeComprarDolar = puedeComprarDolar
        self.__cantMaxTarjetas = cantMaxTarjetas
        self.__cantMaxChequeras = cantMaxChequeras
        self.__comisionTransferencia = comisionTransferencia
        self.__maximoRetirarCajero = maximoRetirarCajero
        self.__totalTarjetasDeCretido = 0
        self.__totalChequeras = 0

    def agregarTransaccion(self, transaccion):
        self.__transacciones.append(transaccion)

    def transferencia(self, monto, cuentaDestino):
        if self.__saldo >= monto:
            self.__saldo -= monto
            cuentaDestino.agregarSaldo(monto - monto * self.__comisionTransferencia)
            return True

    def agregarSaldo(self, saldo):
        self.__saldo += saldo

    def retirarCajero(self, saldo):
        if saldo > self.__maximoRetirarCajero:
            raise Exception("El monto es mayor al máximo permitido")
        else:
            self.__saldo -= saldo
            return True

    def getPuedeCrearChequera(self):
        return self.__puedeCrearChequera

    def getPuedeCrearTarjeta(self):
        return self.__puedeCrearTarjeta

    def getPuedeComprarDolar(self):
        return self.__puedeComprarDolar

    def getMaximoExtraccion(self):
        return self.__maximoExtraccion

    def getMaximoNegativo(self):
        return self.__maximoNegativo

    def getSaldo(self):
        return self.__saldo

    def getNumeroCliente(self):
        return self.__numeroCliente

    def getTotalTarjetasDeCretido(self):
        return self.__totalTarjetasDeCretido

    def getTotalChequeras(self):
        return self.__totalChequeras
