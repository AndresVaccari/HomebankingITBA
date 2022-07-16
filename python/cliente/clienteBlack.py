from cliente import Cliente


class ClienteBlack(Cliente):
    def __init__(self, dicc):
        maximoNegativo = -10000
        cantMaxTarjetas = 5
        cantMaxChequeras = 2
        comisionTransferencia = 0
        super().__init__(
            dicc,
            maximoNegativo,
            cantMaxTarjetas,
            cantMaxChequeras,
            comisionTransferencia,
            puedeComprarDolar=True,
        )
