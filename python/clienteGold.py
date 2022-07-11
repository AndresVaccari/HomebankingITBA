import cliente


class ClienteClassic(cliente.Cliente):
    def __init__(self, nombre, apellido, dni, direccion, telefono, email):
        super().__init__(nombre, apellido, dni, direccion, telefono, email)
        self.__puedeCrearChequera = True
        self.__puedeCrearTarjeta = True
        self.__puedeComprarDolar = True
        self.__comisionTransferencia = 0.005
        self.__maximoTransferencia = 500000
        self.__maximoExtraccion = 20000
        self.__maximoNegativo = -10000
        self.__cantMaxTarjetas = 1
        self.__cantMaxChequeras = 1



    def transferencia(self, monto, cuentaDestino):
        if self.__saldo >= monto:
            self.__saldo -= monto
            cuentaDestino.agregarSaldo(monto - monto * self.__comisionTransferencia)
            return True

    def agregarSaldo(self, saldo):
        if saldo > self.__maximoTransferencia:
            raise Exception("El monto es mayor al máximo permitido")
        else:
            self.__saldo += saldo

    def getPuedeCrearChequera(self):
        return self.__puedeCrearChequera

    def getPuedeCrearTarjeta(self):
        return self.__puedeCrearTarjeta

    def getPuedeComprarDolar(self):
        return self.__puedeComprarDolar
