from django.shortcuts import render, redirect
from .forms import BoletoForm
from .models import Boleto

def inicio(request):
    return render(request,'inicio.html')

def boleto(request):
    if request.method == 'POST': #Si la petición es post (mandando datos a mi base de datos)
        form = BoletoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = BoletoForm()
    return render(request, 'comprar/comprar.html',{'form':form})

