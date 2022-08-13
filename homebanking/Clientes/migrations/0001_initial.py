# Generated by Django 4.0.6 on 2022-08-13 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuditoriaCuenta',
            fields=[
                ('auditoria_id', models.AutoField(primary_key=True, serialize=False)),
                ('old_id', models.IntegerField(blank=True, null=True)),
                ('new_id', models.IntegerField(blank=True, null=True)),
                ('old_balance', models.IntegerField(blank=True, null=True)),
                ('new_balance', models.IntegerField(blank=True, null=True)),
                ('old_iban', models.IntegerField(blank=True, null=True)),
                ('new_iban', models.IntegerField(blank=True, null=True)),
                ('old_type', models.IntegerField(blank=True, null=True)),
                ('new_type', models.IntegerField(blank=True, null=True)),
                ('user_action', models.IntegerField(blank=True, null=True)),
                ('created_at', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'auditoria_cuenta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codename', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
                ('first_name', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.TextField()),
                ('customer_surname', models.TextField()),
                ('customer_dni', models.TextField(db_column='customer_DNI', unique=True)),
                ('dob', models.TextField(blank=True, null=True)),
                ('branch_id', models.IntegerField()),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('balance', models.IntegerField()),
                ('iban', models.TextField()),
                ('limiteextracciondiario', models.TextField(blank=True, db_column='limiteExtraccionDiario', null=True)),
                ('limitetransferenciarecibida', models.TextField(blank=True, db_column='limiteTransferenciaRecibida', null=True)),
                ('costortransferenciarecibida', models.TextField(blank=True, db_column='costorTransferenciaRecibida', null=True)),
                ('saldodescubiertodisponible', models.TextField(blank=True, db_column='saldoDescubiertoDisponible', null=True)),
                ('tipocuenta', models.TextField(blank=True, db_column='tipoCuenta', null=True)),
            ],
            options={
                'db_table': 'cuenta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Direcciones',
            fields=[
                ('iddireccion', models.AutoField(db_column='idDireccion', primary_key=True, serialize=False)),
                ('calle', models.TextField()),
                ('numero', models.TextField()),
                ('ciudad', models.TextField()),
                ('provincia', models.TextField()),
                ('pais', models.TextField()),
            ],
            options={
                'db_table': 'direcciones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('change_message', models.TextField()),
                ('action_flag', models.PositiveSmallIntegerField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_name', models.TextField()),
                ('employee_surname', models.TextField()),
                ('employee_hire_date', models.TextField()),
                ('employee_dni', models.TextField(db_column='employee_DNI')),
                ('branch_id', models.IntegerField()),
            ],
            options={
                'db_table': 'empleado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Marcastarjeta',
            fields=[
                ('marcaid', models.AutoField(db_column='marcaID', primary_key=True, serialize=False)),
                ('nombremarca', models.TextField(db_column='nombreMarca')),
            ],
            options={
                'db_table': 'marcasTarjeta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Movimientos',
            fields=[
                ('movimientoid', models.AutoField(db_column='movimientoID', primary_key=True, serialize=False)),
                ('account_id', models.IntegerField()),
                ('monto', models.IntegerField()),
                ('tipomovimiento', models.TextField(db_column='tipoMovimiento')),
                ('created_at', models.TextField()),
            ],
            options={
                'db_table': 'movimientos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('loan_id', models.AutoField(primary_key=True, serialize=False)),
                ('loan_type', models.TextField()),
                ('loan_date', models.TextField()),
                ('loan_total', models.IntegerField()),
                ('customer_id', models.IntegerField()),
            ],
            options={
                'db_table': 'prestamo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('branch_id', models.AutoField(primary_key=True, serialize=False)),
                ('branch_number', models.BinaryField()),
                ('branch_name', models.TextField()),
                ('branch_address_id', models.IntegerField()),
            ],
            options={
                'db_table': 'sucursal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sujetodireccion',
            fields=[
                ('iddirecciones', models.AutoField(db_column='idDirecciones', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'sujetoDireccion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numerotarjeta', models.TextField(db_column='numeroTarjeta')),
                ('cvv', models.TextField(db_column='CVV')),
                ('fechaotorgamiento', models.TextField(db_column='fechaOtorgamiento')),
                ('fechaexpiracion', models.TextField(db_column='fechaExpiracion')),
                ('customer_id', models.IntegerField()),
            ],
            options={
                'db_table': 'tarjeta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tiposcliente',
            fields=[
                ('tipoid', models.AutoField(db_column='tipoID', primary_key=True, serialize=False)),
                ('cantidadmaxchequeras', models.IntegerField(db_column='cantidadMaxChequeras')),
                ('cantidadmaxtarjetas', models.IntegerField(db_column='cantidadMaxTarjetas')),
                ('puedecrearchequera', models.IntegerField(db_column='puedeCrearChequera')),
                ('puedecreartarjetacredito', models.IntegerField(db_column='puedeCrearTarjetaCredito')),
                ('puedecomprardolar', models.IntegerField(db_column='puedeComprarDolar')),
            ],
            options={
                'db_table': 'tiposCliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tipotarjeta',
            fields=[
                ('tipotarjetaid', models.AutoField(db_column='tipoTarjetaID', primary_key=True, serialize=False)),
                ('nombretipo', models.TextField(db_column='nombreTipo')),
            ],
            options={
                'db_table': 'tipoTarjeta',
                'managed': False,
            },
        ),
    ]