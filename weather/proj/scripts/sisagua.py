# -*- coding: utf-8 -*-
#!/usr/bin/env python

import django
from param.models import Unidade, Param
from projetos.models import Medicao, PtoMonit, Projeto, Campanha
import datetime
import xlrd
import xlwt
import chardet
from dateutil import parser, tz
from datetime import datetime, date
from django.utils import timezone
import pytz

PLANILHA = '/media/projeto_cemig/01_PROJETO SOFTWARE/Dadosarodar/DadosCEMIG20132015.xls'

def pesquisa(ponto):


    descartar = ( u'IG130',   u'IG140', u'DR001', u'DR002',
                  u'DR003',   u'TM001', u'TM002', u'TM014',
                  u'TM015',   u'C05',   u'C08', u'TM001 \xbdZF',
                  u'TM001 F', u'IG120 S' )


    if ponto in descartar:
        return ([], "XXXX")


    dePara = (  (u'SMA002 \xbdZF',  u'SM002'), (u'SMA003',u'SM003'),
                (u'CG004',   u'CM004'), (u'CG001 \xbdZF', u'CM001S'),
                (u'SMA 001', u'SM001'), (u'CG001', u'CM001S'),
                (u'SMA002 S',u'SM002'), (u'ML002',u'MA001'),
                (u'ML001',   u'MA002'), (u'CG001 F', u'CM001S'),
                (u'CG002',   u'CM002'), (u'CG005',  u'CM005'),
                (u'P\xc7001',u'PC001'), (u'P\xc7002', u'PC002'),
                (u'SMA002',  u'SM002')
             )

    for de, para in dePara:
        if ponto == de:
            query = PtoMonit.objects.filter(sigla = para)
            return (query, para)


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


    return (query,key)


def matriz():

    workbook = xlrd.open_workbook(PLANILHA)
    sheet = workbook.sheet_by_index(0)

    col = {}
    for i in range(160):
        if i < 10:
            continue
        value = sheet.cell(0,i).value
        if str(value).strip() == '-' or\
           str(value).strip() == '':
           continue

        col[i] = sheet.cell(0,i).value

    return col



def Converte_Data(param):

    try:
        data_int = xlrd.xldate_as_tuple(int(param), 0)
        saida_1 = date(data_int[0], data_int[1], data_int[2])
    except:
        saida_1 = date(1900,1,1)

    return saida_1

def convert_excel_time(t, hour24=True):
    try:
        if t > 1:
            t = t%1
        seconds = round(t*86400)
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        if hour24:
           if hours > 12:
               hours -= 12
               return "%d:%d:%d PM" % (hours, minutes, seconds)
           else:
               return "%d:%d:%d AM" % (hours, minutes, seconds)
    except:
       hours = 0
       minutes = 0
       seconds = 0

    return int(hours), int(minutes), int(seconds)




def run():

    registros = []
    erros = []

    qtdErros = 0
    colPtosErrados = []
    colPontos = []

    objMatriz = matriz()

    ROW_INICIAL = 6

    workbook = xlrd.open_workbook(PLANILHA, formatting_info=True)
    sheet = workbook.sheet_by_index(0)
    for linha in range(ROW_INICIAL, sheet.nrows):

        data = Converte_Data(sheet.cell(linha,3).value)
        hora, minuto, segundo = convert_excel_time(sheet.cell(linha,4).value, False)

        data1 = datetime(data.year, data.month, data.day, hora, minuto, segundo)
        dataHora = pytz.timezone(django.utils.timezone.get_default_timezone_name()).localize(data1)

        keyPto = u'{0}'.format(sheet.cell(linha,8).value)


        objPonto, keyPto1 = pesquisa(keyPto)

        if keyPto1 == 'XXXX':
            continue
        if len(objPonto) == 0:
            if keyPto not in colPtosErrados:
                colPtosErrados.append(keyPto)
            qtdErros += 1
            continue





        for coluna in objMatriz:
            keyParam = objMatriz[coluna]
            if '-' in str(keyParam) or str(keyParam).strip() == '':
                continue
            objParam = Param.objects.filter(id=keyParam)
            if len(objParam) == 0:
                erros.append(keyParam)
                #print('não achou parametro', keyParam)
                continue

            #Verifica sinal
            sinal = ''
            if (coluna+1) in objMatriz:
                maskParamSinal = '{0}-1'.format(int(keyParam))
                if maskParamSinal == objMatriz[coluna +1]:
                    tipoSinal = str(sheet.cell(linha,coluna+1).value)
                    if tipoSinal ==  'TRUE':
                        sinal = '<'

            vlr = sheet.cell(linha,coluna).value
            if not  u'{0}'.format(vlr).strip() in ('', 'FALSE', 'TRUE'):
                vlr_grava= None
                lbl_grava = None
                try:
                    vlr_grava = float( vlr)
                    lbl_grava = '{0}{1}'.format(sinal, vlr)
                except:
                    vlr_grava = 0
                    lbl_grava = vlr

                registro = ( 'CEM{0}'.format(linha),
                            data1,
                            objPonto[0].sigla,
                            lbl_grava,
                            objParam[0].nome,
                            '-',
                            'Planilha Sisagua' )
                registros.append(registro)






    book = xlwt.Workbook(encoding='utf-8')
    sheet1 = book.add_sheet("SAIDA")
    index = 0
    arq = "/media/projeto_cemig/01_SOFTWARE/consolidado_sisagua.xls"
    indice = 0
    for reg in registros:
        row = sheet1.row(indice)
        col = 0
        for vlr in range(len(reg)):
            row.write(col, reg[vlr])
            col += 1
        indice += 1

    book.save(arq)

    print('Fim..')

