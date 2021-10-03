# Generated by Django 3.2.7 on 2021-09-29 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoIngresso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricaoTipoIngresso', models.CharField(max_length=100, verbose_name='descricaoTipoIngresso')),
                ('slug', models.SlugField(max_length=100, verbose_name='Identificador')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
            options={
                'verbose_name': 'TipoIngresso',
                'verbose_name_plural': 'TipoIngressos',
                'ordering': ['descricaoTipoIngresso'],
            },
        ),
        migrations.CreateModel(
            name='Ingresso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='titulo')),
                ('slug', models.SlugField(max_length=100, verbose_name='Identificador')),
                ('descricao', models.CharField(max_length=280, verbose_name='descricao')),
                ('dataEvento', models.DateField(verbose_name='dataEvento')),
                ('imgEvento', models.ImageField(blank=True, null=True, upload_to='ingressos', verbose_name='Imagem')),
                ('horaEvento', models.DateTimeField(verbose_name='horaEvento')),
                ('localEvento', models.CharField(max_length=150, verbose_name='localEvento')),
                ('idToken', models.CharField(max_length=30, verbose_name='idToken')),
                ('qtdIngresso', models.IntegerField(verbose_name='qtdIngresso')),
                ('precoIngresso', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='precoIngresso')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('tipoingresso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.tipoingresso', verbose_name='TipoIngresso')),
            ],
            options={
                'verbose_name': 'Ingresso',
                'verbose_name_plural': 'Ingressos',
                'ordering': ['titulo'],
            },
        ),
    ]