from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicioSCVP, name='inicioSCVP'),
    path('inicioAdministrador/', views.inicioAdministrador, name='inicioAdministrador'),
    path('creacionDeGrupo/', views.creacionDeGrupo, name='creacionDeGrupo'),
    path('registroUsuario/', views.registroUsuario, name='registroUsuario'),
    path('agregarGrupo/', views.agregarGrupo, name='agregarGrupo'),
]