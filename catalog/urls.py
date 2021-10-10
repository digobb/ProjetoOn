from django.urls import path
from django.urls.conf import include
from catalog import views
import catalog

urlpatterns = [
    path('', views.ingresso_list, name='ingresso_list'),
    path(r'ingressos/(?P<slug>[\w_-]+)/$', views.ingresso, name='ingresso'),
]
