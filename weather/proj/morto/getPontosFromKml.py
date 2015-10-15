# -*- coding: utf-8 -*- 
#!/usr/bin/env python 

from django.contrib.gis.gdal import DataSource
import os
import sys
from os import walk
import xlwt
from xlutils.copy import copy # http://pypi.python.org/pypi/xlutils
import xlrd 
from projetos.models import PtoMonit

def leitura():
	book = xlwt.Workbook()
	sheet1 = book.add_sheet("pontos")

	path = '/home/wbeirigo/Clima/dados/cemig'
	f = []
	for (dirpath, dirnames, filenames) in walk(path):
	    f.extend(filenames)
	    break

	pm = []
	index = 0
	for itFile in f:
	    ds = DataSource(path + '/' + itFile)
	    layer = ds[0]

	    campos =  layer.get_fields('Name')
	    pontos =  [pt.tuple for pt in layer.get_geoms()]

	    for indice in range(len(pontos)):
		cpos = [ campos[indice].encode('ascii', 'ignore').replace(' ',''), str(pontos[indice][0]).replace('.',','), str(pontos[indice][1]).replace('.',',') ] 
	    
		col = 0
		row = sheet1.row(index)
		for item in  cpos: 
		    row.write(col, item)
		    col += 1
		index += 1

	book.save("pontosCaminhamento.xls")


def processa():

    file_path = 'scripts/pontosCaminhamento.xls'
    file_out = 'scripts/pontosProcessados.xls'

    rb = xlrd.open_workbook(file_path,formatting_info=True)
    r_sheet = rb.sheet_by_index(0) 

    wb = copy(rb) 
    sheet = wb.get_sheet(0) 

    row = 0
    for row in range(1,r_sheet.nrows):
        ponto = u'{0}'.format(  r_sheet.cell(row,0).value )
        pontos = PtoMonit.objects.filter(sigla = ponto)
        if len(pontos) == 0:	
            sheet.write(row,3,'not found!')    

    wb.save(file_out)


def run():
    processa()





