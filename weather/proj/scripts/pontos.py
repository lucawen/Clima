# -*- coding: utf-8 -*-
#!/usr/bin/env python

import django
from projetos.models import PtoMonit, Projeto, Layer
import datetime
import os
import sys
import xlrd



def run():
    
    caminho = '/home/wbeirigo/Clima/weather/proj/scripts/Pontos.xls'


    ptoRoot = PtoMonit.objects.get(id=2)
    projRoot = Projeto.objects.get(id=1)
    layerRoot = Layer.objects.get(id=1)


    workbook = xlrd.open_workbook(caminho)
    sheet = workbook.sheet_by_index(0)
    for row in range(0, sheet.nrows):
        val = sheet.cell(row,2).value

	if len( PtoMonit.objects.filter(nome=val)) == 0:

	    reg = PtoMonit( Projeto_FK = projRoot,
                            Layer_FK = layerRoot,
    		            sigla = '' ,
			    nome = val,
			    ObjectID = 0,
			    parent = ptoRoot )
	    reg.save()

            print u'{0}'.format(val)


    for row in range(1, sheet.nrows):
        sigla_val = sheet.cell(row,3).value
	id_val = sheet.cell(row,0).value
	reservat_val = sheet.cell(row,2).value
	nome_val = sheet.cell(row,4).value

    	ptoRoot = PtoMonit.objects.get(nome=reservat_val)

	if len( PtoMonit.objects.filter(sigla=sigla_val)) == 0:

	    reg = PtoMonit( Projeto_FK = projRoot,
                            Layer_FK = layerRoot,
    		            sigla = sigla_val ,
			    nome = nome_val,
			    ObjectID = int(id_val),
			    parent = ptoRoot )
	    reg.save()

            print u'{0}'.format(val)




