# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.interface_view, name='home'), # Directs root to interface_view
]