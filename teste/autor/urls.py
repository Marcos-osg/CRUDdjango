from django.urls import path
from autor import views
from autor.views import ListaAutor, CriaAutor
from autor.views import EditarAutor, ExcluiAutor

urlpatterns = [
    path('', ListaAutor.as_view(), name='listar_autor'),
    path('novo_autor/',views.CriaAutor.as_view(), name='novo_autor'),
    path('editar_autor/<int:pk>', EditarAutor.as_view(), name='editar_autor'),
    path('excluir/<int:pk>',ExcluiAutor.as_view(), name='excluir_autor'),
]