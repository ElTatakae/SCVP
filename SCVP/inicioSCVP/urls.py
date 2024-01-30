from django.urls import path
from . import views


urlpatterns = [
    path('inicioSCVP/', views.inicioSCVP, name='inicioSCVP'),
]