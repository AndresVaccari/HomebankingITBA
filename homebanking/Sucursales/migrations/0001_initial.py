# Generated by Django 4.0.6 on 2022-08-10 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direcciones',
            fields=[
                ('idDireccion', models.AutoField(primary_key=True, serialize=False)),
                ('calle', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=255)),
                ('ciudad', models.CharField(max_length=255)),
                ('provincia', models.CharField(max_length=255)),
                ('pais', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SujetoDireccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idDirecciones', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sucursales.direcciones')),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('branch_id', models.AutoField(primary_key=True, serialize=False)),
                ('branch_number', models.CharField(max_length=255)),
                ('branch_name', models.CharField(max_length=255)),
                ('branch_address', models.CharField(max_length=255)),
                ('idDirecciones', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sucursales.sujetodireccion')),
            ],
        ),
        migrations.AddField(
            model_name='direcciones',
            name='idDirecciones',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sucursales.sujetodireccion'),
        ),
    ]
