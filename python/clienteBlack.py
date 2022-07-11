import cliente


class ClienteBlack(cliente.Cliente):
    def __init__(self, nombre, apellido, dni, direccion, telefono, email):
        super().__init__(nombre, apellido, dni, direccion, telefono, email)
        self.__puedeCrearChequera = True
        self.__puedeCrearTarjeta = True
        self.__puedeComprarDolar = True
        self.__comisionTransferencia = 0
        self.cantidadMaxTarjetas = 5
        self.cantidadMaxTarjetas = 2
        self.__maximoExtracción = 100000
        self.__maximoNegativo = -10000


    def transferencia(self, monto, cuentaDestino):
        if self.__saldo >= monto:
            self.__saldo -= monto
            cuentaDestino.agregarSaldo(monto - monto * self.__comisionTransferencia)
            return True

    def agregarSaldo(self, saldo):
        self.__saldo += saldo

    def getPuedeCrearChequera(self):
        return self.__puedeCrearChequera

    def getPuedeCrearTarjeta(self):
        return self.__puedeCrearTarjeta

    def getPuedeComprarDolar(self):
        return self.__puedeComprarDolar

    def getMaximoExtracción (self):
        return self.__maximoExtracción
        
    def getMaximoNegativo (self):
        return self.__maximoNegativo


