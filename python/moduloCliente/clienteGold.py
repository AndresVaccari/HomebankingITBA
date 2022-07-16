from cliente import Cliente


class ClienteGold(Cliente):
    def __init__(self, dicc):
        maximoNegativo = -10000
        cantMaxTarjetas = 0
        cantMaxChequeras = 0
        comisionTransferencia = 0.005
        maximoTransferenciaRecibida = 500000
        super().__init__(
            dicc,
            maximoNegativo,
            cantMaxTarjetas,
            cantMaxChequeras,
            comisionTransferencia,
            maximoTransferenciaRecibida,
            puedeComprarDolar=True,
        )
