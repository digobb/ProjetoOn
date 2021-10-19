from django.urls import path
from django.urls.conf import include
from catalog import views

#\w = qualquer caracter alfanumerico
# _ ou - pode conter na url
urlpatterns = [
    path('', views.ingresso_list, name='ingresso_list'),
    #path('<slug:slug>', views.ingresso, name='ingresso'),
    path('detalhe/<int:id>', views.ingresso, name='ingresso'),
    #path(r'(?P<slug>[\w_-]+)/$', views.ingresso, name='ingresso'),
]
