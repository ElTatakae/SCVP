from django.apps import AppConfig


class IngresoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ingreso'
    verbose_name = 'perfiles'

    def ready(self):
        import ingreso.signals