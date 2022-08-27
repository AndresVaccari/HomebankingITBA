from django.contrib import admin
from django.urls import path, include

from .views import (
    ClienteViewSet,
    UserViewSet,
    SujetoDireccionViewSet,
    TiposclienteViewSet,
    CuentaViewSet,
    PrestamosViewSet,
    totalPrestamosViewSet,
    SucursalViewSet,
    TarjetasViewSet,
    TipoTarjetaViewSet,
    MarcasTarjetaViewSet,
    GestionPrestamosViewSet,
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"cliente", ClienteViewSet, basename="cliente")
router.register(r"usuarios", UserViewSet, basename="usuarios")
router.register(r"direcciones", SujetoDireccionViewSet)
router.register(r"tipoCliente", TiposclienteViewSet)
router.register(r"cuenta", CuentaViewSet, basename="cuenta")
router.register(r"prestamos", PrestamosViewSet, basename="prestamos")
router.register(r"totalPrestamos", totalPrestamosViewSet, basename="totalPrestamos")
router.register(r"sucursales", SucursalViewSet)
router.register(r"tarjetas", TarjetasViewSet, basename="tarjeta")
router.register(r"tipoTarjeta", TipoTarjetaViewSet)
router.register(r"marcasTarjeta", MarcasTarjetaViewSet)
router.register(r"gestionPrestamos", GestionPrestamosViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
