from django.db import models
from datetime import datetime
from autor.models import Autor

# Create your models here.
class Livro(models.Model):
    nome = models.CharField(max_length=50, unique=True, verbose_name='Nome do livro')
    autor = models.ForeignKey(Autor, on_delete=models.DO_NOTHING , verbose_name='Autor')
    qtd_pagina = models.IntegerField(verbose_name='Páginas')
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    data_inclusao = models.DateField(default=datetime.now ,verbose_name='Data de inclusão')


    def __str__(self):
        return self.nome