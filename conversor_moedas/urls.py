# conversor_moedas/urls.py
from django.contrib import admin
from django.urls import path, include  # Certifique-se de incluir o 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('conversor.urls')),  # Incluindo as URLs da aplicação 'conversor'
]
