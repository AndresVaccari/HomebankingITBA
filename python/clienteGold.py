from cliente import Cliente


class ClienteGold(Cliente):
    def __init__(self, nombre, apellido, dni, direccion, telefono, email):
        maximoExtraccion = 20000
        maximoNegativo = -10000
        puedeCrearChequera = True
        puedeCrearTarjeta = True
        puedeComprarDolar = True
        comisionTransferencia = 0.005
        maximoRetirarCajero = 500000
        cantMaxTarjetas = 1
        cantMaxChequeras = 1
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
        if self.__totalChequeras < 1:
            return True
        else:
            return False

    def pueder_crear_tarjeta_credito(self):
        if self.__totalTarjetasDeCretido < 1:
            return True
        else:
            return False

    def pueder_comprar_dolar(self):
        return True
