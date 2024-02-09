from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('ingreso.urls')),
    path('', include('usuarios.urls')),
    path('', include('empresa.urls')),
    path('', include('operadores.urls')),
    path('admin/', admin.site.urls),
]
