from django.shortcuts import render

# Create your views here.


def homebanking(request):
    customer_name = request.session["customer_name"]
    customer_surname = request.session["customer_surname"]
    context = {"customer_name": customer_name, "customer_surname": customer_surname}
    return render(request, "Cuentas/homebanking.html", context=context)


def gastos(request):
    return render(request, "Cuentas/gastos.html")
