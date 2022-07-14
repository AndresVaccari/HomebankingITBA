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
            maximoNegativo,
            comisionTransferencia,
            maximoRetirarCajero,
        )

