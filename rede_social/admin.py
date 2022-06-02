from django.contrib import admin

from rede_social.models import Comentario, Postagens, RelacionamentoUsuarios, Usuario

# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    pass

@admin.register(Postagens)
class PostagensAdmin(admin.ModelAdmin):
    pass

@admin.register(Comentario)
class Comentario(admin.ModelAdmin):
    pass
