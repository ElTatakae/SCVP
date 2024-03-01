from django.urls import path
from .views import adminInicioView, registroEmpresaView, registroAdminView, registroLiderView, crudEmpresaView, verEmpresaView

app_name = 'administrador'
urlpatterns = [
    path('administrador/', adminInicioView.as_view(), name='inicio_administrador'),
    path('administrador/menu/registro_de_empresa/', registroEmpresaView.as_view(), name='registro_empresa'),
    path('administrador/menu_empresa/', crudEmpresaView.as_view(), name='menu_empresa'),
    path('registro_de_lider/', registroLiderView.as_view(), name='registro_lider'),
    path('registro_de_admin/', registroAdminView.as_view(), name='registro_admin'),
    path('visualizar_empresa/', verEmpresaView.as_view(), name='ver_empresa'),
]
