from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('modulo_administrador/', views.modulo_administrador, name='modulo_administrador'),
    path('modulo_administrador/registro_de_usuario/', views.registro_de_usuario, name='registro_de_usuario'),
    path('modulo_administrador/registro_de_empresa/', views.registro_de_empresa, name='registro_de_empresa'),
    path('modulo_administrador/registro_de_administrador/', views.registro_de_administrador, name='registro_de_administrador'),
    path('panel_administrador/', views.panel_administrador, name='panel_administrador'),
]