# conversor/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.conversao, name='conversao'),
]
