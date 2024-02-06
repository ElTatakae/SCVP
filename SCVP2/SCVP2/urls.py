from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('usuarios.urls')),
    path('', include('ingreso.urls')),
    path('', include('empresa.urls')),
    path('admin/', admin.site.urls),
]