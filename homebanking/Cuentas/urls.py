from django.urls import path
from . import views

urlpatterns = [
    path("inicio/", views.homebanking, name="homebanking"),
    path("gastos/", views.gastos, name="gastos"),
]
