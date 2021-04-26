from django.forms import ModelForm
from livro.models import Livro

class LivroModel(ModelForm):
    class Meta:
        model = Livro
        fields = ('__all__')