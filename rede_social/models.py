from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=50)

    slug = models.SlugField('Slug', max_length=250)

    usuario = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        verbose_name='Usuário')
    
    amigos = models.ManyToManyField('Pessoa', blank=True)

    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super(Pessoa, self).save(*args, **kwargs)


class Postagem(models.Model):

  pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Usuario" )

  conteudo = models.CharField('Conteudo', max_length=200)

  data = models.DateTimeField("Data de publicação", auto_now_add=True)

  def __str__(self):
    return self.conteudo

class Comentario(models.Model):

  pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Usuario")
  postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE, verbose_name="Postagens")
  conteudo = models.CharField('Comentario', max_length=200)
  data = models.DateTimeField("Data de publicação", auto_now_add=True)
  
  def __str__(self):
     return self.conteudo
