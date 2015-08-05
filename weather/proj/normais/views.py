# -*- coding: utf-8 -*- 
#!/usr/bin/env python

from django.shortcuts import render
import simplejson as json
from django.http import HttpResponse
import models as db
from django.core import serializers
from django.template import RequestContext, loader

def registros(request, station, parametro):

    print station, parametro


    col = db.Resultado.objects.get(Station_FK__id= int(station), Parametro_FK__id= int(parametro) ) 

    meses = [ 'jan','fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago','stb', 'out', 'nov', 'dez']
    colec = col.__dict__

    dados = {}
    for item in meses:
        dados[item] = colec[item]
    
    templ = { 'mapa' : {
                        'titulo': col.Station_FK.Nome, 
                        'legenda': 'none',
                        'subtitulo': col.Parametro_FK.Nome,
                        'horiz' : '(meses)',
                        'vert' : col.Parametro_FK.unidade,
                       },
             'data':  dados
            }

    dado = json.dumps(templ)
    return HttpResponse(dado, content_type="application/json")


def mapa(request):
    colEstacoes = db.Station.objects.values_list('Nome', flat=True)

    colParam = db.Parametro.objects.values('id', 'Nome')
    
    saida  = '['
    for i in colEstacoes:
        saida += '\'' +  i + '\','
    saida += ']'

    context = RequestContext(request, { 'estacoes': saida, 'parametros': colParam  });
    template = loader.get_template('tela001.html')   
    return HttpResponse(template.render(context))

