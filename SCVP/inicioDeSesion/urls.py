from django.urls import path
from . import views

urlpatterns = [
    path('inicioDeSesion/', views.inicioDeSesion, name='inicioDeSesion'),
]