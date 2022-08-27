from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("continueRegister/", views.signup_view, name="continueRegister"),
    path("empleadoRegister/", views.registerEmpleado, name="empleadoRegister"),
    path("continueRegisterEmpleado/", views.signup_viewEmpleado, name="continueRegisterEmpleado"),
]
