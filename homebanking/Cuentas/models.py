from django.db import models

# Create your models here.

class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.CharField(max_length=255)
    balance = models.CharField(max_length=None)
    iban = models.CharField(max_length=255)
    limiteExtraccionDiario = models.DecimalField(max_digits=5, decimal_places=2)
    limiteTransferenciaRecibida = models.DecimalField(max_digits=5, decimal_places=2)
    costorTransferenciaRecibida = models.DecimalField(max_digits=5, decimal_places=2)
    saldoDescubiertoDisponible = models.DecimalField(max_digits=5, decimal_places=2)
    tipoCuenta = models.CharField(max_length=None)