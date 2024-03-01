from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# PERFIL DEL USUARIO

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    phone = models.CharField(max_length=150, null=True, blank=True, verbose_name='Telefono')
    image = models.ImageField(default='user/usuario_defecto.jpg', upload_to='users/', verbose_name='Imagen de perfil')
    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'
        ordering = ['-id']

    def __str__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
