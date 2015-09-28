# -*- coding: utf-8 -*- 
#!/usr/bin/env python
import os
import sys
import xlrd
import xlwt

caminho = '/home/wbeirigo/Clima/dados/IGAM/'


planilhas = []
for files in os.walk(caminho):	
    for file in files:
        for item in  file:
		planilhas.append(caminho + item)



for caminho in planilhas:
    workbook = xlrd.open_workbook(caminho)
    sheet = workbook.sheet_by_index(0)
    for row in range(1, sheet.nrows):
        val = sheet.cell(row,2).value
        sigla_val = sheet.cell(row,3).value





