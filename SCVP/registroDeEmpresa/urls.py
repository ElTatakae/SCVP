from django.urls import path
from . import views


urlpatterns = [
    path('registroDeEmpresa/', views.registroDeEmpresa, name='registroDeEmpresa'),
    path('registroDatosEmpresa/', views.registroDatosEmpresa, name='registroDatosEmpresa'),
]