from rest_framework import serializers
from Clientes.models import Cliente, Cuenta, Tarjeta, Direcciones, Sucursal, Sujetodireccion, Tiposcliente
from Prestamos.models import Prestamo
from django.contrib.auth.models import User

# from homebanking.Clientes.models import Sujetodireccion


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    # usuario = serializers.HyperlinkedRelatedField(many=True, view_name="user-list", read_only=True)
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
