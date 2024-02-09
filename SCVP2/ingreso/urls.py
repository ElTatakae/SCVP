from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio_ingreso, name='inicio_ingreso'),
    path('ingreso_admin', views.ingreso_admin, name='ingreso_admin'),
   
   # path('', include('usuarios.urls')),
]


#path('panel_lider/', views.panel_lider, name='panel_lider'),
#path('panel_operador/', views.panel_operador, name='panel_operador'),