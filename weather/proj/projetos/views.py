# -*- coding: utf-8 -*- 
#!/usr/bin/env python 

from projetos.regras import Grafico
from django.db import models
from projetos.models import Campanha, PtoMonit
from param.models import Param
from projetos.forms import frmGrafico
from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
def viewGrafico(request):

    grafJson = ''
    if request.method == 'POST':
	form = frmGrafico(request.POST)
	if form.is_valid():
            idParametro = form.cleaned_data['parametro'].id
            idPonto =  form.cleaned_data['pontos'].id
            colPontos = [ vlr.id for vlr in  PtoMonit.objects.filter(parent = idPonto).all() ] 
            colCampanha =  [ vlr.id for vlr in form.cleaned_data['campanhas'] ]

	    grafJson  = Grafico().runJson(idParametro, colPontos, colCampanha) 

    else:

	form = frmGrafico()

    return render(request, 'frmGrafico.html', {'form': form, 'grafJson': grafJson} )
	
