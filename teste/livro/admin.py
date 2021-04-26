from django.contrib import admin
from .models import Livro

# Register your models here.
class LivroAdmin(admin.ModelAdmin):
    list_display = ('id','nome','autor','qtd_pagina','preco','data_inclusao',)
    list_display_links = ('id','nome','autor',)


admin.site.register(Livro, LivroAdmin)