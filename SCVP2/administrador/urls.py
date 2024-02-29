from django.urls import path
from .views import adminInicioView, registroEmpresaView, registroAdminView, registroLiderView

app_name = 'admin'
urlpatterns = [
    path('admin/', adminInicioView.as_view(), name='inicio_admin'),
    path('admin/registro_de_empresa/', registroEmpresaView.as_view(), name='registro_empresa'),
    path('admin/registro_de_lider/', registroLiderView.as_view(), name='registro_lider'),
    path('admin/registro_de_admin/', registroAdminView.as_view(), name='registro_de_admin'),
]
