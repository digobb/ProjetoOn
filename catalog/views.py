from django.shortcuts import render
from django.http import HttpResponse
from .models import Ingresso


# Create your views here.
def ingresso_list(request):
    return render(request, 'catalog/ingresso_list.html') #para cada aplicação irá buscar a pasta template e renderizar 
















