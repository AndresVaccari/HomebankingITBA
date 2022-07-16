class RazonTransferenciaEnviada:
    def resolver(self, SaldoEnCuenta, MontoEnviado):
        if SaldoEnCuenta > MontoEnviado:
            return "Puede realizar la transferencia"
        else:
            return "No puede realizar la transferencia, el monto enviado supera el saldo"
