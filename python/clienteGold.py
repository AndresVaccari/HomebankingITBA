from cliente import Cliente


class ClienteGold(Cliente):
    def __init__(self, nombre, apellido, dni, direccion, telefono, email):
        maximoNegativo = -10000
        cantMaxTarjetas = 0
        cantMaxChequeras = 0
        comisionTransferencia = 0.005
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
