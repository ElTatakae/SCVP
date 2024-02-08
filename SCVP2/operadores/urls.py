from django.urls import path, include
from . import views

urlpatterns = [
    path('estadisticos/', views.estadisticos, name='estadisticos'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
]
