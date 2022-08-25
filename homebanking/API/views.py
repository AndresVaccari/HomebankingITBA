from django.shortcuts import render
from rest_framework import status, generics, permissions, viewsets
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .serializers import ClienteSerializer
from Clientes.models import Cliente

# Create your views here.


class ClienteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
