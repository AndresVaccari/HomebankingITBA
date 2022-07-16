from datetime import datetime


class Transaccion:
    def __init__(self, numero, tipo, id_cuenta, cliente):
        self.__estado = "Pendiente"
        self.__tipo = tipo
        self.__cuentaNumero = cliente.getNumeroCliente()
        self.__cupoDiarioRestante = None
        self.__monto = None
        self.__fecha = datetime.now()
        self.__numero = numero
        self.__saldoEnCuenta = cliente.getSaldo()
        self.__id_cuenta = id_cuenta
        self.__numero = None
        self.__totalTarjetasDeCretidoActualmente = cliente.getTotalTarjetasDeCretido()
        self.__totalChequerasActualmente = cliente.getTotalChequeras()
