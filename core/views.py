from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.http import HttpResponse

#Tela inicial (tela base)
def index (request):
    return render(request, 'index.html')

def contact (request):
    return render(request, 'contact.html')

class Login(LoginView):
    template_name = 'login.html'

class Logout(LogoutView):
    template_name = 'index.html'


    
