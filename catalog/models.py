from enum import unique
from django.db import models
from django.db.models.fields import CharField

from django.urls import reverse


# Ajustar modelagem
# Carrinho no centro e deve ser criado uma classe evento, onde esta

class Ingresso(models.Model):
    titulo = models.CharField('titulo', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    descricao = models.CharField('descricao', max_length=280)
    dataEvento = models.DateField('dataEvento')
    imgEvento = models.ImageField(
        'Imagem', upload_to='ingressos', blank=True, null=True)
    horaEvento = models.TimeField('horaEvento')
    localEvento = models.CharField('localEvento', max_length=150)
    idToken = models.CharField('idToken', max_length=30)
    qtdIngresso = models.IntegerField('qtdIngresso')
    precoIngresso = models.DecimalField(
        'precoIngresso', decimal_places=2, max_digits=8)

    tipoingresso = models.ForeignKey(
        'catalog.TipoIngresso', verbose_name='TipoIngresso', on_delete=models.CASCADE)
    # no momento que inserir no bd ele insere a data atual
    criado = models.DateTimeField('Criado em', auto_now_add=True)
    # no momento que editar, altera a data para a atual
    modificado = models.DateTimeField('Modificado em', auto_now=True)
# classe meta-> contêiner de classe com algumas opções (metadados) anexadas ao modelo

    class Meta:
        verbose_name = 'Ingresso'
        verbose_name_plural = 'Ingressos'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo #define que o objeto se chamará o "titulo"
    

class TipoIngresso(models.Model):
    descricaoTipoIngresso = models.CharField(
        'descricaoTipoIngresso', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)
# classe meta-> contêiner de classe com algumas opções (metadados) anexadas ao modelo

    class Meta:
        verbose_name = 'TipoIngresso'
        verbose_name_plural = 'TipoIngressos'
        ordering = ['descricaoTipoIngresso']

    def __str__(self):
        return self.descricaoTipoIngresso #define que o objeto se chamará o "descricaoTipoIngresso"