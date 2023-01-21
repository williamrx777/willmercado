from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Produto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models. DO_NOTHING)
    foto = models.ImageField(upload_to='foto')
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    pais = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nome