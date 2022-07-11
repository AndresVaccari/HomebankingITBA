class Transaccion:
    def __init__(self, id, monto, fecha, tipo, id_cuenta):
        self.id = id
        self.monto = monto
        self.fecha = fecha
        self.tipo = tipo
        self.id_cuenta = id_cuenta

    def __str__(self):
        return "Transaccion: {}, {}, {}, {}, {}".format(
            self.id, self.monto, self.fecha, self.tipo, self.id_cuenta
        )
