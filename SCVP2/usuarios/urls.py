from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
<<<<<<< HEAD
    path('inicio/', views.inicio, name='inicio'),
    path('modulo_administrador/', views.modulo_administrador, name='modulo_administrador'),
    path('modulo_lider/', views.modulo_lider, name='modulo_lider'),
    path('modulo_operador/', views.modulo_operador, name='modulo_operador'),
=======
    path('', views.inicio_panel, name='inicio_panel'),
    path('registro_de_usuario/', views.registro_de_usuario, name='registro_de_usuario'),
>>>>>>> 03a728ceb8c60b78927b74e6fa149964371b3092
    path('inicio_de_sesion/', views.inicio_de_sesion, name='inicio_de_sesion'),
    path('agregar_grupo/', views.agregar_grupo, name='agregar_grupo'),
    path('base/', views.base, name='base'),
    path('panel_lideres/', views.panel_lideres, name='panel_lideres'),
    path('panel_operadores/', views.panel_operadores, name='panel_operadores'),
]