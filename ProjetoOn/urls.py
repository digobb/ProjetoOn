"""ProjetoOn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import(
    path,
    include,
)
from core import views
from core.views import index 
from catalog import(
    urls,

) 


urlpatterns = [
    path('admin/', admin.site.urls),  # area administrativa
    # página index (padrão) - name='' torna acessível a chamativa da url dentro do code
    path('', index, name='index'),
    path('contato', views.contact, name='contact'),
    #path('ingresso', views.ingresso, name='ingresso'),
    path('ingressos/', include('catalog.urls')), #irá verificar dentro de catalog/templates/urls.py a view a ser retornada 
]
