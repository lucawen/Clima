# -*- coding: utf-8 -*- 
#!/usr/bin/env python 

import django
from tools import PlanilhaExcel, ObjectView
from normais.models import Station
import json
from  automaticas import regras
from datetime import datetime 
import time
def imortAutomaticas():
    todas = Station.objects.filter(tipo= 'A')
    todas.delete()


    with open('/home/wbeirigo/Clima/weather/proj/scripts/Automaticas.json') as data_file:    
        data = json.load(data_file)

    for item in data:
    	r = ObjectView(item)

        estacao = Station.objects.filter(Codigo = r.codigo)
        if len(estacao) == 0:
            q = Station(tipo    = r.tipo,
        		    	Codigo  = r.codigo, 
        	            Nome    = r.Nome, 
                	    Estado  = r.Estado, 
        	            UF      = r.UF,
        	      		Altitude = r.Altitude, 
        			    posicao = 'SRID=4326;POINT({0} {1})'.format(r.longi, r.lati),
        	            LatLong = u'({0},{1})'.format(r.longi, r.lati)  
            		   )
            q.save()
        else:
            print estacao[0].Nome, r.Nome

def default(obj):

    """Default JSON serializer."""
    import calendar, datetime

    if isinstance(obj, datetime.datetime):
        if obj.utcoffset() is not None:
            obj = obj - obj.utcoffset()
    millis = int(
        calendar.timegm(obj.timetuple()) * 1000 +
        obj.microsecond / 1000
    )
    return millis

def run():

    objMedicao = regras.Medicao()

    key = '86865'
    objMedicao.graficos(key)


"""
http://jsfiddle.net/w172sc4t/2/
"""


