# Generated by Django 3.2.7 on 2021-10-17 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_ingresso_horaevento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingresso',
            name='slug',
            field=models.SlugField(max_length=100, verbose_name='slug'),
        ),
    ]
