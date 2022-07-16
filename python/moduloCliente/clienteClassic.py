from cliente import Cliente


class ClienteClassic(Cliente):
    def __init__(self, dicc):
        maximoNegativo = 0
        cantMaxTarjetas = 1
        cantMaxChequeras = 1
        comisionTransferencia = 0.01
        maximoTransferenciaRecibida = 150000
        super().__init__(
            dicc,
            maximoNegativo,
            cantMaxTarjetas,
            cantMaxChequeras,
            comisionTransferencia,
            maximoTransferenciaRecibida,
            puedeComprarDolar=False,
        )
