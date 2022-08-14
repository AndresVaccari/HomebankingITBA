from socket import fromshare
from tkinter.ttk import Style
from django import forms


class validacionUsuario(forms.Form):
    dni = forms.CharField(label="Documento", max_length=9)
    dob = forms.CharField(label="Fecha nacimiento (YYYY-MM-DD)", max_length=10)
