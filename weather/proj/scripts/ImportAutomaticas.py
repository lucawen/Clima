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

    colAutomaticas = regras.Estacao()

    objMedicao = regras.Medicao()

    key = '81996'
    dados_temp = dados_umi = dados_po = dados_pres   = []
    dados_rad =  dados_pre =  dados_vdd = dados_vvel = []

    objDados = objMedicao.getMedicaoDiaria(key)
    for item in objDados:
        dt = item['data']
        dt  = long(time.mktime(dt.timetuple()))
#       seconds += (dt.microsecond / 1000000.0)
    
 
        dados_temp.append(    [ dt, item['tempmed'] ])
        dados_umi.append(     [ dt, item['umidmed']])
        dados_po.append(      [ dt, item['pomed'] ])
        dados_pres.append(    [ dt, item['pmed']  ])
        dados_rad.append(     [ dt, item['radiacao']])
        dados_pre.append(     [ dt, 0])
        dados_vdd.append(     [ dt, 0])
        dados_vvel.append(    [ dt, item['vvelmed']])
        
        saida = {
                    'dados_temp' :  dados_temp,
                    'dados_umi'  :  dados_umi,
                    'dados_po '  :  dados_po,
                    'dados_pres' :  dados_pres,
                    'dados_rad'  :  dados_rad,
                    'dados_pre'  :  dados_pre,
                    'dados_vdd'  :  dados_vdd,
                    'dados_vvel' :  dados_vvel
                }

        response = json.dumps(saida)

        print response

    return response  





"""
http://jsfiddle.net/w172sc4t/2/
"""


