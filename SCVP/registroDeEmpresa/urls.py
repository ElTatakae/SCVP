from django.urls import path
from . import views

urlpatterns = [
    path('registroDeEmpresa/', views.registroDeEmpresa, name='registroDeEmpresa'),
    path('registrarNombreEmpresa/', views.registrarNombreEmpresa, name='registrarNombreEmpresa'),
]