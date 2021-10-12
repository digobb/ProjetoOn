from typing import ContextManager
from django.shortcuts import render
from django.http import HttpResponse
from .models import Ingresso


# Create your views here.
def ingresso_list(request):
    context = {
        'ingressos': Ingresso.objects.all() 
    }
    return render(request, 'catalog/ingresso_list.html', context) #para cada aplicação irá buscar a pasta template e renderizar 

def ingresso(request, titulo):
    ingresso = Ingresso.objects.get(titulo = titulo)
    context = {
        'ingresso':ingresso
    }
    return render(request, 'catalog/ingresso.html', context)















