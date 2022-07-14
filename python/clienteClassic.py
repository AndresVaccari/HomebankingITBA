from cliente import Cliente


class ClienteClassic(Cliente):
    def __init__(self, nombre, apellido, dni, direccion, telefono, email):
        maximoNegativo = 0
        comisionTransferencia = 0.01
        maximoRetirarCajero = 150000
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
