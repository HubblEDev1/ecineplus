from django.contrib import admin
from .models import Pelicula, Cliente, Boleto
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Pelicula)
admin.site.register(Boleto)
