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


# Create your views here.

# Create your views here.
@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "clientes": reverse("clientes-list", request=request, format=format),
        }
    )


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


# class ClienteDetail(APIView):
#     def get(self, request, pk=None):
#         # user = User.objects.filter(pk=pk).first()
#         cliente = Cliente.objects.filter(usuario=pk)
#         serializer = ClienteSerializer(cliente)
#         if cliente:
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class ClienteViewSet(viewsets.ReadOnlyModelViewSet):
    # queryset = Cliente.objects.all()
    # serializer_class = ClienteSerializer
    # permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Cliente.objects.all()

    def list(self, request):
        queryset = Cliente.objects.all()
        serializer = ClienteSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Cliente.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ClienteSerializer(user, context={"request": request})
        return Response(serializer.data)


class SujetoDireccionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sujetodireccion.objects.all()
    serializer_class = SujetoDireccionSerializer
    permission_classes = [permissions.IsAuthenticated]


class TiposclienteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tiposcliente.objects.all()
    serializer_class = TiposclienteSerializer
    permission_classes = [permissions.IsAuthenticated]
