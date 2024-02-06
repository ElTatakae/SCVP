from django.urls import path, include
from . import views

urlpatterns = [
    path('inicio_ingreso/', views.inicio_ingreso, name='inicio_ingreso'),
   # path('', include('usuarios.urls')),
]
