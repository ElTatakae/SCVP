from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from .models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_numero_empleado(self):
        numero_empleado = self.cleaned_data.get('numero_empleado')
        if not numero_empleado.isalnum() or len(numero_empleado) > 8:
            raise ValidationError(_('El número de empleado debe ser alfanumérico y tener como máximo 8 caracteres.'))
        return numero_empleado

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError(_('La contraseña debe tener al menos 8 caracteres.'))

        # Verificar si la contraseña contiene al menos un dígito
        if not any(char.isdigit() for char in password):
            raise ValidationError(_('La contraseña debe contener al menos un dígito (número).'))

        # Verificar si la contraseña contiene al menos una letra mayúscula
        if not any(char.isupper() for char in password):
            raise ValidationError(_('La contraseña debe contener al menos una letra mayúscula.'))

        # Verificar si la contraseña contiene al menos una letra minúscula
        if not any(char.islower() for char in password):
            raise ValidationError(_('La contraseña debe contener al menos una letra minúscula.'))

        # Verificar si la contraseña contiene al menos un símbolo
        if not any(char in "!@#$%^&*()-_+=<>,.?/:;{}[]|'\"" for char in password):
            raise ValidationError(_('La contraseña debe contener al menos un símbolo (por ejemplo: !@#$%^&*).'))

        return password

    def clean_password_repeat(self):
        password = self.cleaned_data.get('password')
        password_repeat = self.cleaned_data.get('password_repeat')

        if password and password_repeat and password != password_repeat:
            raise ValidationError(_('Las contraseñas no coinciden.'))

        return password_repeat

    class Meta:
        model = CustomUser
        fields = ['nombre', 'email', 'numero_empleado', 'password']
