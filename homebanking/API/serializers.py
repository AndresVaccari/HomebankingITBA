from cgitb import lookup
from rest_framework import serializers

from Clientes.models import (
    Cliente,
    Cuenta,
    Tarjeta,
    Direcciones,
    Sucursal,
    Sujetodireccion,
    Tiposcliente,
    Tipotarjeta,
    Marcastarjeta,
)
from Prestamos.models import Prestamo

from django.contrib.auth.models import User
from django.http import Http404


# from homebanking.Clientes.models import Sujetodireccion


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    usuario = serializers.HyperlinkedRelatedField(
        many=False,
        view_name="usuarios-detail",
        read_only=True,
    )
    # iddirecciones = serializers.HyperlinkedRelatedField(many=True, view_name="Sujetodireccion-list", read_only=True)

    class Meta:
        model = Cliente
        fields = "__all__"


class SujetoDireccionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sujetodireccion
        fields = "__all__"


class TiposclienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tiposcliente
        fields = "__all__"


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class CuentaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cuenta
        fields = ["customer_id", "balance", "tipocuenta"]


class PrestamosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prestamo
        fields = ["customer_id", "loan_type", "loan_total"]


class GestionPrestamosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = "__all__"

    def create(self, validated_data):
        cuentaCliente = Cuenta.objects.filter(customer_id=validated_data["customer_id"])
        if cuentaCliente.count() > 0:
            cuentaCliente = cuentaCliente.first()
            cuentaCliente.balance = cuentaCliente.balance + int(validated_data["loan_total"]) * 10
            cuentaCliente.save()
        else:
            raise Http404
        return Prestamo.objects.create(**validated_data)


class TotalPrestamosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prestamo
        fields = ["branch_id", "loan_total"]


class TarjetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tarjeta
        fields = ["numerotarjeta", "cvv", "customer_id", "tipotarjetaid", "marcaid"]


class TipoTarjetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipotarjeta
        fields = "__all__"


class MarcasTarjetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marcastarjeta
        fields = "__all__"


class DireccionesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Direcciones
        fields = "__all__"


class SucursalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sucursal
        fields = "__all__"
