# -*- coding: utf-8 -*- 
#!/usr/bin/env python

from django.shortcuts import render, redirect
import simplejson as json
from django.http import HttpResponse
import models as db
from django.core import serializers
from django.template import RequestContext, loader
from forms import PesquisaEstacaoFRM
from scripts.tools import ObjectView

from normais.regras import NormalGraficos


def grafico(request, station):

    estacao = {}
    try:
        estacao = db.Station.objects.get(pk=station)
    except:
        return redirect('/estacoes/')


    grf = NormalGraficos(station).getGrafico()

    template = loader.get_template('tela002.html')   
    context = RequestContext(request, { 'estacao': estacao, 'graficos': grf });
    return HttpResponse(template.render(context))


def estacoes(request):


    colEstacoes = db.Station.objects.values_list('Nome', flat=True)
    if request.method == 'POST':

        form = PesquisaEstacaoFRM(request.POST)
        if form.is_valid():
            nomeEstac = form.cleaned_data['nomeEstacao']
            estacao = db.Station.objects.filter(Nome__contains = nomeEstac)
            if estacao:
                return redirect('/grafico/{0}'.format(estacao[0].id) ) 

    else:
        form = PesquisaEstacaoFRM()    

    saida  = '['
    for i in colEstacoes:
        saida += '\'' +  i + '\','
    saida += ']'
    context = RequestContext(request, { 'estacoes': saida, 'form': form });
    template = loader.get_template('tela001.html')   

    return HttpResponse(template.render(context))




