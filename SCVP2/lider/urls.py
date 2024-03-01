from django.urls import path
from . import views
from django.views.generic import TemplateView
from .views import InicioLiderView, crearGrupoView, procesosView, productoView, estadisticoView, monitoreoView, \
    asignarVariableView, asignarEstandarEquipoView, variableView

app_name = 'lider'

urlpatterns = [
    path('inicio_lider/', InicioLiderView.as_view(), name='inicio_lider'),
    path('lider/crear_grupo/', crearGrupoView.as_view(), name='crear_grupo'),
    path('lider/procesos/', procesosView.as_view(), name='procesos'),
    path('lider/registro_usuarios/', views.registroDeLideresYOperadoresView.as_view(),
         name='registroDeLideresYOperadores'),
    path('lider/producto/', productoView.as_view(), name='producto'),
    path('lider/producto/asignar_var', asignarVariableView.as_view(), name='asignar_var_producto'),
    path('lider/monitoreo/', monitoreoView.as_view(), name='monitoreo'),
    path('lider/estadistico/', estadisticoView.as_view(), name='estadistico'),
    path('lider/equipo/', asignarEstandarEquipoView.as_view(), name='asignar_estandar_equipo'),
    path('lider/variable/', variableView.as_view(), name='variable'),
]
