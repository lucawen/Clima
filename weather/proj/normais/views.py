# -*- coding: utf-8 -*- 
#!/usr/bin/env python

from django.shortcuts import render, redirect
import simplejson as json
from django.http import HttpResponse
import models as db
from django.core import serializers
from django.template import RequestContext, loader
from forms import PesquisaEstacaoFRM
from normais.modelos import ChartsTypes
from scripts.tools import ObjectView


def registros(request, station):

    print station

    meses = [ 'jan','fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago','stb', 'out', 'nov', 'dez']
    colecao = []
    for col in  db.Resultado.objects.filter(Station_FK__id= int(station)):
        nomeEstacao =  col.Station_FK.Nome
        nomeParam = col.Parametro_FK.Nome
        nomeUnid = col.Parametro_FK.unidade

        dicionario = col.__dict__

        for chave in dicionario.keys():
            if chave not in meses:
                del dicionario[chave]

        templ = { 'mapa' : {
                            'titulo': nomeEstacao, 
                            'legenda': 'none',
                            'subtitulo': nomeParam,
                            'horiz' : '(meses)',
                            'vert' : nomeUnid,
                            'data':  dicionario
                            }
                }
        colecao.append(templ)

    dado = json.dumps(colecao)
    return HttpResponse(dado, content_type="application/json")




def grafico(request, station):

    meses = [ 'jan','fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago','stb', 'out', 'nov', 'dez']

    drawGoogleChart = []
    for col in  db.Resultado.objects.filter(Station_FK__id= int(station)):

        if col.Parametro_FK.tipoMapa.strip() == '':
            tipoMapa = 'LN'
        else:
            tipoMapa = col.Parametro_FK.tipoMapa

        dicionario = col.__dict__

        chart_options = {
            'title': col.Parametro_FK.Nome,
            'hAxis': {'title': '(meses)', 'titleTextStyle': {'color': 'red'}},
            'backgroundColor': '#fcfcfc',
            'vAxis': {'title': col.Parametro_FK.unidade, 'titleTextStyle': {'color': 'blue'}}
        };

        chart_data = []
        for mes in meses:
            chart_data.append( { 'mes': mes,'val' : dicionario[mes] } )            

        chart_element = 'google-chart-{0}'.format(col.id)
        chart_type = ChartsTypes().getBySigla(tipoMapa)

        linha = {   'id' : '{0}'.format(col.id),
                    'chart_data' : chart_data, 
                    'chart_options': chart_options, 
                    'chart_element': chart_element, 
                    'chart_type': chart_type, 
                    'chart_element':  chart_element  } 
        drawGoogleChart.append( ObjectView(linha) )



    template = loader.get_template('tela002.html')   
    context = RequestContext(request, { 'graficos': drawGoogleChart });
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




