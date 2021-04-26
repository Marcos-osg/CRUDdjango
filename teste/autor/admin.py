from django.contrib import admin
from .models import Autor

# Register your models here.
class AutorAdmin(admin.ModelAdmin):
    list_display = ('id','nome',)
    list_display_links = ('id','nome',)


admin.site.register(Autor, AutorAdmin)