from django.contrib import admin

from .models import Ingresso, TipoIngresso

#Adiciona e registra no DjangoAdmin que contém estes modelos para cadastro
admin.site.register(Ingresso) 
admin.site.register(TipoIngresso)
