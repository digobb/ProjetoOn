from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

#Tela inicial (tela base)
def index (request):
    return render(request, 'index.html')

def contact (request):
    return render(request, 'contact.html')

class Login(LoginView):
    template_name = 'login.html'

class Logout(LogoutView):
    template_name = 'index.html'

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'cadastro.html'
    model = User
register = RegisterView.as_view()

    
