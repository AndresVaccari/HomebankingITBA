from ast import Return
from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from rest_framework import permissions, viewsets, status
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
    DireccionesSerializer,
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
    Direcciones,
)
from Prestamos.models import Prestamo

from django.contrib.auth.models import User

from datetime import datetime

# Create your views here.


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get"]

    def list(self, request):
        queryset = User.objects.get(username=request.user)
        serializer = UserSerializer(queryset, many=False, context={"request": request})
        return Response(serializer.data)


class ClienteViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get"]

    def list(self, request):
        usuario = User.objects.get(username=request.user)
        if usuario.is_staff:
            queryset = Cliente.objects.all()
            serializer = ClienteSerializer(queryset, many=True, context={"request": request})
        else:
            queryset = Cliente.objects.get(usuario=usuario.id)
            serializer = ClienteSerializer(queryset, many=False, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        usuario = User.objects.get(username=request.user)
        if usuario.is_staff:
            queryset = Cliente.objects.get(pk=pk)
            serializer = ClienteSerializer(queryset, many=False, context={"request": request})
        else:
            queryset = Cliente.objects.get(usuario=usuario.id)
            serializer = ClienteSerializer(queryset, many=False, context={"request": request})
        return Response(serializer.data)


class SujetoDireccionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sujetodireccion.objects.all()
    serializer_class = SujetoDireccionSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get"]


class TiposclienteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tiposcliente.objects.all()
    serializer_class = TiposclienteSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get"]


class CuentaViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get"]

    def list(self, request):
        usuario = User.objects.get(username=request.user)
        if usuario.is_staff:
            queryset = Cuenta.objects.all()
            serializer = CuentaSerializer(queryset, many=True, context={"request": request})
        else:
            cliente = Cliente.objects.get(usuario=usuario.id)
            queryset = Cuenta.objects.filter(customer_id=cliente.customer_id)
            serializer = CuentaSerializer(queryset, many=True, context={"request": request})
        if serializer.data:
            return Response(serializer.data)
        else:
            return Response({"message": "No hay cuentas registradas"}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):
        usuario = User.objects.get(username=request.user)
        if usuario.is_staff:
            queryset = Cuenta.objects.get(pk=pk)
            serializer = CuentaSerializer(queryset, many=False, context={"request": request})
        else:
            cliente = Cliente.objects.get(usuario=usuario.id)
            queryset = Cuenta.objects.filter(customer_id=cliente.customer_id)
            if queryset:
                serializer = CuentaSerializer(queryset, many=True, context={"request": request})
                return Response(serializer.data)
            else:
                return Response({"message": "No hay cuentas registradas"}, status=status.HTTP_404_NOT_FOUND)


class PrestamosViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get"]

    def list(self, request):
        usuario = User.objects.get(username=request.user)
        if usuario.is_staff:
            queryset = Prestamo.objects.all()
            serializer = PrestamosSerializer(queryset, many=True, context={"request": request})
        else:
            cliente = Cliente.objects.get(usuario=usuario.id)
            queryset = Prestamo.objects.filter(customer_id=cliente.customer_id)
            serializer = PrestamosSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        usuario = User.objects.get(username=request.user)
        if usuario.is_staff:
            queryset = Prestamo.objects.get(pk=pk)
            serializer = PrestamosSerializer(queryset, many=False, context={"request": request})
        else:
            cliente = Cliente.objects.get(usuario=usuario.id)
            queryset = Prestamo.objects.filter(customer_id=cliente.customer_id)
            if queryset:
                serializer = PrestamosSerializer(queryset, many=True, context={"request": request})
                return Response(serializer.data)
            else:
                return Response({"message": "No hay prestamos registrados"}, status=status.HTTP_404_NOT_FOUND)


class totalPrestamosViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TotalPrestamosSerializer
    http_method_names = ["get"]

    def list(self, request):
        usuario = User.objects.get(username=request.user)
        if usuario.is_staff:
            queryset = Prestamo.objects.all()
            serializer = TotalPrestamosSerializer(queryset, many=True, context={"request": request})
            return Response(serializer.data)
        return Response(
            {"error": "No tienes permisos para acceder a esta información"}, status=status.HTTP_401_UNAUTHORIZED
        )

    def retrieve(self, request, pk=None):
        usuario = User.objects.get(username=request.user)
        if usuario.is_staff:
            queryset = Prestamo.objects.filter(branch_id=pk)
            serializer = TotalPrestamosSerializer(queryset, many=True, context={"request": request})
            return Response(serializer.data)
        return Response(
            {"error": "No tienes permisos para acceder a esta información"}, status=status.HTTP_401_UNAUTHORIZED
        )


class GestionPrestamosViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Prestamo.objects.all()
    serializer_class = GestionPrestamosSerializer
    http_method_names = ["post", "delete"]

    def create(self, request):
        usuario = User.objects.get(username=request.user)
        if usuario.is_staff:
            serializer = GestionPrestamosSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "No tienes permisos para realizar esta acción"}, status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, pk=None):
        usuario = User.objects.get(username=request.user)
        if usuario.is_staff:
            instance = self.get_object()
            instance.delete()
            cuentaCliente = Cuenta.objects.filter(customer_id=instance.customer_id)
            if cuentaCliente.count() > 0:
                cuentaCliente = cuentaCliente.first()
                cuentaCliente.balance = cuentaCliente.balance - int(instance.loan_total) * 10
                cuentaCliente.save()
            else:
                raise Http404
            return Response({"detail": "Successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "No tienes permisos para realizar esta acción"}, status=status.HTTP_401_UNAUTHORIZED)


class SucursalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer


class TarjetasViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        return Response(
            {"error": "No se puede acceder a la lista de todas las tarjetas"}, status=status.HTTP_401_UNAUTHORIZED
        )

    def retrieve(self, request, pk=None):
        usuario = User.objects.get(username=request.user)
        if usuario.is_staff:
            queryset = Tarjeta.objects.filter(customer_id=pk)
            serializer = TarjetaSerializer(queryset, many=True, context={"request": request})
            if serializer.data:
                return Response(serializer.data)
            return Response({"detail": "El cliente no tiene tarjetas"}, status=status.HTTP_404_NOT_FOUND)
        return Response(
            {"detail": "No tiene permisos para acceder a esta información"}, status=status.HTTP_401_UNAUTHORIZED
        )


class TipoTarjetaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tipotarjeta.objects.all()
    serializer_class = TipoTarjetaSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get"]


class MarcasTarjetaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Marcastarjeta.objects.all()
    serializer_class = MarcasTarjetaSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get"]


class DireccionesViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Direcciones.objects.all()
    serializer_class = DireccionesSerializer
    http_method_names = ["get", "patch"]

    def list(self, request):
        usuario = User.objects.get(username=request.user)
        if usuario.is_staff:
            queryset = Direcciones.objects.all()
            serializer = DireccionesSerializer(queryset, many=True, context={"request": request})
            return Response(serializer.data)
        else:
            cliente = Cliente.objects.get(usuario=usuario.id)
            queryset = Direcciones.objects.filter(iddirecciones=cliente.iddirecciones)
            serializer = DireccionesSerializer(queryset, many=True, context={"request": request})
            if serializer.data:
                return Response(serializer.data)
            return Response({"detail": "El cliente no tiene direcciones"}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):
        usuario = User.objects.get(username=request.user)
        if usuario.is_staff:
            queryset = Direcciones.objects.filter(pk=pk)
            serializer = DireccionesSerializer(queryset, many=True, context={"request": request})
            if serializer.data:
                return Response(serializer.data)
            return Response({"detail": "La direccion no existe"}, status=status.HTTP_404_NOT_FOUND)
        else:
            cliente = Cliente.objects.get(usuario=usuario.id)
            queryset = Direcciones.objects.get(pk=pk)
            print(queryset.iddirecciones)
            print(cliente.iddirecciones)
            if queryset.iddirecciones == cliente.iddirecciones:
                serializer = DireccionesSerializer(queryset, many=False, context={"request": request})
                return Response(serializer.data)
            return Response({"detail": "Solo puedes acceder a tus direcciones"}, status=status.HTTP_401_UNAUTHORIZED)

    def update(self, request, pk=None, partial=True):
        usuario = User.objects.get(username=request.user)
        if usuario.is_staff:
            instance = self.get_object()
            serializer = DireccionesSerializer(
                instance, data=request.data, partial=partial, context={"request": request}
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            cliente = Cliente.objects.get(usuario=usuario.id)
            instance = self.get_object()
            if instance.iddirecciones == cliente.iddirecciones:
                serializer = DireccionesSerializer(
                    instance, data=request.data, partial=partial, context={"request": request}
                )
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(
                {"detail": "No puedes actualizar una dirección que no es tuya"}, status=status.HTTP_401_UNAUTHORIZED
            )
