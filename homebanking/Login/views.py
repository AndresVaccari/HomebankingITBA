from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "Login/index.html")


def login(request):
    return render(request, "Login/login.html")


def homebanking(request):
    return render(request, "homebanking.html")


def gastos(request):
    return render(request, "gastos.html")


# def register(request):
#     return render(request, "register.html")
