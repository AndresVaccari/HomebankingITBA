# from socket import fromshare
from urllib import request
from django import forms


class PrestamosForm(forms.Form):

    montoPrestamo = forms.IntegerField(label="Monto", widget=forms.NumberInput(attrs={"class": "form-control"}))
    date = forms.DateTimeField(
        label="Fecha",
        widget=forms.DateTimeInput(attrs={"type": "date", "class": "form-control"}),
    )
    tipoPrestamo = forms.ChoiceField(
        choices=[("Hipotecario", "Hipotecario"), ("Personal", "Personal"), ("Prendario", "Prendario")],
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    def clean_montoPrestamo(self):
        montoPrestamo = self.cleaned_data.get("montoPrestamo")
        if montoPrestamo < 0:
            raise forms.ValidationError("El monto no puede ser negativo")
        return montoPrestamo
