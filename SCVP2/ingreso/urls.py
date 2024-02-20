from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ingreso, name='ingreso'),
    path('modulo_operador/', views.modulo_operador, name='modulo_operador'),
    path('modulo_lider/', views.modulo_lider, name='modulo_lider'),
   # path('', include('usuarios.urls')),
    path('', views.ingreso_usuario, name='ingreso_usuario'),
    path('ingreso_administrador/', views.ingreso_administrador, name='ingreso_administrador'),
]

