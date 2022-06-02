from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Usuario(models.Model):
    nome = models.CharField('Nome', max_length=50)

    slug = models.SlugField('Slug', max_length=250)

    nome_usuario = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        verbose_name='Usuário')


    email = models.EmailField(
        'E-mail', 
        null=True, 
        blank=True)

    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super(Usuario, self).save(*args, **kwargs)


class Postagens(models.Model):

  usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuario" )

  conteudo = models.CharField('Conteudo', max_length=200)

  def __str__(self):
    return self.conteudo

class RelacionamentoUsuarios(models.Model):

  relacionamentoUsuarios = models.ManyToManyField(Usuario)
  
  def __str__(self):
    return self.relacionamentoUsuarios

class Comentario(models.Model):

  usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, verbose_name="Usuario")
  postagem = models.ForeignKey(Postagens, on_delete=models.CASCADE, verbose_name="Postagens")
  conteudo = models.CharField('Comentario', max_length=200)


  def __str__(self):
     return self.conteudo
