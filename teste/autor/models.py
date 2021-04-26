from django.db import models

# Create your models here.

class Autor(models.Model):
    nome = models.CharField(max_length=50, unique=True ,verbose_name='Nome do Autor')


    def __str__(self):
        return self.nome