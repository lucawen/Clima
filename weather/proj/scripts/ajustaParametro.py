# -*- coding: utf-8 -*-
#!/usr/bin/env python

import django
from param.models import Unidade, Param
from projetos.models import Medicao, PtoMonit, Projeto, Campanha
import datetime
import xlrd
import chardet
import mptt

def run():

    toRemove = []
    fromTo = {} 
    dePara = [] 

    NODE_LIXO = 780

    workbook = xlrd.open_workbook(\
            '/home/wbeirigo/Clima/weather/proj/scripts/Parametros_ajustes.xls')
    sheet = workbook.sheet_by_index(0)
    for row in range(1, sheet.nrows): 

        if sheet.cell(row,0).value == '':
            continue

        idReg    = int(sheet.cell(row,0).value)
        desc    =  u'{0}'.format((sheet.cell(row,1).value)).strip()

        vlr = '0{0}'.format(sheet.cell(row,3).value)\
              .replace('.0','')\
              .replace('(NITRATO)', '').replace('(NITRITO)','')

        idFrom = int(vlr)

        if sheet.cell(row,2).value == 'x' :
            toRemove.append(idReg)

        if idFrom > 0:
            fromTo[desc] = idReg
            dePara.append([idFrom, idReg])

        if idReg == '':
            break

    print toRemove
    print "=================================="
    print fromTo
    print '=================================='
    print dePara


    paramLixo = Param.objects.get(id=NODE_LIXO)

    for item in toRemove:
        query = Param.objects.filter(id = item)
        for reg in query: 
            reg.move_to(paramLixo)
            reg.save()


