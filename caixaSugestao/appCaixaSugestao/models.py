from django.db import models
from django.conf import settings
from django import forms
# Create your models here.

class Sugestao(models.Model):
    nome = models.CharField(max_length=30)
    texto = models.TextField()
    area_Da_Empresa = models.CharField(max_length=30)

class mensagemArea(models.Model):
    responsavel = models.CharField(max_length=100)
    resposta = models.TextField()
    sugestionador = models.CharField(max_length=100)




