from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('modulo_administrador/', views.modulo_administrador, name='modulo_administrador'),
    path('modulo_lider/', views.modulo_lider, name='modulo_lider'),
    path('modulo_operador/', views.modulo_operador, name='modulo_operador'),
    path('inicio_de_sesion/', views.inicio_de_sesion, name='inicio_de_sesion'),
    path('base/', views.base, name='base'),
]