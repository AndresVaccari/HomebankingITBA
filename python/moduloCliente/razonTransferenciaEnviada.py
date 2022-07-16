class RazonTransferenciaEnviada:
    def resolver(self, cliente, SaldoEnCuenta, MontoEnviado):
        if cliente.SaldoEnCuenta > MontoEnviado():
            return "Puede realizar la transferencia"
        else:
            return "No puede realizar la transferencia, el monto enviado supera el saldo"