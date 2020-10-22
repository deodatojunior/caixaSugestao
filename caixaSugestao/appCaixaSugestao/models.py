from django.db import models
from django.conf import settings
from django import forms
# Create your models here.

class Sugestao(models.Model):
    nome = models.CharField(max_length=30, null=False)
    texto = models.TextField(null=False)
    area_Da_Empresa = models.CharField(max_length=30, null=False)

class mensagemArea(models.Model):
    responsavel = models.CharField(max_length=100, null=False)
    resposta = models.TextField(null=False)
    sugestionador = models.CharField(max_length=100, null=False)




