from django.urls import path
from . import views

urlpatterns = [
    path('InicioDeSesion/', views.InicioDeSesion, name='InicioDeSesion'),
]