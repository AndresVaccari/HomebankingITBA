from cliente import Cliente


class ClienteClassic(Cliente):
    def __init__(self, nombre, apellido, dni, direccion, telefono, email):
        maximoExtraccion = 20000
        maximoNegativo = -10000
        puedeCrearChequera = True
        puedeCrearTarjeta = True
        puedeComprarDolar = True
        comisionTransferencia = 0.005
        maximoTransferencia = 500000
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
            maximoTransferencia,
        )
