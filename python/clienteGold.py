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
            maximoNegativo,
            comisionTransferencia,
        )


