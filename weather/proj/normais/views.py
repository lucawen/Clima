# -*- coding: utf-8 -*- 
#!/usr/bin/env python

from django.shortcuts import render

import json
from django.http import HttpResponse
import datetime
import models as db
from django.core import serializers
from django.template import RequestContext, loader

def registros(request):
    col = db.Resultado.objects.filter(Station_FK__id= 1494, Parametro_FK__id=149).fields()
    data = serializers.serialize('json', col)
    return HttpResponse(data,content_type='text/javascript')


def mapa(request):
    col = db.Resultado.objects.get(Station_FK__id= 1494, Parametro_FK__id=149)

    templ = { 'mapa' : {
                        'titulo':'Mariana', 
                        'legenda': 'none',
                        'sub_tiulo': 'xxxxxxxxxxxxxxxxx',
                        'horiz' : '(meses)',
                        'vert' : '(mm)',
                       },
              'dados': col
            }

    context = RequestContext(request, templ )

    template = loader.get_template('grafico.html')      
    return HttpResponse(template.render(context))
