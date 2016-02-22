# -*- coding: utf-8 -*-
#!/usr/bin/env python

import django
from param.models import Unidade, Param
from projetos.models import Medicao, PtoMonit, Projeto, Campanha
from toolbox.tools import ObjectView, xlsDate_as_datetime
from projetos.regras import getCampanha
from xlwt import Workbook
import time

PATH_ARQUIVO     = '/home/wbeirigo/Clima/dados/dadoslaborat/procmedicao.xls'
PATH_FERRAMENTA  = '/home/wbeirigo/Clima/dados/dadoslaborat/converte.xls'

def run():

    col_label_param = {}
    for item in Param.objects.values('id','nome', 'vlrTeto', 'vlrPiso').all():
       col_label_param[ item['id'] ] = [ item['nome'],  item['vlrPiso'], item['vlrTeto'] ]

    col_label_ponto = {}
    for item in PtoMonit.objects.values('id','sigla').all():
       col_label_ponto[ item['id'] ]  = item['sigla']



    col_label_Ponto = PtoMonit.objects.all()

    # .filter(PtoMonit_FK_id=2448)
    col_param = []
    col_linha = []
    result = []
    colMedicao =  Medicao.objects.values('data', 'PtoMonit_FK_id', 'Parametro_FK_id', 'vlr').order_by('data', 'PtoMonit_FK_id', 'Parametro_FK_id')
    linha = []
    for item in colMedicao:

        key_param = ( item['Parametro_FK_id'])
        try:
            indice_param = col_param.index(key_param)
        except ValueError:
            col_param.append(key_param)
            indice_param = col_param.index(key_param)

        key_linha = (item['data'], item['PtoMonit_FK_id'])
        try:
            indice_linha = col_linha.index(key_linha)
        except ValueError:
            col_linha.append(key_linha)
            indice_linha = col_linha.index(key_linha)

        registro = (indice_linha, indice_param, item['vlr'])

        result.append(registro)


    print('len(result), len(col_param), len(col_linha), len(col_label_ponto), len(col_label_param)')
    print(len(result), len(col_param), len(col_linha), len(col_label_ponto), len(col_label_param))


    workbook = Workbook()
    sheet = workbook.add_sheet('Sheet1')

    for item in col_param:
        y = col_param.index(item)
        y += 10
        sheet.write(0, y, col_label_param[item][0])
        sheet.write(1, y, col_label_param[item][1])
        sheet.write(2, y, col_label_param[item][2])

    for item in col_linha:
        x = col_linha.index(item)
        x += 10
        sheet.write(x, 0, col_label_ponto[item[1]] )
        dt = item[0]
        try:
            sheet.write(x, 1, '{0}/{1}/{2}'.format(dt.day, dt.month, dt.year) )
        except:
            print(dt )


    for item in result:
        x, y, z = item
        x += 10
        y += 10
        z = z
        try:
            sheet.write(x, y, z)
        except:
            pass

    path_saida = '/home/wbeirigo/dados/wilson.xls'
    workbook.save(path_saida)


