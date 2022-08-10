from django.db import models

# Create your models here.


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey("Cliente", on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=30, decimal_places=2)
    iban = models.CharField(max_length=255)
    limiteExtraccionDiario = models.DecimalField(max_digits=5, decimal_places=2)
    limiteTransferenciaRecibida = models.DecimalField(max_digits=5, decimal_places=2)
    costorTransferenciaRecibida = models.DecimalField(max_digits=5, decimal_places=2)
    saldoDescubiertoDisponible = models.DecimalField(max_digits=5, decimal_places=2)
    tipoCuenta = models.CharField(max_length=255)
