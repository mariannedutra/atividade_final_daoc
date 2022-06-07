
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.db.models import Prefetch

from .models import Pessoa, Postagem

def index(request):
  return HttpResponse('Página Inicial')

def perfil_template(request,slug):
  try:
    perfil = Pessoa.objects.prefetch_related(
      Prefetch('postagem_set', queryset=Postagem.objects.order_by('-data'))
    ).get(slug=slug)

  except Pessoa.DoesNotExist:
    raise Http404('Perfil não encontrado')
    
  return render(request, 'rede_social/perfil.html', {'perfil': perfil})