from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from livro.models import Livro
from django.urls import reverse_lazy

# Create your views here.
class ListaLivro(ListView):
    template_name = 'livros/lista.html'
    model = Livro
    context_object_name = 'livros'

class NovoLivro(CreateView):
    model = Livro
    fields = '__all__'
    template_name = 'livros/form-livro.html'
    success_url = reverse_lazy('listar_livro')

class EditarLivro(UpdateView):
    model = Livro
    fields = '__all__'
    template_name = 'livros/form-livro.html'
    success_url = reverse_lazy('listar_livro')

class ExcluirLivro(DeleteView):
    model = Livro
    template_name = 'livros/delete-livro.html'
    success_url = reverse_lazy('listar_livro')