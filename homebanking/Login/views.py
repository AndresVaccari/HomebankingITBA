from django.shortcuts import render
from .forms import validacionUsuario

# Create your views here.


def index(request):
    return render(request, "Login/index.html")


def login(request):
    return render(request, "Login/login.html")


def register(request):
    if request.method == "POST":
        form = validacionUsuario(request.POST)
        if form.is_valid():
            dni = request.POST.get("dni")
            dob = request.POST.get("dob")
            print(dni, dob)
            return render(request, "Login/login.html", {"form": form})

    form = validacionUsuario()
    return render(request, "Login/register.html", {"form": form})
