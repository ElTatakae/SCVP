from django.contrib import admin
from django.urls import path, include
from inicioSCVP import views
from inicioDeSesion import views

urlpatterns = [
    path('', views.inicioSCVP, name='inicioSCVP'),
    path('', views.inicioDeSesion, name='inicioDeSesion'),
    path('admin/', admin.site.urls),
]


