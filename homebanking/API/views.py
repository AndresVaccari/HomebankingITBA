from msilib.schema import ServiceInstall
from typing_extensions import Self
from django.shortcuts import render
from rest_framework import status, generics, permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .serializers import ClienteSerializer, UserSerializer, SujetoDireccionSerializer, TiposclienteSerializer
from Clientes.models import Cliente, Sujetodireccion, Tiposcliente
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.contrib.sessions.models import Session


# Create your views here.

# Create your views here.


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


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
