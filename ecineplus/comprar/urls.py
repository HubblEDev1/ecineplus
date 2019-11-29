from django.urls import path
from .views import inicio, boleto

urlpatterns = [
    path('boletos/', boleto, name= 'boleto')
]