# Generated by Django 4.0.6 on 2022-08-13 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Clientes', '0003_cliente_iddirecciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='usuario',
            field=models.OneToOneField(blank=True, db_column='usuario', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
