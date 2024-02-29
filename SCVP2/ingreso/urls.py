from django.urls import path
from .views import inicioView, ingresoUsuarioView, ingresoAdminView

app_name = 'ingreso'
urlpatterns = [
    path('', inicioView.as_view(), name='inicio'),
    path('ingreso_usuario/', ingresoUsuarioView.as_view(), name='ingreso_usuario'),
    path('ingreso_admin/', ingresoAdminView.as_view(), name='ingreso_admin'),
]
