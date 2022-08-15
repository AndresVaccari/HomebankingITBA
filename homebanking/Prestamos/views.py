from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from Clientes.models import Cuenta, Cliente
from .forms import PrestamosForm
from .models import Prestamo

# Create your views here.


def prestamos(request):

    try:
        request.session["usuario"]
        cantidadcuentasCliente = list(Cuenta.objects.filter(customer_id=request.session["customer_id"]))
        if len(cantidadcuentasCliente) == 0:
            return redirect("/homebanking/inicio")
        if request.method == "POST":
            form = PrestamosForm(request.POST)
            if form.is_valid():
                montoPrestamo = request.POST.get("montoPrestamo")
                date = request.POST.get("date")
                tipoPrestamo = request.POST.get("tipoPrestamo")
                if request.session["tipoCliente"] == "Classic":
                    if int(montoPrestamo) > 100000:
                        return render(
                            request,
                            "Prestamos/prestamos.html",
                            {"form": form, "error": "El monto no puede ser mayor a 100000"},
                        )
                if request.session["tipoCliente"] == "Gold":
                    if int(montoPrestamo) > 300000:
                        return render(
                            request,
                            "Prestamos/prestamos.html",
                            {"form": form, "error": "El monto no puede ser mayor a 300000"},
                        )
                if request.session["tipoCliente"] == "Black":
                    if int(montoPrestamo) > 500000:
                        return render(
                            request,
                            "Prestamos/prestamos.html",
                            {"form": form, "error": "El monto no puede ser mayor a 500000"},
                        )
                prestamo = Prestamo(
                    loan_type=tipoPrestamo,
                    loan_total=montoPrestamo,
                    loan_date=date,
                    customer_id=Cliente.objects.get(customer_id=request.session["customer_id"]),
                )
                prestamo.save()
                cuentasCliente = Cuenta.objects.filter(customer_id=request.session["customer_id"])
                cuentaCliente = Cuenta.objects.get(account_id=cuentasCliente[0].account_id)
                cuentaCliente.balance = cuentasCliente[0].balance + int(montoPrestamo) * 10
                cuentaCliente.save()
                return render(
                    request,
                    "Prestamos/prestamos.html",
                    {"form": form, "error": "El prestamo se ha realizado con exito"},
                )
        else:
            form = PrestamosForm()
        return render(request, "Prestamos/prestamos.html", {"form": form})
    except (Session.DoesNotExist, KeyError):
        return redirect("/")
