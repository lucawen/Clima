# -*- coding: utf-8 -*-
#!/usr/bin/env python

import django
from param.models import Unidade, Param
from projetos.models import Medicao, PtoMonit, Projeto, Campanha
import datetime
import xlrd
import chardet
from dateutil import parser


def pesquisa(ponto):


    descartar = ( 'IG130', 'IG140', 'DR001', 'DR002',\ 
    			  'DR003', 'TM001', 'TM002', 'TM014',\ 
    			  'TM015', 'C05', 'C08', 'TM001 \xbdZF',\ 
    			  'TM001 F', 'IG120 S' )
         
    dePara = (  ('SMA002', 'SM002'), ('SMA003','SM003),\
    			('CG004', 'CM004), ('CG001', 'CM001S),\
    			('CG002', 'CM002S),('SMA 001', 'SM001),\
    			('SMA002 S','SM002),('ML002','MA001'),\
    			('ML001','MA002') 
    			)
    
    if ponto in descartar:
        return ([], "XXXX")
        
    for item in dePara:
        if ponto == dePara[0]:
            query = PtoMonit.objects.filter(sigla = dePara[1])
            return (query, dePara[1])
        

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
 

    return (query,key)



def chacaPontos():

    ROW_INICIAL = 4

    lista = []

    workbook = xlrd.open_workbook(\
    '/home/wbeirigo/Clima/dados/sisagua/dados.xls')
    sheet = workbook.sheet_by_index(0)
    for row in range(ROW_INICIAL, sheet.nrows): 

        if sheet.cell(row,0).value == '':
            continue
        
        ponto = u'{0}'.format(sheet.cell(row,1).value)

        query, key = pesquisa(ponto) 
        lista.append([ ponto,  key, len(query) ] )


    for item in lista:
        print  u'{0};{1};{2};'.format(
                    item[0].encode('ascii','ignore'),
                    item[1],
                    item[2] )

    print len(lista)

def matriz():
    
    workbook = xlrd.open_workbook(\
    '/home/wbeirigo/cemig/matriz.xls')
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

def lerDataExcel(vlr):
    date = datetime.datetime(1899, 12, 30)
    get_ = datetime.timedelta(int(vlr))
    get_col2 = str(date + get_)[:10]
    d = datetime.datetime.strptime(get_col2, '%Y-%m-%d')
    return d.strftime('%d-%m-%Y')

def convert_excel_time(t, hour24=True):
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

    return "%d:%d:%d" % (hours, minutes, seconds)


def run():


    qtdErros = 0
    colPtosErrados = []
    colPontos = []
    col = []

    objMatriz = matriz()

    ROW_INICIAL = 6

    objProjeto = Projeto.objects.get(pk=1)

    campos = ('Campanha_FK', 'PtoMonit_FK'
              'Parametro_FK', 'controle'
              'data', 'dataInc'
              'vlr', 'vlrLbl')

    workbook = xlrd.open_workbook(\
    '/home/wbeirigo/cemig/matriz.xls')
    sheet = workbook.sheet_by_index(0)
    for linha in range(ROW_INICIAL, sheet.nrows):

        data = lerDataExcel(sheet.cell(linha,3).value)
        hora = convert_excel_time(sheet.cell(linha,4).value, False)
        #mask = '{0} {1}'.format(data, hora)
        mask = '{0}'.format(data)
        dataHora =  parser.parse(mask)


        """
        Campanha
        """
        colCampanha = Campanha.objects.\
                      filter(Projeto_FK_id = objProjeto.id,\
                             ano = dataHora.year,\
                             mes = dataHora.month)

        if len(colCampanha)  == 0:
            nmCamp = 'Campanha {0}/{1}'.format(dataHora.month, dataHora.year)
            objCampanha = Campanha( nome = nmCamp, 
                                    mes  =  dataHora.month,
                                    ano  =  dataHora.year,
                                    Projeto_FK = objProjeto)
            objCampanha.save()
        else:
            objCampanha = colCampanha[0]

        """
        Ponto de monitoramento
        """
        keyPto = u'{0}'.format(sheet.cell(linha,1).value)
        objPonto, keyPto1 = pesquisa(keyPto)
        if keyPto1 == 'XXXX':
            continue
        if keyPto != keyPto1 and keyPto not in col:
            col.append(keyPto)
            colPontos.append([linha, keyPto, keyPto1])
        if len(objPonto) == 0:
            if keyPto not in colPtosErrados:
                colPtosErrados.append(keyPto)
            qtdErros += 1
            continue

        """
        for coluna in objMatriz:
            keyParam = objMatriz[coluna]
            if '-' in str(keyParam) or str(keyParam).strip() == '':
                continue
            objParam = Param.objects.filter(id=keyParam)
            if len(objParam) == 0:
                print 'não achou parametro', keyParam 
                qtdErros += 1
                continue

            #Verifica sinal 
            sinal = ''
            if (coluna+1) in objMatriz:
                maskParamSinal = '{0}-1'.format(int(keyParam)) 
                if maskParamSinal == objMatriz[coluna +1]:
                    tipoSinal = str(sheet.cell(linha,coluna+1).value)
                    if tipoSinal== 'FALSE':
                        sinal = '<'
                    elif tipoSinal ==  'TRUE':
                        sinal = '>' 


            vlr = sheet.cell(linha,coluna).value
            if not  str(vlr).strip() in ('', 'FALSE', 'TRUE'):
                vlr = float( vlr)
                obj = Medicao(  Campanha_FK  = objCampanha,
                                PtoMonit_FK  = objPonto[0],
                                Parametro_FK = objParam[0],
                                controle     = '{0}'.format(linha),
                                data         = dataHora,
                                vlr          = vlr,
                                vlrLbl       = '{0}{1}'.format(sinal, vlr) )
                #obj.save()
        """

    print qtdErros
    print colPtosErrados
    print '-------------------------------------'
    for item in colPontos:
        print u'linha[{0}] de:[{1}] para:[{2}]'\
            .format(item[0], item[1], item[2])


