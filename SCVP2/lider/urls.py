from django.urls import path, include
from . import views

urlpatterns = [
    path('modulo_lider/', views.modulo_lider, name='modulo_lider'),
    path('modulo_lider/crear_grupo/', views.crear_grupo, name='crear_grupo'),
    path('modulo_lider/procesos/', views.procesos, name='procesos'),
    path('modulo_lider/registro_de_lideres_y_operadores/', views.registro_de_lideres_y_operadores, name='registro_de_lideres_y_operadores'),
    path('modulo_lider/producto/', views.producto, name='producto'),
    path('modulo_lider/monitoreo/', views.monitoreo, name='monitoreo'),
]
