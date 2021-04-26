from django.urls import path
from livro import views
from livro.views import ListaLivro, NovoLivro

urlpatterns = [
    path('',views.ListaLivro.as_view(), name='listar_livro'),
    path('novo_livro/',views.NovoLivro.as_view(), name='novo_livro'),
    path('editar_livro/<int:pk>',views.EditarLivro.as_view(), name='editar_livro'),
    path('excluir_livro/<int:pk>',views.ExcluirLivro.as_view(), name='excluir_livro'),
]