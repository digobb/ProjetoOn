from django.shortcuts import render
from django.http import HttpResponse

#Tela inicial (tela base)
def index (request):
    return render(request, 'index.html')

