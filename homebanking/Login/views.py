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
            cliente = Cliente.objects.filter(customer_dni=dni, dob=dob)
            if cliente:
                if cliente[0].usuario != None:
                    print("Usuario registrado")
                else:
                    request.session["userid"] = cliente[0].customer_id
    form = validacionUsuario()
    return render(request, "Login/register.html", {"form": form})


def signup_view(request):
    form = UserCreationForm()
    return render(request, "Login/continueRegister.html", {"form": form})
