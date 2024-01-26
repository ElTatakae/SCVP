from django.urls import path
from . import views

urlpatterns = [
    path('InicioDeSesion/', views.members, name='members'),
]