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
from os import name
from django.contrib import admin
from django.urls import(
    path,
    include,
)
from core import views
from core.views import Login, Logout, index 
from catalog import(
    urls,

)
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static, settings



urlpatterns = [
    path('admin/', admin.site.urls),  # area administrativa
    # página index (padrão) - name='' torna acessível a chamativa da url dentro do code
    path('', index, name='index'),
    path('contato', views.contact, name='contact'),

    path('ingressos/', include('catalog.urls'), name='ingressos'),
    #path('ingressos/', include('catalog.urls'), name='ingressos'), #irá verificar dentro de catalog/templates/urls.py a view a ser retornada 
    #login e logout
    path('login/', Login.as_view(), name="login"),
    path('cadastro/', views.register, name="cadastro"),
    path('logout/', Logout.as_view(), name="logout"),
]

#seta pasta onde contém as img 
if settings.DEBUG:
    urlpatterns = urlpatterns + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
