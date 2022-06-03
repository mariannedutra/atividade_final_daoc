from django.urls import path

from rede_social.views import index, perfil_template

urlpatterns = [
    path('', index, name="index"),
    path('perfil/<str:slug>/', perfil_template, name='perfil')
]
