# Generated by Django 3.1.2 on 2020-10-30 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mensagemArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsavel', models.CharField(max_length=100)),
                ('resposta', models.TextField()),
                ('sugestionador', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sugestao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('texto', models.TextField()),
                ('area_Da_Empresa', models.CharField(max_length=30)),
            ],
        ),
    ]
