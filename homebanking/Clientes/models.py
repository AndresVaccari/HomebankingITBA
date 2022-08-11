from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    customer_surname = models.CharField(max_length=255)
    customer_DNI = models.CharField(max_length=9)
    dob = models.CharField(max_length=10)
    branch_id = models.ForeignKey("Sucursales.Sucursal", on_delete=models.CASCADE)
    idDirecciones = models.ForeignKey("Sucursales.SujetoDireccion", on_delete=models.CASCADE)
