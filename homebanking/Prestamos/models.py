from django.db import models

# Create your models here.
class Prestamos(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.CharField(max_length=11)
    loan_date = models.CharField(max_length=10)
    loan_total = models.CharField(max_length= 9)
    customer_id = models.ForeignKey("Cliente", on_delete=models.CASCADE)