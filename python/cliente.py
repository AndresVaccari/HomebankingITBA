class Cliente:
    def __init__(self, nombre, apellido, numeroCliente, dni, tipoCliente, direccion):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__numeroCliente = numeroCliente
        self.__dni = dni
        self.__tipoCliente = tipoCliente
        self.__direccion = direccion
        self.__transacciones = []

    def agregarTransaccion(self, transaccion):
        self.__transacciones.append(transaccion)
