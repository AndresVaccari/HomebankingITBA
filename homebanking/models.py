# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ClientesCliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    customer_surname = models.CharField(max_length=255)
    customer_dni = models.CharField(db_column='customer_DNI', max_length=9)  # Field name made lowercase.
    dob = models.CharField(max_length=10)
    branch_id = models.ForeignKey('SucursalesSucursal', models.DO_NOTHING)
    iddirecciones = models.ForeignKey('SucursalesSujetodireccion', models.DO_NOTHING, db_column='idDirecciones_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Clientes_cliente'


class CuentasCuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    balance = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    iban = models.CharField(max_length=255)
    limiteextracciondiario = models.DecimalField(db_column='limiteExtraccionDiario', max_digits=10, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    limitetransferenciarecibida = models.DecimalField(db_column='limiteTransferenciaRecibida', max_digits=10, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    costortransferenciarecibida = models.DecimalField(db_column='costorTransferenciaRecibida', max_digits=10, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    saldodescubiertodisponible = models.DecimalField(db_column='saldoDescubiertoDisponible', max_digits=10, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    tipocuenta = models.CharField(db_column='tipoCuenta', max_length=255)  # Field name made lowercase.
    customer_id = models.ForeignKey(ClientesCliente, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Cuentas_cuenta'


class CuentasEmpleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=255)
    employee_surname = models.CharField(max_length=255)
    employee_hire_date = models.CharField(max_length=10)
    employee_dni = models.CharField(db_column='employee_DNI', max_length=9)  # Field name made lowercase.
    branch_id = models.ForeignKey('SucursalesSucursal', models.DO_NOTHING)
    iddirecciones = models.ForeignKey('SucursalesSujetodireccion', models.DO_NOTHING, db_column='idDirecciones_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cuentas_empleado'


class PrestamosPrestamos(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.CharField(max_length=11)
    loan_date = models.CharField(max_length=10)
    loan_total = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    customer_id = models.ForeignKey(ClientesCliente, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Prestamos_prestamos'


class SucursalesDirecciones(models.Model):
    iddireccion = models.AutoField(db_column='idDireccion', primary_key=True)  # Field name made lowercase.
    calle = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    provincia = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    iddirecciones = models.ForeignKey('SucursalesSujetodireccion', models.DO_NOTHING, db_column='idDirecciones_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sucursales_direcciones'


class SucursalesSucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.CharField(max_length=255)
    branch_name = models.CharField(max_length=255)
    branch_address = models.CharField(max_length=255)
    iddirecciones = models.ForeignKey('SucursalesSujetodireccion', models.DO_NOTHING, db_column='idDirecciones_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sucursales_sucursal'


class SucursalesSujetodireccion(models.Model):
    iddirecciones = models.ForeignKey(SucursalesDirecciones, models.DO_NOTHING, db_column='idDirecciones_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sucursales_sujetodireccion'


class TarjetasMarca(models.Model):
    marcaid = models.AutoField(db_column='marcaID', primary_key=True)  # Field name made lowercase.
    marca = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Tarjetas_marca'


class TarjetasMovimiento(models.Model):
    movimientoid = models.AutoField(db_column='movimientoID', primary_key=True)  # Field name made lowercase.
    monto = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    tipomovimiento = models.CharField(db_column='tipoMovimiento', max_length=255)  # Field name made lowercase.
    created_at = models.CharField(max_length=10)
    account_id = models.ForeignKey(CuentasCuenta, models.DO_NOTHING, db_column='account_ID_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tarjetas_movimiento'


class TarjetasTarjeta(models.Model):
    numerotarjeta = models.CharField(db_column='numeroTarjeta', primary_key=True, max_length=16)  # Field name made lowercase.
    cvv = models.CharField(db_column='CVV', max_length=3)  # Field name made lowercase.
    fechaotorgamiento = models.CharField(db_column='fechaOtorgamiento', max_length=10)  # Field name made lowercase.
    fechaexpiracion = models.CharField(db_column='fechaExpiracion', max_length=10)  # Field name made lowercase.
    customer_id = models.ForeignKey(ClientesCliente, models.DO_NOTHING, db_column='customer_ID_id')  # Field name made lowercase.
    marcaid = models.ForeignKey(TarjetasMarca, models.DO_NOTHING, db_column='marcaID_id')  # Field name made lowercase.
    tipotarjetaid = models.ForeignKey('TarjetasTipotarjeta', models.DO_NOTHING, db_column='tipoTarjetaID_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tarjetas_tarjeta'


class TarjetasTipotarjeta(models.Model):
    tipotarjetaid = models.AutoField(db_column='tipoTarjetaID', primary_key=True)  # Field name made lowercase.
    tipotarjeta = models.CharField(db_column='tipoTarjeta', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tarjetas_tipotarjeta'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
