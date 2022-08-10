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


class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=255)
    employee_surname = models.CharField(max_length=255)
    employee_hire_date = models.CharField(max_length=10)
    employee_DNI = models.CharField(max_length=9)
    branch_id = models.ForeignKey("Sucursal", on_delete=models.CASCADE)
    idDirecciones = models.ForeignKey("SujetoDireccion", on_delete=models.CASCADE)
