from django.forms import ModelForm
from autor.models import Autor


class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = ('nome')
        