from django.shortcuts import render

# Create your views here.


def homebanking(request):
    return render(request, "Cuentas/homebanking.html")


def gastos(request):
    return render(request, "Cuentas/gastos.html")
