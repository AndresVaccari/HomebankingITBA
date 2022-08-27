# Generated by Django 4.0.6 on 2022-08-27 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0005_cliente_tipocliente'),
        ('Prestamos', '0005_alter_prestamo_customer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='branch_id',
            field=models.ForeignKey(blank=True, db_column='branch_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='Clientes.sucursal'),
        ),
    ]
