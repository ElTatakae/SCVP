from django.urls import path, include
from . import views

urlpatterns = [
    path('modulo_operador/', views.modulo_operador, name='modulo_operador'),
    path('estadisticos/', views.estadisticos, name='estadisticos'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('panel_operador/', views.panel_operador, name='panel_operador'),
]
