from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        max_length=150,
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-]+$',
                message='.'
            )
        ]
    )
    username = forms.CharField(
        required=True,
        max_length=50,
        validators=[
            RegexValidator(
                regex=r'',
                message='.'
            )
        ]
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Elimina la ayuda para la contraseña y ajusta el texto del campo de contraseña
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Contraseña'

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        # Aquí puedes personalizar las validaciones de contraseña según tus necesidades
        password_validation.validate_password(password1, self.instance)
        return password1

    def clean_password2(self):
        password2 = self.cleaned_data.get('password2')
        password_validation.validate_password(password2, self.instance)
        return password2
