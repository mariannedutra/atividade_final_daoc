# Generated by Django 4.0.3 on 2022-06-06 20:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('slug', models.SlugField(max_length=250, verbose_name='Slug')),
                ('amigos', models.ManyToManyField(to='rede_social.pessoa')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
        migrations.CreateModel(
            name='Postagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.CharField(max_length=200, verbose_name='Conteudo')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Data de publicação')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rede_social.pessoa', verbose_name='Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.CharField(max_length=200, verbose_name='Comentario')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Data de publicação')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rede_social.pessoa', verbose_name='Usuario')),
                ('postagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rede_social.postagem', verbose_name='Postagens')),
            ],
        ),
    ]
