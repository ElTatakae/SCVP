from django.urls import path, include
from . import views

urlpatterns = [
    path('registro_de_empresa/', views.registro_de_empresa, name='registro_de_empresa'),
   # path('', include('administrador.urls')),
]
