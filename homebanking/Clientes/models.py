# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuditoriaCuenta(models.Model):
    auditoria_id = models.AutoField(primary_key=True)
    old_id = models.IntegerField(blank=True, null=True)
    new_id = models.IntegerField(blank=True, null=True)
    old_balance = models.IntegerField(blank=True, null=True)
    new_balance = models.IntegerField(blank=True, null=True)
    old_iban = models.IntegerField(blank=True, null=True)
    new_iban = models.IntegerField(blank=True, null=True)
    old_type = models.IntegerField(blank=True, null=True)
    new_type = models.IntegerField(blank=True, null=True)
    user_action = models.IntegerField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "auditoria_cuenta"


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = "auth_group"


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey("AuthPermission", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_group_permissions"
        unique_together = (("group", "permission"),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey("DjangoContentType", models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "auth_permission"
        unique_together = (("content_type", "codename"),)


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
        db_table = "auth_user"


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_user_groups"
        unique_together = (("user", "group"),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_user_user_permissions"
        unique_together = (("user", "permission"),)


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column="customer_DNI", unique=True)  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()
    iddirecciones = models.ForeignKey(
        "Sujetodireccion", models.DO_NOTHING, db_column="idDirecciones", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "cliente"


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    balance = models.IntegerField()
    iban = models.TextField()
    limiteextracciondiario = models.TextField(
        db_column="limiteExtraccionDiario", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    limitetransferenciarecibida = models.TextField(
        db_column="limiteTransferenciaRecibida", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    costortransferenciarecibida = models.TextField(
        db_column="costorTransferenciaRecibida", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    saldodescubiertodisponible = models.TextField(
        db_column="saldoDescubiertoDisponible", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    tipocuenta = models.TextField(db_column="tipoCuenta", blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "cuenta"


class Direcciones(models.Model):
    iddireccion = models.AutoField(primary_key=True, db_column="idDireccion")  # Field name made lowercase.
    calle = models.TextField()
    numero = models.TextField()
    ciudad = models.TextField()
    provincia = models.TextField()
    pais = models.TextField()
    iddirecciones = models.ForeignKey(
        "Sujetodireccion", on_delete=models.CASCADE, db_column="idDirecciones"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "direcciones"


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey("DjangoContentType", models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = "django_admin_log"


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "django_content_type"
        unique_together = (("app_label", "model"),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_migrations"


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_session"


class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column="employee_DNI")  # Field name made lowercase.
    branch_id = models.IntegerField()
    iddirecciones = models.ForeignKey(
        "Sujetodireccion", on_delete=models.CASCADE, db_column="idDirecciones", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "empleado"


class Marcastarjeta(models.Model):
    marcaid = models.AutoField(db_column="marcaID", primary_key=True)  # Field name made lowercase.
    nombremarca = models.TextField(db_column="nombreMarca")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "marcasTarjeta"


class Movimientos(models.Model):
    movimientoid = models.AutoField(db_column="movimientoID", primary_key=True)  # Field name made lowercase.
    account_id = models.IntegerField()
    monto = models.IntegerField()
    tipomovimiento = models.TextField(db_column="tipoMovimiento")  # Field name made lowercase.
    created_at = models.TextField()

    class Meta:
        managed = False
        db_table = "movimientos"


class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()
    iddirecciones = models.ForeignKey(
        "Sujetodireccion", on_delete=models.CASCADE, db_column="idDirecciones", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "sucursal"


class Sujetodireccion(models.Model):
    iddirecciones = models.AutoField(db_column="idDirecciones", primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "sujetoDireccion"


class Tarjeta(models.Model):
    numerotarjeta = models.TextField(db_column="numeroTarjeta")  # Field name made lowercase.
    marcaid = models.ForeignKey(
        Marcastarjeta, on_delete=models.CASCADE, db_column="marcaID"
    )  # Field name made lowercase.
    cvv = models.TextField(db_column="CVV")  # Field name made lowercase.
    fechaotorgamiento = models.TextField(db_column="fechaOtorgamiento")  # Field name made lowercase.
    fechaexpiracion = models.TextField(db_column="fechaExpiracion")  # Field name made lowercase.
    tipotarjetaid = models.ForeignKey(
        "Tipotarjeta", on_delete=models.CASCADE, db_column="tipoTarjetaID"
    )  # Field name made lowercase.
    customer_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = "tarjeta"


class Tipotarjeta(models.Model):
    tipotarjetaid = models.AutoField(db_column="tipoTarjetaID", primary_key=True)  # Field name made lowercase.
    nombretipo = models.TextField(db_column="nombreTipo")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "tipoTarjeta"


class Tiposcliente(models.Model):
    tipoid = models.AutoField(db_column="tipoID", primary_key=True)  # Field name made lowercase.
    cantidadmaxchequeras = models.IntegerField(db_column="cantidadMaxChequeras")  # Field name made lowercase.
    cantidadmaxtarjetas = models.IntegerField(db_column="cantidadMaxTarjetas")  # Field name made lowercase.
    puedecrearchequera = models.IntegerField(db_column="puedeCrearChequera")  # Field name made lowercase.
    puedecreartarjetacredito = models.IntegerField(db_column="puedeCrearTarjetaCredito")  # Field name made lowercase.
    puedecomprardolar = models.IntegerField(db_column="puedeComprarDolar")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "tiposCliente"
