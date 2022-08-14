from django.shortcuts import render, redirect
from .forms import validacionUsuario
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from Clientes.models import Cliente
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    request.session["customer_id"] = None
    return render(request, "Login/index.html")


def login(request):
    request.session["customer_id"] = None
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            cliente = Cliente.objects.get(usuario=form.get_user())
            request.session["customer_id"] = cliente.customer_id
            request.session["customer_dni"] = cliente.customer_dni
            request.session["customer_name"] = cliente.customer_name
            request.session["customer_surname"] = cliente.customer_surname
            return redirect("/homebanking/inicio")
    else:
        form = AuthenticationForm()
    return render(request, "Login/login.html", {"form": form})


def register(request):
    request.session["customer_id"] = None
    if request.method == "POST":
        form = validacionUsuario(request.POST)
        if form.is_valid():
            dni = request.POST.get("dni")
            dob = request.POST.get("dob")
            cliente = Cliente.objects.filter(customer_dni=dni, dob=dob)
            if cliente:
                if cliente[0].usuario != None:
                    print("Usuario registrado")
                else:
                    request.session["customer_id"] = cliente[0].customer_id
                    return redirect("/continueRegister")
    form = validacionUsuario()
    return render(request, "Login/register.html", {"form": form})


def signup_view(request):
    if request.session["customer_id"] != None:
        id = request.session["customer_id"]
        if request.method == "POST":
            form = UserCreationForm(request.POST)
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
            form = UserCreationForm()
        return render(request, "Login/continueRegister.html", {"form": form})
    else:
        return redirect("/")
