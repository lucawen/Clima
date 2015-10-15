# -*- coding: utf-8 -*-
#!/usr/bin/env python

import django
from param.models import Unidade, Param
from projetos.models import Medicao, PtoMonit, Projeto, Campanha
import datetime
import xlrd
import os
import sys
import xlwt

def xlsDate_as_datetime(xldate, datemode):
    # datemode: 0 for 1900-based, 1 for 1904-based
    return (
        datetime.datetime(1899, 12, 30)
        + datetime.timedelta(days=xldate + 1462 * datemode)
        )

def run():

    caminho = '/home/wbeirigo/Clima/dados/bioagri/'

    wb = xlwt.Workbook(encoding='utf-8') 
    ws = wb.add_sheet('Plan1')

    ln = 0
    ws.write(ln,0, 'contrato')
    ws.write(ln,1, 'data')
    ws.write(ln,2, 'ponto')
    ws.write(ln,3, 'valor')
    ws.write(ln,4, 'param')
    ws.write(ln,5, 'unidade')


    for e in os.walk(caminho):
        for file in e[2]:
            arquivo  = caminho + file
            workbook = xlrd.open_workbook(arquivo)
            sheet = workbook.sheet_by_index(0)
            for row in range(1, sheet.nrows):
		_contrato = sheet.cell(row,1).value
		_data = sheet.cell(row,15).value
		_ponto = sheet.cell(row,8).value
		_valor = sheet.cell(row,20).value
		_param = sheet.cell(row,19).value
		_unidade = sheet.cell(row,21).value

		if u'RESULTADO' in u'{0}'.format(_valor).upper():
		    continue

		print _valor
  		ln += 1
                ws.write(ln,0, _contrato)
                ws.write(ln,1, _data)
                ws.write(ln,2, _ponto)
                ws.write(ln,3, _valor)
                ws.write(ln,4, _param)
                ws.write(ln,5, _unidade)

    wb.save(caminho+'consolidado.xls')


