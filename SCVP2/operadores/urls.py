from django.urls import path, include
from . import views

urlpatterns = [
    path('estadisticos/', views.estadisticos, name='estadisticos'),
]
