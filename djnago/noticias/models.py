from django.db import models
# -*- coding: utf-8 -*-
# Create your models here.

from datetime import datetime

class Noticia(models.Model):
    # ordenação das noticias pelo campo de publição (descendente, pelo sinal -)
    class Meta:
        ordering = ('-publicacao',)

    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    publicacao = models.DateTimeField(default=datetime.now, blank=True)
    url = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return self.titulo
    
def noticia_pre_save(signal, instance, sender, **kwargs):
    publicacao = instance.publicacao
    titulo = instance.titulo

    titulo_formatado = titulo.replace(" ", "-")
    publicacao_formatada = str(publicacao.year) + '/' + str(publicacao.month) + '/' + str(publicacao.day) 
    

    instance.url = publicacao_formatada + "/" + titulo_formatado

    
models.signals.pre_save.connect(noticia_pre_save, sender=Noticia) 
