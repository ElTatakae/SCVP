from django.urls import path
from . import views
from django.views.generic import TemplateView
from .views import InicioLiderView, crearGrupoView, procesosView, productoView, estadisticoView, monitoreoView, \
    asignarVariableView, asignarEstandarEquipoView, variableView

app_name = 'lider'

urlpatterns = [
    path('inicio_lider/', InicioLiderView.as_view(), name='inicio_lider'),
    path('crear_grupo/', crearGrupoView.as_view(), name='crear_grupo'),
    path('procesos/', procesosView.as_view(), name='procesos'),
    path('registro_usuarios/', views.registroDeLideresYOperadoresView.as_view(),
         name='registroDeLideresYOperadores'),
    path('producto/', productoView.as_view(), name='producto'),
    path('producto/asignar_var', asignarVariableView.as_view(), name='asignar_var_producto'),
    path('monitoreo/', monitoreoView.as_view(), name='monitoreo'),
    path('estadistico/', estadisticoView.as_view(), name='estadistico'),
    path('equipo/', asignarEstandarEquipoView.as_view(), name='asignar_estandar_equipo'),
    path('variable/', variableView.as_view(), name='variable'),
]
