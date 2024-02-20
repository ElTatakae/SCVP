from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.inicio_panel, name='inicio_panel'),
    path('inicio_de_sesion/', views.inicio_de_sesion, name='inicio_de_sesion'),
    path('agregar_grupo/', views.agregar_grupo, name='agregar_grupo'),
    path('base/', views.base, name='base'),
    path('panel_lideres/', views.panel_lideres, name='panel_lideres'),
    path('panel_operadores/', views.panel_operadores, name='panel_operadores'),
]