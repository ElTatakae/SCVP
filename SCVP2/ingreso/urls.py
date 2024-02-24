from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ingreso_usuario, name='ingreso_usuario'),
    path('ingreso_administrador/', views.ingreso_administrador, name='ingreso_administrador'),
]

