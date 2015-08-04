# -*- coding: utf-8 -*-
#!/usr/bin/env python

import xlrd
import dms2dec
import json

def leituraPlanilha(param):

    base = {}

    book = xlrd.open_workbook(param['planilha'], formatting_info=True) 
    sheet = book.sheet_by_name('Plan1')     
    rows, cols = sheet.nrows, sheet.ncols
   
    for row in range(2,rows-2):
        rg = {}
        
        for it in campos:
            nomeCampo = it[0]
            col = it[2]
        
            if it[1] == 'N':
                valor =  float(sheet.cell(row, col).value)
            else:
                valor =  sheet.cell(row, col).value
                valor =  u'{0}'.format(valor).replace('.0','')

            rg[nomeCampo] = valor

        chave = rg[ param['key']]
        print chave
        base[chave] = rg

    return base







campos = [
            ['Codigo',   'C', 0],
            ['Nome',     'C', 1],
            ['Estadoi',  'C', 2], 
            ['UF',       'C', 3],      
            ['Latitude', 'C', 4], 
            ['Longitude','C', 5],
            ['Altitude', 'N', 6],
            ['Tmed',     'C', 7],
            ['Tmax',     'C', 8],
            ['Tmin',     'C', 9],
            ['TmaxAbs',  'C', 10],
            ['TminAbs',  'C', 11],
            ['Colunas4', 'C', 12],
            ['Colunas5', 'C', 13],
            ['Pres',     'C', 14],
            ['Inso',     'C', 15],
            ['Evap',     'C', 16],
            ['Neb',      'C', 17  ],
            ['NebHora',  'C', 18],
            ['UR',       'C', 19],
            ['URHora',   'C', 20],
            ['Prec',     'C', 21],
            ['PrecMax',  'C', 22],
            ['PrecNDias','C', 23],
            ['PDec',     'C', 24],
            ['PdecND',   'C', 25],
            ['NPSec',    'C', 26],
            ['VentoInt', 'C', 27],
            ['Ventou',   'C', 28],
            ['Ventov',   'C', 29],
            ['VentoDirRes',  'C', 30],
            ['VentoDirPred', 'C', 31],
            ['NNormais',     'N', 32],
]

plan = {'planilha': '../Relac_Est_Meteo_NC.xls', 'campos':campos, 'key':'Codigo' } 

col = leituraPlanilha(plan)

saida = json.dumps(col)


print saida

