from rest_framework import serializers
from Clientes.models import Cliente, Cuenta, Tarjeta, Direcciones, Sucursal
from Prestamos.models import Prestamo
from django.contrib.auth.models import User


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    # usuario = serializers.HyperlinkedRelatedField(many=True, view_name="user-detail", read_only=True)

    class Meta:
        model = Cliente
        fields = "__all__"


class CuentaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cuenta
        fields = "__all__"


class PrestamosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prestamo
        fields = "__all__"


class TarjetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tarjeta
        fields = "__all__"


class DireccionesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Direcciones
        fields = "__all__"


class SucursalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sucursal
        fields = "__all__"
