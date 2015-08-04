# -*- coding: utf-8 -*-
#!/usr/bin/env python

import xlrd


class ObjectView(object):
    def __init__(self, d):
        self.__dict__ = d

class PlanilhaExcel:

    def leituraPlanilha(self, param):

        base = {}

        book = xlrd.open_workbook(param['planilha'], formatting_info=True) 
        sheet = book.sheet_by_index(0)
        inicio = param['rowInic'] 
        rows, cols = sheet.nrows, sheet.ncols
   
        for row in range(inicio,rows):
            rg = {}

            for it in param['campos']:
                nomeCampo = it[0]
                col = it[2]

                vlr = sheet.cell(row, col).value
                if it[1] == 'N':
                    try:
                        valor =  float(vlr)
                    except:
                        valor = -99
                else:
                    valor =  u'{0}'.format(vlr).replace('.0','')

                rg[nomeCampo] = valor

            if str(param['key']).strip() == '':
                break

            chave = rg[ param['key']]
            base[chave] = rg

        return base


