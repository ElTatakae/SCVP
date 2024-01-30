from django.urls import path
from . import views


urlpatterns = [
    path('registroDeEmpresa/', views.registroDeEmpresa, name='registroDeEmpresa'),
    path('registroNombreEmpresa/', views.registroNombreEmpresa, name='registroNombreEmpresa'),
    path('registroDatosEmpresa/', views.registroDatosEmpresa, name='registroDatosEmpresa'),
]