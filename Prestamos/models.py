from django.db import models

# Create your models here.


class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.ForeignKey("Clientes.cliente", on_delete=models.CASCADE, db_column="customer_id")
    branch_id = models.ForeignKey(
        "Clientes.sucursal", on_delete=models.CASCADE, db_column="branch_id", null=True, blank=True
    )

    class Meta:
        db_table = "prestamo"
