# -*- coding: utf-8 -*-
#!/usr/bin/env python

import django
from param.models import Unidade, Param
from projetos.models import Medicao, PtoMonit, Projeto, Campanha
import datetime
import xlrd
import chardet


def run():

    toRemove = []
    fromTo = {} 
    dePara = [] 

    workbook = xlrd.open_workbook(\
            '/home/wbeirigo/Clima/weather/proj/scripts/Parametros_ajustes.xls')
    sheet = workbook.sheet_by_index(0)
    for row in range(1, sheet.nrows): 

        if sheet.cell(row,0).value == '':
            continue

        idReg    = int(sheet.cell(row,0).value)
        desc    =  u'{0}'.format((sheet.cell(row,1).value)).strip()

        isDelete = sheet.cell(row,2).value

        vlr = '0{0}'.format(sheet.cell(row,3).value)\
              .replace('.0','')\
              .replace('(NITRATO)', '').replace('(NITRITO)','')

        idFrom = int(vlr)
        if idFrom > 0:
            toRemove.append(idFrom)
            fromTo[desc] = idReg
            dePara.append([idFrom, idReg])

        if idReg == '':
            break

    print toRemove
    print "=================================="
    print fromTo
    print '=================================='
    print dePara

    for item in dePara: 
        query = Medicao.objects.filter(Parametro_FK_id = item[0])
        for it in query:
            it.Parametro_FK = Param.objects.get(id = item[1])
            it.save()


    for item in toRemove:
        query = Param.objects.filter(id = item)
        for reg in query: 
            reg.delete()
            reg.save()


