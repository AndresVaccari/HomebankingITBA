from django.shortcuts import render, get_object_or_404
from django.http import Http404

from rest_framework import permissions, viewsets
from rest_framework.response import Response

from .serializers import (
    ClienteSerializer,
    TarjetaSerializer,
    UserSerializer,
    SujetoDireccionSerializer,
    TiposclienteSerializer,
    CuentaSerializer,
    PrestamosSerializer,
    TotalPrestamosSerializer,
    SucursalSerializer,
    TipoTarjetaSerializer,
    MarcasTarjetaSerializer,
    GestionPrestamosSerializer,
)
from Clientes.models import (
    Cliente,
    Sujetodireccion,
    Tiposcliente,
    Cuenta,
    Sucursal,
    Tarjeta,
    Tipotarjeta,
    Marcastarjeta,
)
from Prestamos.models import Prestamo

from django.contrib.auth.models import User

from datetime import datetime

# Create your views here.


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        queryset = User.objects.get(username=request.user)
        serializer = UserSerializer(queryset, many=False, context={"request": request})
        return Response(serializer.data)


class ClienteViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        usuario = User.objects.get(username=request.user)
        queryset = Cliente.objects.get(usuario=usuario.id)
        serializer = ClienteSerializer(queryset, many=False, context={"request": request})
        return Response(serializer.data)


class SujetoDireccionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sujetodireccion.objects.all()
    serializer_class = SujetoDireccionSerializer
    permission_classes = [permissions.IsAuthenticated]


class TiposclienteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tiposcliente.objects.all()
    serializer_class = TiposclienteSerializer
    permission_classes = [permissions.IsAuthenticated]


class CuentaViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):

        usuario = User.objects.get(username=request.user)
        cliente = Cliente.objects.get(usuario=usuario.id)
        queryset = get_object_or_404(Cuenta, customer_id=cliente.customer_id)
        serializer = CuentaSerializer(queryset, many=False, context={"request": request})
        return Response(serializer.data)


class PrestamosViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):

        usuario = User.objects.get(username=request.user)
        cliente = Cliente.objects.get(usuario=usuario.id)
        queryset = Prestamo.objects.filter(customer_id=cliente.customer_id)
        serializer = PrestamosSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)


class totalPrestamosViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TotalPrestamosSerializer

    def list(self, request):
        queryset = Prestamo.objects.all()
        serializer = TotalPrestamosSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Prestamo.objects.filter(branch_id=pk)
        serializer = TotalPrestamosSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)


class GestionPrestamosViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Prestamo.objects.all()
    serializer_class = GestionPrestamosSerializer

    def perform_create(self, serializer):
        cuentaCliente = Cuenta.objects.filter(customer_id=serializer.validated_data["customer_id"])
        if cuentaCliente.count() > 0:
            cuentaCliente = cuentaCliente.first()
            cuentaCliente.balance = cuentaCliente.balance + int(serializer.validated_data["loan_total"]) * 10
            serializer.save()
            cuentaCliente.save()
        else:
            raise Http404

    def perfom_destroy(self, serializer, pk=None):
        print(pk)
        queryset = Prestamo.objects.get(loan_id=pk)
        print("a")
        cuentaCliente = Cuenta.objects.filter(customer_id=queryset.customer_id)
        if cuentaCliente.count() > 0:
            cuentaCliente = cuentaCliente.first()
            print(cuentaCliente.balance)
            cuentaCliente.balance = cuentaCliente.balance - int(queryset.loan_total) * 10
            queryset.perfom_destroy()
            cuentaCliente.save()
        else:
            raise Http404


class SucursalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer
    permission_classes = [permissions.IsAuthenticated]


class TarjetasViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        queryset = Tarjeta.objects.all()
        serializer = TarjetaSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Tarjeta.objects.filter(customer_id=pk)
        serializer = TarjetaSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)


class TipoTarjetaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tipotarjeta.objects.all()
    serializer_class = TipoTarjetaSerializer
    permission_classes = [permissions.IsAuthenticated]


class MarcasTarjetaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Marcastarjeta.objects.all()
    serializer_class = MarcasTarjetaSerializer
    permission_classes = [permissions.IsAuthenticated]
