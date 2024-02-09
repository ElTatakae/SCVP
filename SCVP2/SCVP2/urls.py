from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('ingreso.urls')),
    path('', include('administrador.urls')),
    path('', include('empresa.urls')),
    path('', include('operador.urls')),
    path('admin/', admin.site.urls),
]
