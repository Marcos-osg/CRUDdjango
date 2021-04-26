from django.shortcuts import render, redirect
from autor.models import Autor
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



# Create your views here.
class ListaAutor(ListView):
    template_name = 'autor/lista.html'
    model = Autor
    context_object_name = 'autores'


class CriaAutor(CreateView):
    model = Autor
    fields = ['nome']
    template_name = 'autor/form.html'
    success_url = reverse_lazy('listar_autor')

class EditarAutor(UpdateView):
    model = Autor
    fields = ['nome']
    template_name = 'autor/form.html'
    success_url = reverse_lazy('listar_autor')

class ExcluiAutor(DeleteView):
    model = Autor
    template_name = 'autor/delete.html'
    success_url = reverse_lazy('listar_autor')