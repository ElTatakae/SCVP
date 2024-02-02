#from django import forms

#class obtenerDatosRregistros(forms.Form):
 #   introduceNombre = forms.CharField(max_length=40)
  #  introduceApellido = forms.CharField(max_length=80)


# forms.py
from django import forms
from .models import Empleado
from django.core.validators import RegexValidator

class InicioSesionForm(forms.ModelForm):
    # Definir un validador personalizado para el número de empleado
    alphanumeric_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9]{8}$',
        message='El número de empleado debe tener exactamente 8 caracteres alfanuméricos.',
        code='invalid_numero_empleado'
    )

    # Agregar el validador al campo numero_Empleado
    numero_Empleado = forms.CharField(
        max_length=8,
        validators=[alphanumeric_validator],
        widget=forms.TextInput(attrs={'placeholder': 'Introduce tu número de empleado'})
    )

    class Meta:
        model = Empleado
        fields = ['numero_Empleado', 'contrasena_Empleado']
        widgets = {
            'contrasena_Empleado': forms.PasswordInput(attrs={'placeholder': 'Introduce tu contraseña'}),
            # Se agrega un widget de contraseña para ocultar la contraseña mientras se ingresa.
        }
