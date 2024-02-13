from django import forms
#from .models import Administrador

class ingresoAdminForm(forms.Form):
    numero_empleado = forms.CharField(max_length=8)
    contrasena = forms.CharField(widget=forms.PasswordInput)
