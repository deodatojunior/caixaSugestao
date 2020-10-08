from django.db import models
from django.conf import settings
from django import forms
# Create your models here.

class Sugestao(models.Model):
    titulo = models.CharField(max_length=30)
    texto = models.TextField()
    area_Da_Empresa = models.CharField(max_length=30)





