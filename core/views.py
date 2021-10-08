from django.shortcuts import render
from django.http import HttpResponse

#Tela inicial (tela base)
def index (request):
    return render(request, 'index.html')

def contact (request):
    return render(request, 'contact.html')

def ingresso (request):
    return render(request, 'ingresso.html')

    
