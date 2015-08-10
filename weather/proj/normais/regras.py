# -*- coding: utf-8 -*- 
#!/usr/bin/env python

import django
from normais.models import Parametro, Classe, Resultado
import itertools
import json
import decimal

class TipoGrafico:

	def getAll(self):

		chartType = [
				[ 'CL', 'google.visualization.ColumnChart'],
				[ 'PI', 'google.visualization.PieChart'],
				[ 'SC', 'google.visualization.ScatterChart'],
				[ 'BB', 'google.visualization.BubbleChart'],
				[ 'GO', 'google.visualization.GeoChart'],
				[ 'LN', 'google.visualization.LineChart'],
			]
		return chartType

	def getBySigla(self, sigla ):
		return [x[1] for x in self.getAll() if x[0] == sigla][0]




class NormalGraficos():

    def __init__(self, _idStation):
        self.idStation = _idStation


    def getEixo(self, idSerie):

        meses = ['jan','fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago','stb', 'out', 'nov', 'dez']

        if idSerie == 99:
            titulo = '(meses)'
            serie = meses
            serie.insert(0,'meses') 
        else:

            reg = Parametro.objects.get(codigo = idSerie)
            titulo = u'({0})'.format(reg.unidade)
            serie = []

            result = Resultado.objects.filter(Station_FK_id = self.idStation, Parametro_FK_id = reg.id)
            if len(result) > 0:
                dicionario = result[0].__dict__
                serie.append( reg.Nome.encode('latin-1') )
                for mes in meses:
                    serie.append( float(dicionario[mes])) 

        saida = { 'titulo' : titulo, 'serie' : serie } 

        return saida 


    def geraDataTable(self, eixo):

        qtdCols = len(eixo[0]['serie'])
        qtdRows = len(eixo)

        tabela = []
        for col in range(qtdCols):
            colLinha = []
            for linha in range(qtdRows):
                colLinha.append( eixo[linha]['serie'][col] )                               

            print colLinha 
            tabela.append(colLinha)        
      
        return tabela 


    def getGrafico(self):

        colGraficos = []
        col = [    { 'id': 1, 'title': 'Precipitação Acumulada',      'tipo': 'CL', 'series' : [99,11,] },  
                    { 'id': 2, 'title': 'Temperaturas',                'tipo': 'LN', 'series' : [99,1,2,3,] } ,  
                   { 'id': 3, 'title': 'Precipitação Máxima 24h',     'tipo': 'CL', 'series' : [99,12,] } ,  
                   { 'id': 4, 'title': 'Temperatura Mínima Absoluta', 'tipo': 'LN', 'series' : [99,4,] } ,  
                   { 'id': 5, 'title': 'Temperatura Máxima Absoluta', 'tipo': 'LN', 'series' : [99,5,] } , 
                   { 'id': 6, 'title': 'Deficit e Superávit Hídrico', 'tipo': 'LN', 'series' : [99,19,] } ,  
                   { 'id': 7, 'title': 'Umidade Relativa',            'tipo': 'CL', 'series' : [99,10,] } ,  
                   { 'id': 8, 'title': 'Nebulosidade',                'tipo': 'LN', 'series' : [99,9,] } ,  
                   { 'id': 9, 'title': 'Pressão',                     'tipo': 'LN', 'series' : [99,6,] },  
                   { 'id':10, 'title': 'Insolação',                   'tipo': 'CL', 'series' : [99,7,] } ,  
                   { 'id':11, 'title': 'Dias sem Chuva',              'tipo': 'CL', 'series' : [99,13,] } ,  
                   { 'id':12, 'title': 'Direção Predominante do Vento', 'tipo': 'LN', 'series' : [99,14,15,16,17,18,] } ,  
                   { 'id':13, 'title': 'Velocidade do Vento',         'tipo': 'LN', 'series' : [99,14,] },
            ]
       
        for item in col: 
            series = item['series']
            eixo = []

            isGrafico = True

            for parametro in  series:
                key = parametro if parametro == 99 else parametro 
                linha = self.getEixo(key)
                
                if len(linha['serie']) > 0:
                    eixo.append( linha  )
                else:
                    isGrafico = False
                    break            

            if not isGrafico:
                continue


            titulo01 =  u'{0}'.format( eixo[1]['titulo'])
            hEixo   = ' {title: "(meses)", titleTextStyle: {color: "red"}} '
            vEixo   = ' {title: "' + titulo01  + '" , titleTextStyle: { color: "red"}} '
            title   =   item['title']  
            if item['id'] ==  2:
                legenda = ' { position : "top" } '
            else:
                legenda = ' { position : "none" } '

            grafico = { 'id'        : item['id'], 
                        'titulo'    : item['title'],
                        'element'   : 'elemento{0}'.format(item['id']),
                        'type'      : TipoGrafico().getBySigla(item['tipo']),
                        'data'      : self.geraDataTable(eixo), 
                        'vEixo'     : vEixo, 
                        'options'   : { 'title' : title, 'vAxis': vEixo, 'hAxis': hEixo, 'legenda':legenda },
                        'legenda'   : legenda,
                        'views'     : "( [ 0, 1, { type: 'string', role: 'annotation', sourceColumn: 1, calc: 'stringify' }] )"
                      }
            colGraficos.append(grafico)
        
        return colGraficos

