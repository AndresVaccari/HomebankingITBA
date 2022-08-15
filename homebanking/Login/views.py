from os import curdir
from django.shortcuts import render, redirect
from .forms import validacionUsuario, registroForm, loginForm
from django.contrib.auth.forms import AuthenticationForm
from Clientes.models import Cliente, Cuenta
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session


# Create your views here.


def index(request):
    try:
        request.session["usuario"]
        return redirect("/homebanking/inicio")
    except (Session.DoesNotExist, KeyError):
        request.session["customer_id"] = None
        return render(request, "Login/index.html")


def login(request):
    try:
        request.session["usuario"]
        return redirect("/homebanking/inicio")
    except (Session.DoesNotExist, KeyError):
        request.session["customer_id"] = None
        if request.method == "POST":
            form = loginForm(data=request.POST)
            if form.is_valid():
                cliente = Cliente.objects.get(usuario=form.get_user())
                username = User.objects.get(username=form.get_user())
                request.session["customer_id"] = cliente.customer_id
                request.session["customer_dni"] = cliente.customer_dni
                request.session["customer_name"] = cliente.customer_name
                request.session["customer_surname"] = cliente.customer_surname
                request.session["usuario"] = username.username
                request.session["tipoCliente"] = cliente.tipoCliente.nombretipo
                return redirect("/homebanking/inicio")
        else:
            form = loginForm()
        return render(request, "Login/login.html", {"form": form})


def register(request):
    try:
        request.session["usuario"]
        return redirect("/homebanking/inicio")
    except (Session.DoesNotExist, KeyError):
        request.session["customer_id"] = None
        if request.method == "POST":
            form = validacionUsuario(request.POST)
            if form.is_valid():
                dni = request.POST.get("dni")
                dob = request.POST.get("dob")
                try:
                    cliente = Cliente.objects.get(customer_dni=dni, dob=dob)
                except Cliente.DoesNotExist:
                    return render(request, "Login/register.html", {"form": form, "error": "El cliente no existe"})
                if cliente.usuario != None:
                    return render(
                        request, "Login/register.html", {"form": form, "error": "El cliente ya tiene un usuario"}
                    )
                else:
                    request.session["customer_id"] = cliente.customer_id
                    return redirect("/continueRegister")
        else:
            form = validacionUsuario()
        return render(request, "Login/register.html", {"form": form})


def signup_view(request):
    try:
        request.session["usuario"]
        return redirect("/homebanking/inicio")
    except (Session.DoesNotExist, KeyError):
        if request.session["customer_id"] != None:
            id = request.session["customer_id"]
            if request.method == "POST":
                form = registroForm(request.POST)
                if form.is_valid():
                    form.save()
                    usuario = request.POST.get("username")
                    user = User.objects.get(username=usuario)
                    cliente = Cliente.objects.get(customer_id=id)
                    cliente.usuario = user
                    cliente.save()
                    request.session["customer_id"] = None
                    return redirect("login")
            else:
                form = registroForm()
            return render(request, "Login/continueRegister.html", {"form": form})
        else:
            return redirect("/")
