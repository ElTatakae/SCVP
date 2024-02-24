from django.urls import path, include
from . import views

urlpatterns = [
    path('operador/', views.operador, name='operador'),
    path('operador/estadisticos/', views.estadisticos, name='estadisticos'),
    path('operador/crear_producto/', views.crear_producto, name='crear_producto'),
    path('operador/panel_operador/', views.panel_operador, name='panel_operador'),
]
