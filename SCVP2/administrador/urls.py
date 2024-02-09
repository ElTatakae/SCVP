from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('modulo_administrador/', views.modulo_administrador, name='modulo_administrador'),
    path('modulo_lider/', views.modulo_lider, name='modulo_lider'),
    path('modulo_operador/', views.modulo_operador, name='modulo_operador'),
    path('modulo_administrador/registro_de_usuario/', views.registro_de_usuario, name='registro_de_usuario'),
    path('inicio_de_sesion/', views.inicio_de_sesion, name='inicio_de_sesion'),
    path('panel_administrador/', views.panel_administrador, name='panel_administrador'),
]