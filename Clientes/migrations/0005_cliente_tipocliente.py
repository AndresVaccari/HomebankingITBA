# Generated by Django 4.0.6 on 2022-08-14 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0004_cliente_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='tipoCliente',
            field=models.ForeignKey(blank=True, db_column='tipoCliente', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Clientes.tiposcliente'),
        ),
    ]