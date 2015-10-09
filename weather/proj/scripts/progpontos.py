# -*- coding: utf-8 -*- 
#!/usr/bin/env python
import os
import sys
from  projetos.models import PtoMonit
from  dms2dec import dms2dec
import xlrd
import datetime
import psycopg2

def run():

    try:
        connstring = "host='10.2.8.239' dbname='geonode_data'\
                     user='geonode' password='FsBUYSRW'"
        db  = psycopg2.connect(connstring)
    except:
        raise


    caminho = '/home/wbeirigo/Clima/dados/PontosOficial.xls'

    workbook = xlrd.open_workbook(caminho)
    sheet = workbook.sheet_by_index(0)

    id = 50

    ptosNotFound = []

    for row in range(1, sheet.nrows): 

        key = str(sheet.cell(row, 4).value).strip().replace(' ','')

        if key == 'X' or key == '':
            continue

        pesquisa = PtoMonit.objects.filter(sigla = key)
        if len(pesquisa) == 0:
            ptosNotFound.append(key)
            continue

        ponto = pesquisa[0]
        ponto.ObjectID = id
        ponto.save()

        local = key
        lat   = float(str(sheet.cell(row,1).value).replace(',','.'))
        longi = float(str(sheet.cell(row,2).value).replace(',','.'))

        cursor = db.cursor()
        try:
            sql = 'INSERT INTO cemig_pontos(\
                    fid, the_geom, "Name")\
                            VALUES (%s, ST_GeomFromText(\'POINT(%s %s)\',4326), %s);'
            dados = (id, lat, longi, local )
            cursor.execute(sql, dados)
            db.commit()
        except psycopg2.IntegrityError:
            db.rollback()
        else:
            db.commit()


        id += 1

    db.close()


    for item in ptosNotFound:
        print item

    print 'Fim'


