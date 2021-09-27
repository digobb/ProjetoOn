from enum import unique
from django.db import models
from django.db.models.fields import CharField


class Ingresso(models.Model):
    titulo = models.CharField('titulo', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    descricao = models.CharField('descricao', max_length=280)
    dataEvento = models.DateField('dataEvento')
    imgEvento = models.ImageField('imgEvento')
    horaEvento = models.DateTimeField('horaEvento')
    localEvento = models.CharField('localEvento')
    idToken = models.CharField('idToken', max_length=30)
    qtdIngresso = models.IntegerField('qtdIngresso')
    precoIngresso = models.DecimalField('precoIngresso', decimal_places=2, max_digits=8)

    formaPagamento = models.ForeignKey('catalog.FormaPagamento') #informa o model e a associação


    # no momento que inserir no bd ele insere a data atual
    criado = models.DateTimeField('Criado em', auto_now_add=True)
    # no momento que editar, altera a data para a atual
    modificado = models.DateTimeField('Modificado em', auto_now=True)

    # classe meta-> contêiner de classe com algumas opções (metadados) anexadas ao modelo
    class Meta:
        verbose_titulo = 'Ingresso'
        verbose_titulo_plural = 'Ingressos'
        ordering = ['titulo']


class Usuario:
    idUsuario = models.IntegerField('idUsuario', unique=True)
    nome = models.CharField('nome', max_length=50)
    sexo = models.CharField('sexo')
    email = models.EmailField('email', unique=True)
    senha = models.CharField('senha')
    cpf = models.CharField('cpf', unique=True)
    nCelular = models.CharField('nCelular', max_length=15, unique=True)

    # no momento que inserir no bd ele insere a data atual
    criado = models.DateTimeField('Criado em', auto_now_add=True)

class FormaPagamento:
    idFormaPagamento = models.CharField('idFormaPagamento', max_length=20)
    descricaoFormaPagamento = models.CharField('descricaoFormaPagamento', max_length=50, unique=True)
    formaPagamento = models.CharField('formaPagamento') 
