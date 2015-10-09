# -*- coding: utf-8 -*-
#!/usr/bin/env python

import django
from param.models import Unidade, Param
from projetos.models import Medicao, PtoMonit, Projeto, Campanha
import datetime
import xlrd
import chardet


def pesquisa(ponto):
    ponto = ponto.replace('1/2','')
    ponto = ponto.encode('ascii',errors='ignore').encode('utf-8') 
    ponto = ponto.replace(' L','')
    ponto = ponto.replace(' ','')
    ponto = ponto.replace('IL','')
    ponto = ponto.replace('IVL','')

    ponto = ponto.replace('LS','S')
    ponto = ponto.replace('LZF','ZF')
    ponto = ponto.replace('L12ZF','ZF')
    ponto = ponto.replace('12ZF','ZF')
    ponto = ponto.replace('LF','F')
    ponto = ponto.replace('SV','SV0')
    ponto = ponto.replace('SPV','SP0')
    ponto = ponto.replace('NP0','NP')
    ponto = ponto.replace('SC0','SCLI')
    ponto = ponto.replace('XC','XC0')
    ponto = ponto.replace('JG','JG0')
    ponto = ponto.replace('IG-LI-','IGLI')

    if ponto[-1:] == 'S':
        ponto = ponto[:-1]

    if ponto[-1:] == 'S':
        ponto = ponto[:-1]



    key = ponto
    query = PtoMonit.objects.filter(sigla = key)
    if len(query) == 0:
        key = ponto + 'S'
        query = PtoMonit.objects.filter(sigla = key)
    if len(query) == 0:
        key = ponto.replace('00','0')
        query = PtoMonit.objects.filter(sigla = key)
    if len(query) == 0:
        key = key + 'S'
        query = PtoMonit.objects.filter(sigla = key)
 

    return (query,key, ponto)

def run():

    ROW_INICIAL = 4

    notFound = []

    workbook = xlrd.open_workbook(\
    '/home/wbeirigo/Clima/dados/sisagua/dados.xls')
    sheet = workbook.sheet_by_index(0)
    for row in range(ROW_INICIAL, sheet.nrows): 

        if sheet.cell(row,0).value == '':
            continue
        
        ponto = u'{0}'.format(sheet.cell(row,1).value)

        query, key, tratado = pesquisa(ponto) 
        if len(query) == 0:
            notFound.append([ key,ponto,tratado ] )
            continue


    for item in notFound:
        print item

    print len(notFound)
