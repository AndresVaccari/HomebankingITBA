# from socket import fromshare
from tkinter.ttk import Style
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


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

    def clean_dni(self):
        dni = self.cleaned_data.get("dni")
        if len(dni) > 9:
            raise forms.ValidationError("El DNI debe menos de 9 caracteres")
        return dni


class registroForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control mb-2"})
            field.help_text = None

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class loginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control mb-2"})
            field.help_text = None

    class Meta:
        model = User
        fields = ["username", "password"]
