# from socket import fromshare
from tkinter.ttk import Style
from django import forms


class validacionUsuario(forms.Form):
    dni = forms.CharField(
        label="Documento",
        max_length=9,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    dob = forms.DateTimeField(
        label="Fecha Nacimiento",
        widget=forms.DateTimeInput(attrs={"type": "date", "class": "form-control"}),
    )
