
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render

from .models import Usuario

def index(request):
  return HttpResponse('Página Inicial')

def perfil_template(request,slug):
  try:
    perfil = Usuario.objects.get(slug=slug)

  except Usuario.DoesNotExist:
    raise Http404('Perfil não encontrado')
    
  return render(request, 'atividade_inicial/perfil.html', {'perfil': perfil})