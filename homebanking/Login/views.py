from urllib import request
from django.shortcuts import render
from .forms import validacionUsuario 
from django.contrib.auth.forms import UserCreationForm

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

def signup_view(request):
    form = UserCreationForm()
    return render(request, "Login/continueRegister.html", {"form":form})
