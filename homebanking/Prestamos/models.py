from django.db import models

# Create your models here.
class Prestamos(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.CharField(max_length=11)
    loan_date = models.CharField(max_length=10)
    loan_total = models.DecimalField(max_digits=30, decimal_places=2)
    customer_id = models.ForeignKey("Cliente", on_delete=models.CASCADE)
