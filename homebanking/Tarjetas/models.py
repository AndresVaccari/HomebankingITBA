from django.db import models

# Create your models here.


class Tarjeta(models.Model):
    numeroTarjeta = models.CharField(max_length=16, primary_key=True)
    marcaID = models.ForeignKey("Marca", on_delete=models.CASCADE)
    CVV = models.CharField(max_length=3)
    fechaOtorgamiento = models.CharField(max_length=10)
    fechaExpiracion = models.CharField(max_length=10)
    tipoTarjetaID = models.ForeignKey("TipoTarjeta", on_delete=models.CASCADE)
    customer_ID = models.ForeignKey("Cliente", on_delete=models.CASCADE)


class Marca(models.Model):
    marcaID = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=255)


class TipoTarjeta(models.Model):
    tipoTarjetaID = models.AutoField(primary_key=True)
    tipoTarjeta = models.CharField(max_length=255)


class Movimiento(models.Model):
    movimientoID = models.AutoField(primary_key=True)
    account_ID = models.ForeignKey("Cuenta", on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=30, decimal_places=2)
    tipoMovimiento = models.CharField(max_length=255)
    created_at = models.CharField(max_length=10)
