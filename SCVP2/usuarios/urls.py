from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.inicio_panel, name='inicio_panel'),
    path('registro_de_usuario/', views.registro_de_usuario, name='registro_de_usuario'),
    path('inicio_de_sesion/', views.inicio_de_sesion, name='inicio_de_sesion'),
    path('base/', views.base, name='base'),
]