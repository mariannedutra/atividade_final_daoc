from django.contrib import admin

from rede_social.models import Comentario, Postagem, Pessoa

# Register your models here.

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    pass

@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    pass

@admin.register(Comentario)
class Comentario(admin.ModelAdmin):
    pass
