from django.contrib import admin
from .models import Ingresso, TipoIngresso


class IngressoAdmin(admin.ModelAdmin):  #lista de opções que irão ser apresentadas no /admin
    list_display = ['titulo', 'slug', 'tipoingresso',       
                    'qtdIngresso', 'criado', 'modificado']
    search_fields = ['titulo', 'slug']
    list_filter = ['criado', 'modificado'] #opção de filtro para criados e modificados


class TipoIngressoAdmin(admin.ModelAdmin): #lista de opções que irão ser apresentadas no /admin
    list_display = ['descricaoTipoIngresso', 'slug', 'created', 'modified']
    search_fields = ['descricaoTipoIngresso', 'slug']
    list_filter = ['created', 'modified'] #opção de filtro para criados e modificados


# Adiciona e registra no DjangoAdmin que contém estes modelos para cadastro
admin.site.register(TipoIngresso, TipoIngressoAdmin)
admin.site.register(Ingresso, IngressoAdmin)
