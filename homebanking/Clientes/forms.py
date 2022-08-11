from socket import fromshare
from django import forms
from .models import Cliente


class ClientesForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["customer_name", "customer_surname", "customer_DNI"]
