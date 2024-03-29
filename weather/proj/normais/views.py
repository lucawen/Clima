# -*- coding: utf-8 -*- 
#!/usr/bin/env python

from django.shortcuts import render, redirect
from django.http import HttpResponse
import models as db
from django.core import serializers
from django.template import RequestContext, loader
from forms import PesquisaEstacaoFRM, PesquisaAutomaticasFRM
from toolbox.tools import ObjectView

from normais.regras import NormalGraficos
from automaticas.graficos   import GeraGraficos
from automaticas.regras    import Medicao
from datetime import datetime
from django.utils import http
from django.shortcuts import  redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def loginusr(request):

    state = "Por favor informe seu usuario e senha..."
    username = password = ''
    
    template = loader.get_template('login.html')
    if request.POST:
        username = request.POST['usuario']
        password = request.POST['senha']
        
        user = authenticate(username=username, password=password)        
        if user is not None:
            if user.is_active:       
                login(request,user)                     
                return redirect('/dashboard/1/')                                           
            else:
                state = u"Sua conta esta desativada, por favor entre em contato com o administrador.."
        else:
            state = u"Seu usuario ou senha estao  incorretos.."            
            
            
    context = RequestContext(request, {'usuario': username, 'state':state } )                  
    return HttpResponse(template.render(context))

def sair(request):    
    logout(request)
    return redirect('/accounts/login')


@login_required()
def normais(request):

    if request.method == 'POST':
        form = PesquisaEstacaoFRM(request.POST)
        if form.is_valid():
            nomeEstac = form.cleaned_data['nomeEstacao']
            estacao = db.Station.objects.filter(Nome__contains = nomeEstac)
            texto     = u'{0}'.format(form.cleaned_data['nomeTexto'])

            if texto.strip() == '':
                texto = estacao[0].Nome
            
            texto = texto.replace('-',' ').replace('.',' ').replace('(',' ').replace(')',' ')
            texto = http.urlquote(texto)

            if estacao:
                return redirect('/grafnormais/{0}/{1}'.format(estacao[0].id, texto.replace(' ', '_')) ) 
    else:
        form = PesquisaEstacaoFRM()    

    colEstacoes = db.Station.objects.filter(tipo='N').values_list('Nome', flat=True)
    saida  = '['
    for i in colEstacoes:
        saida += '\'' +  i + '\','
    saida += ']'
    context = RequestContext(request, { 'estacoes': saida, 'form': form });
    template = loader.get_template('normais.html')   

    return HttpResponse(template.render(context))

@login_required()
def grafnormais(request, station, texto):

    texto = http.urlunquote(texto)
    estacao = {}
    try:
        estacao = db.Station.objects.get(pk=station)
    except:
        return redirect('/normais/')


    grf = NormalGraficos(station, texto).getGrafico()

    template = loader.get_template('grafnormais.html')   
    context = RequestContext(request, { 'estacao': estacao, 'graficos': grf });
    return HttpResponse(template.render(context))

@login_required()
def automaticas(request):

    if request.method == 'POST':

        form = PesquisaAutomaticasFRM(request.POST)
        if form.is_valid():
            nomeEstac = form.cleaned_data['nomeEstacao']
            mes       = form.cleaned_data['mes']
            ano       = form.cleaned_data['ano']
            texto     = u'{0}'.format(form.cleaned_data['nomeTexto'])
            estacao   = db.Station.objects.filter(Nome__contains = nomeEstac)

            if texto.strip() == '':
                texto = estacao[0].Nome

            texto = texto.replace('-',' ').replace('.',' ').replace('(',' ').replace(')',' ')
            texto = http.urlquote(texto)

            if estacao:
                if mes == '99':
                    return redirect(u'/grafautomaticatotal/{0}/{1}'.format(estacao[0].id,texto )) 
                else:
                    return redirect(u'/grafautomatica/{0}/{1}/{2}/{3}/'.format(estacao[0].Codigo, mes, ano,  texto )) 
    else:
        form = PesquisaAutomaticasFRM()    

    colEstacoes = db.Station.objects.filter(tipo='A').values_list('Nome', flat=True)
    saida  = '['
    for i in colEstacoes:
        saida += '\'' +  i + '\','
    saida += ']'
    context = RequestContext(request, { 'estacoes': saida, 'form': form });
    template = loader.get_template('automaticas.html')   

    return HttpResponse(template.render(context))

@login_required()
def grafAutomatica(request, station, ano, mes, texto):

    texto = texto.replace('_', ' ')

    obj = GeraGraficos()
    year = int(ano)
    month  = int(mes)
    if month  == 0:
        tipo = "A"
        month = 1
    else:
        tipo = 'D'

    datadefinida = datetime(year,month,1)
    result = obj.pool( station, datadefinida, tipo, texto)

    context = RequestContext(request, { 'result' : result} )
    template = loader.get_template('graflinha.html')   

    return HttpResponse(template.render(context))



def getautomaticajson(request, station):

    result = json.dumps( { 'dados' :  Medicao().graficos(station) } )

    return HttpResponse(result,content_type='text/javascript')


def dadosAutomatica(request, station):

    result = json.dumps( { 'dados' :  Medicao().graficos(station) } )

    return HttpResponse(result,content_type='text/javascript')

@login_required()
def grafAutomaticaTotal(request, station, texto):

    texto = texto.replace('_', ' ')

    estacao = {}
    try:
        estacao = db.Station.objects.get(pk=station)
    except:
        return redirect('/estacoes/')

    if texto.strip() == '':
        texto = estacao.Nome


    credits = {  'text': 'Powered by: Terravision',
                 'href': 'http://www.terravisiongeo.com.br/'
              }

    context = RequestContext(request, { 'estacao':  estacao, 'credits' : credits, 'texto': texto })
    template = loader.get_template('grafautomaticatotal.html')   

    return HttpResponse(template.render(context))

@login_required()
def mapaestacoes(request):
    context = RequestContext(request)
    template = loader.get_template('mapaestacoes.html')   

    return HttpResponse(template.render(context))

def mapafocoincendio(request):
    context = RequestContext(request)
    template = loader.get_template('mapafocoincendio.html')   

    return HttpResponse(template.render(context))

  
def focoCalor(request, id):

    print id

    reg =  db.FocoItem.objects.get(id=id)

    saida = { 'Temp' :  reg.Temp, 'FireFlag' : reg.FireFlag, 'Data' : reg.foco_FK.dataUTC, 'id' : reg.id }  
    context = RequestContext(request, { 'foco': saida } )

    template = loader.get_template('focoCalor.html')

    return HttpResponse(template.render(context))





