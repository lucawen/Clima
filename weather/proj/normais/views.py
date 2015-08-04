# -*- coding: utf-8 -*- 
#!/usr/bin/env python

from django.shortcuts import render


from django.http import HttpResponse
import datetime
import models as db
from django.core import serializers
from django.template import RequestContext, loader

def registros(request):
    col = db.Resultado.objects.filter(Station_FK__id= 1494, Parametro_FK__id=149)
    data = serializers.serialize('json', col)
    return HttpResponse(data,content_type='text/javascript')


"""
def mapa(request):
    template = loader.get_template('mapa.html')      
    return HttpResponse(template.render(request))
"""
