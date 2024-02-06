from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, nombre, numero_empleado, is_lider, password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        user = self.model(
            email=self.normalize_email(email),
            nombre=nombre,
            numero_empleado=numero_empleado,
            is_lider=is_lider,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nombre, numero_empleado, password):
        user = self.create_user(
            email=email,
            nombre=nombre,
            numero_empleado=numero_empleado,
            password=password,
            is_lider=True,
            is_staff=True,
            is_superuser=True,
        )
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=255)
    numero_empleado = models.CharField(max_length=8, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_lider = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'numero_empleado']

    def __str__(self):
        return self.email
