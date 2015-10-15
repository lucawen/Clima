# -*- coding: utf-8 -*- 
#!/usr/bin/env python
import os
import sys
from  igam.models import Pontos
from  dms2dec import dms2dec
import xlrd
import datetime
from  proj import settings

def trataPonto(str1, str2, str3):

	sec = u'{0}'.format(str3)
        if ',' not in sec:
	   sec = sec[0:-1]
	   sec += ',00"'


        result = u'{0} {1} {2}'.format( str1,\
                                        str2,\
                                        sec)\
		             .replace('-','')\
   	                     .replace("''", '"') + 'S'

	return result


def ImportaPontosIGAM():

    caminho = settings.IGAM_PATH

    arquivos = []
    for files in os.walk(caminho):	
	for item in  files[2]:
            arquivos.append(caminho + '/' + item)

    campos = ["upgrh",     "estacao",\
              "descricao", "classeEnquad",\
              "datEstab",  "",\
              "Bacia",     "SubBacia",\
              "CursoDAgua", "estado",\
              "municipio",\
              "","","","",\
              "","","","",\
              "altitude",  "tipoCorpDAgua",\
              "posicao",   "objects", ]
    
    objPontos = Pontos.objects.all()
    objPontos.delete()
    objPontos.update()


    colecPontos = []
    for item in arquivos:
        workbook = xlrd.open_workbook(item)
        sheet = workbook.sheet_by_index(0)

        for row in range(1, sheet.nrows): 
            objPontos = Pontos()

            key = str(sheet.cell(row,1).value)
            if key in colecPontos:
                indice +=1
                continue

            strlat = trataPonto(sheet.cell(row,11).value,\
                                sheet.cell(row,12).value,\
                                sheet.cell(row,13).value)

            strlng = trataPonto(sheet.cell(row,14).value,\
                                sheet.cell(row,15).value,\
                                sheet.cell(row,16).value)

            lati   = dms2dec(strlat) * -1
            longi  = dms2dec(strlng) * -1

            objPontos.posicao = 'SRID=4326;POINT({0} {1})'.format(longi, lati)

            indice = 0
            for col in range(0, sheet.ncols): 
                if campos[indice] != "":
                    if indice in (4,5) :
                        vlr = int(sheet.cell(row,indice).value)
                        valor = datetime.date(1900, 1, 1) + datetime.timedelta(vlr-2)
                        setattr(objPontos, campos[indice], valor)
                    else:
                        setattr(objPontos, campos[indice], sheet.cell(row,indice).value)
                indice += 1
            objPontos.save() 
            colecPontos.append(key)




