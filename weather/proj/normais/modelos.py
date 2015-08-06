# -*- coding: utf-8 -*- 
#!/usr/bin/env python

class ChartsTypes():

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


