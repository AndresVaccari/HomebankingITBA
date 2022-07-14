from cliente import Cliente


class ClienteClassic(Cliente):
    def __init__(self, nombre, apellido, dni, direccion, telefono, email):
        maximoNegativo = 0
        cantMaxTarjetas = 0
        cantMaxChequeras = 0
        comisionTransferencia = 0.01
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
