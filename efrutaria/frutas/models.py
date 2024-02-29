# frutas/models.py
from django.db import models

class Fruta(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='frutas/images/')

    def __str__(self):
        return self.nome
