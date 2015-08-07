# -*- coding: utf-8 -*-
#!/usr/bin/env python

import django
from normais.models import Parametro, Classe, Resultado

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
        self.eixos = []


    def getEixo(self, idSerie):

        print idSerie

        if idSerie == 99:
            titulo = '(meses)'
            serie = ['meses', 'jan','fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago','stb', 'out', 'nov', 'dez']
        else:
            reg = Parametro.objects.get(pk = idSerie)

            titulo = '({0})'.format(reg.unidade)
            result = Resultado.objects.get(Station_FK__id == self.idStation, Parametro_FK__id == idSerie).__dict__ 
            serie = []
            serie.append('vlr')
            for mes in self.meses():
                serie.append(result[mes])

        saida = { 'titulo' : titulo, 'serie' : serie } 

        return saida 


    def geraDataTable(self):
        return "TESS"


    def getGrafico(self):

        colGraficos = []
        col = [    { 'id': 1, 'title': 'Precipitação Acumulada',      'tipo': 'CL', 'series' : [11,] } ,  
                   { 'id': 2, 'title': 'Temperaturas',                'tipo': 'LN', 'series' : [1,2,3,] } ,  
                   { 'id': 3, 'title': 'Precipitação Máxima 24h',     'tipo': 'CL', 'series' : [12,] } ,  
                   { 'id': 4, 'title': 'Temperatura Mínima Absoluta', 'tipo': 'LN', 'series' : [4,] } ,  
                   { 'id': 5, 'title': 'Temperatura Máxima Absoluta', 'tipo': 'LN', 'series' : [5,] } , 
                   { 'id': 6, 'title': 'Deficit e Superávit Hídrico', 'tipo': 'LN', 'series' : [8,11,] } ,  
                   { 'id': 7, 'title': 'Umidade Relativa',            'tipo': 'CL', 'series' : [10,] } ,  
                   { 'id': 8, 'title': 'Nebulosidade',                'tipo': 'LN', 'series' : [9,] } ,  
                   { 'id': 9, 'title': 'Pressão',                     'tipo': 'LN', 'series' : [6,] },  
                   { 'id':10, 'title': 'Insolação',                   'tipo': 'CLN','series' : [7,] } ,  
                   { 'id':11, 'title': 'Dias sem Chuva',              'tipo': 'CL', 'series' : [13,] } ,  
                   { 'id':12, 'title': 'Direção Predominante do Vento', 'tipo': 'LN', 'series' : [14,15,16,17,18,] } ,  
                   { 'id':13, 'title': 'Velocidade do Vento',         'tipo': 'LN', 'series' : [14,] } ,  ]
       
        for item in col: 
            item['series'].insert[99,0]
        
            for parametro in item['series']:
                self.eixos.append( self.getEixo(parametro) )


            grafico = { 'DataTable' : self.geraDataTable(), 
                        'Options'   : 'var chart_options{0} = { title: {1} };'.format(item.id,  item.title), 
                        'chart'     : 'var chart{0} = new {1}(document.getElementById("chart_name{0}")); '.format( item.id,  TipoGrafico().getBySigla(item) )

                      }
            colGraficos.append(grafico)


        return colGraficos


def run():
    teste = NormalGraficos(14).getGrafico()
