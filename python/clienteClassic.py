from cliente import Cliente


class ClienteClassic(Cliente):
    def __init__(self, nombre, apellido, dni, direccion, telefono, email):
        maximoExtraccion = 10000
        maximoNegativo = 0
        puedeCrearChequera = False
        puedeCrearTarjeta = False
        puedeComprarDolar = False
        comisionTransferencia = 0.01
        maximoRetirarCajero = 150000
        cantMaxTarjetas = 0
        cantMaxChequeras = 0
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
        return False

    def pueder_crear_tarjeta_credito(self):
        return False

    def pueder_comprar_dolar(self):
        return False