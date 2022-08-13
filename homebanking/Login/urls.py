from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("homebanking/", views.homebanking, name="homebanking"),
    path("gastos/", views.gastos, name="gastos"),
    # path("register/", views.register, name="register"),
]
