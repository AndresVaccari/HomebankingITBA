from cliente import Cliente


class ClienteBlack(Cliente):
    def __init__(self, nombre, apellido, dni, direccion, telefono, email):
        maximoNegativo = -10000
        cantMaxTarjetas = 5
        cantMaxChequeras = 2
        comisionTransferencia = 0
        super().__init__(
            nombre,
            apellido,
            dni,
            direccion,
            telefono,
            email,
            maximoNegativo,
            cantMaxTarjetas,
            cantMaxChequeras,
            comisionTransferencia,
        )
