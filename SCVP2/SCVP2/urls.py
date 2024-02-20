from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('ingreso.urls')),
<<<<<<< HEAD
    path('', include('usuarios.urls')),
    path('', include('empresa.urls')),
    path('', include('operadores.urls')),
=======
    path('', include('administrador.urls')),
    path('', include('lider.urls')),
    path('', include('operador.urls')),
>>>>>>> 03a728ceb8c60b78927b74e6fa149964371b3092
    path('admin/', admin.site.urls),
]
