from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "Login/index.html")


def login(request):
    return render(request, "Login/login.html")


# def register(request):
#     return render(request, "register.html")
