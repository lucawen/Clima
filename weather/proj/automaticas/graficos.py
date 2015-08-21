# -*- coding: utf-8 -*- 
#!/usr/bin/env python 


import psycopg2
import re
import requests
import json
import ast
from datetime import datetime, timedelta 
import time
import calendar


class GeraGraficos:

    def __init__(self):
        try:
            connstring = "host='10.3.0.29' dbname='clima' user='postgres' password='wilci5w7'"
            self.db  = psycopg2.connect(connstring)
        except:
             raise


    def defcategoria(self, _tipo, _data):

        if _tipo == 'd':
            faixa = [ int(dia) for dia in calendar.Calendar().itermonthdays(_data.year, _data.month) if dia >0]
        else:
            faixa = [ 'jan',  'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    
        faixa.insert(0,0)

        return faixa


    def defgrafico(self, _tipo, _lencategorias, _nomeestacao, _data):
   

        sql = '' 
        if _tipo == 'tempdiaria':
            titulo = u'Temperatura Diária  (Máxima, Média, Mínima)'
            subtitulo = u'Estação: {0}  -  {1}/{2}'.format(_nomeestacao, _data.month, _data.year)

            ytitle = 'Temperatura (°C)'

            campos = ['tempmed',  'tempmax',  'tempmin', ]
           
            tipo = 'line'
 
            sql = sql + 'avg("TempInst")     as tempmed, '
            sql = sql + 'avg("TempMax")      as tempmax, '
            sql = sql + 'avg("TempMin")      as tempmin  '

            group =   'GROUP BY "Data"' 

            series =  [ 
                        { 'name' : u'Temperatura Máxima'.encode('latin1'), 'color' : 'orange', 'data' : [] }  ,
                        { 'name' : u'Temperatura Média'.encode('latin1') , 'color' : 'yellow',    'data' : [] }  ,
                        { 'name' : u'Temperatura Mínima'.encode('latin1'), 'color' : 'green',   'data' : [] }  
                      ]

        if _tipo == 'tempmensal':
            titulo = u'Temperatura Mensal - (Máxima, Mínima)'
            subtitulo = u'Estação: {0}  -  {1}'.format(_nomeestacao, _data.year)

            ytitle = 'Temperatura (°C)'

            campos = ['tempmax',  'tempmin', ]
           
            tipo = 'line'
 
            sql = sql + 'max("TempMax")      as tempmax, '
            sql = sql + 'min("TempMin")      as tempmin  '

            group =   'GROUP BY "month(Data)"' 

            series =  [ 
                        { 'name' : u'Temperatura Máxima'.encode('latin1'), 'color' : 'orange', 'data' : [] }  ,
                        { 'name' : u'Temperatura Mínima'.encode('latin1'), 'color' : 'green',  'data' : [] }  
                      ]



 

 
        return {    'titulo'    : titulo,
                    'ytitle'    : ytitle, 
                    'campos'    : campos, 
                    'sql'       : sql, 
                    'group'     : group, 
                    'series'    : series, 
                    'type'      : tipo, 
                    'subtitulo' : subtitulo   }


    def processa(self, _codestac,  _data, _tipo, _nomeestac):

        diarios     = ['tempdiaria']
        periodo     = 'd' if _tipo in diarios else 'a'
        categoria   = self.defcategoria(periodo, _data ) 
        defgrafico  = self.defgrafico(_tipo, len(categoria), _nomeestac,  _data)


        if periodo == 'd':
            lastcategoria =  categoria[-1:][0]
            dataini = datetime(_data.year, _data.month, 1)
            datafim = datetime(_data.year, _data.month, lastcategoria)
        else:
            dataini = datetime(_data.year, 1, 1)
            datafim = datetime(_data.year, 12, 31)
 
        data       = [ [ 0 for  dia in categoria ]for i in defgrafico['series'] ]

        sql = ''
        sql = sql + 'SELECT "Data",                                 '
        sql = sql + defgrafico['sql']
        sql = sql + '       FROM "Clima_dadosestacao" d           '
        sql = sql + '              LEFT JOIN "Clima_estacoes" e ON d."codEstac" = e.codigo  '
        sql = sql + '       WHERE e.omm  = %s AND                                           '
        sql = sql + '             d."Data" BETWEEN %s AND %s                                '
        sql = sql + defgrafico['group']
        sql = sql + '       ORDER BY "Data"                                        '

        sql = sql + ';'


        try:
            cursor = self.db.cursor()
            dados = ( _codestac, dataini, datafim )
            cursor.execute(sql, dados)
            for item in  cursor.fetchall():
                indice = 0
                dia = item[0].day
                for cpo in defgrafico['campos']:
                    data[indice][dia] = round( item[indice+1], 2)
                    indice += 1
        except:
            raise
    
        self.db.close()

        indice = 0 
        for item in defgrafico['series']:
            defgrafico['series'][indice]['data'] = data[indice][1:]           
            indice += 1
 
        grafico = { 
                    'type':         defgrafico['type'], 
                    'titulo':       defgrafico['titulo'],
                    'subtitulo':    defgrafico['subtitulo'],
                    'categories':   categoria,
                    'ytitle':        defgrafico['ytitle'] ,
                    'series':       defgrafico['series']
                  }

        return grafico


