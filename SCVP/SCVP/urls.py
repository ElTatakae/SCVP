from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('', include('inicioSCVP.urls')),
    path('', include('inicioDeSesion.urls')),
    path('', include('registroDeEmpresa.urls')),
    path('admin/', admin.site.urls),
]


