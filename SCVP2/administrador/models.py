from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

"""

class AdministradorManager(BaseUserManager):
    def create_user(self, numero_empleado, contrasena=None):
        if not numero_empleado:
            raise ValueError('El número de empleado es obligatorio')

        user = self.model(
            numero_empleado=numero_empleado,
        )

        user.set_password(contrasena)
        user.save(using=self._db)
        return user
git
    def create_superuser(self, numero_empleado, contrasena=None):
        user = self.create_user(
            numero_empleado=numero_empleado,
            contrasena=contrasena,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Administrador(AbstractBaseUser):
    numero_empleado = models.CharField(max_length=8, unique=True)
    contrasena = models.CharField(max_length=100)

    USERNAME_FIELD = 'numero_empleado'

    objects = AdministradorManager()

    def __str__(self):
        return self.numero_empleado

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
# Especifica el nombre de la tabla existente en la base de datos
"""