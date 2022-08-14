from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session

# Create your views here.


def homebanking(request):
    try:
        request.session["usuario"]
        customer_name = request.session["customer_name"]
        customer_surname = request.session["customer_surname"]
        context = {"customer_name": customer_name, "customer_surname": customer_surname}
        return render(request, "Cuentas/homebanking.html", context=context)
    except (Session.DoesNotExist, KeyError):
        return redirect("/")


def gastos(request):
    try:
        request.session["usuario"]
        return render(request, "Cuentas/gastos.html")
    except (Session.DoesNotExist, KeyError):
        return redirect("/")
