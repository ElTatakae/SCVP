from django.urls import path, include
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.ingreso, name='ingreso'),
    path('modulo_operador/', views.modulo_operador, name='modulo_operador'),
    path('modulo_lider/', views.modulo_lider, name='modulo_lider'),
   
   # path('', include('usuarios.urls')),
=======
    path('', views.ingreso_usuario, name='ingreso_usuario'),
    path('ingreso_administrador/', views.ingreso_administrador, name='ingreso_administrador'),

>>>>>>> 03a728ceb8c60b78927b74e6fa149964371b3092
]


#path('panel_lider/', views.panel_lider, name='panel_lider'),
#path('panel_operador/', views.panel_operador, name='panel_operador'),