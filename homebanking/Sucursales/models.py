from django.db import models

# Create your models here.


class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.CharField(max_length=255)
    branch_name = models.CharField(max_length=255)
    branch_address = models.CharField(max_length=255)
    idDirecciones = models.ForeignKey("SujetoDireccion", on_delete=models.CASCADE)


class Direcciones(models.Model):
    idDireccion = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    provincia = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    idDirecciones = models.ForeignKey("SujetoDireccion", on_delete=models.CASCADE)


class SujetoDireccion(models.Model):
    idDirecciones = models.ForeignKey("Direcciones", on_delete=models.CASCADE)
