from django.contrib import admin
from rede_social.models import Pessoa, Postagem, Comentario


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    pass

@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    pass

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    pass
