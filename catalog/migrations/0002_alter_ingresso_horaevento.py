# Generated by Django 3.2.7 on 2021-10-03 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingresso',
            name='horaEvento',
            field=models.TimeField(verbose_name='horaEvento'),
        ),
    ]
