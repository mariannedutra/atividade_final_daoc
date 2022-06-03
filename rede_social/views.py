
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render

from .models import Pessoa

def index(request):
  return HttpResponse('Página Inicial')

def perfil_template(request,slug):
  try:
    perfil = Pessoa.objects.get(slug=slug)

  except Pessoa.DoesNotExist:
    raise Http404('Perfil não encontrado')
    
  return render(request, 'rede_social/perfil.html', {'perfil': perfil})