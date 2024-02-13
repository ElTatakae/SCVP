from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ingreso, name='ingreso'),
    path('modulo_operador/', views.modulo_operador, name='modulo_operador'),
    path('modulo_lider/', views.modulo_lider, name='modulo_lider'),
   
   # path('', include('usuarios.urls')),
]


#path('panel_lider/', views.panel_lider, name='panel_lider'),
#path('panel_operador/', views.panel_operador, name='panel_operador'),