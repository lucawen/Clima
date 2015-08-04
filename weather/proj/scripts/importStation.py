# -*- coding: utf-8 -*-
#!/usr/bin/env python

import django
from tools import PlanilhaExcel, ObjectView
from normais.models import Station

def run():

    exc  = PlanilhaExcel()


    campos = [
                ['Codigo',   'C', 0],
                ['Nome',     'C', 1],
                ['Estado',  'C', 2], 
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

    plan = {'planilha': '/home/wbeirigo/Clima/dados/Relac_Est_Meteo_NC.xls', 'campos':campos, 'key':'Codigo', 'aba':'Plan1' } 
    col = exc.leituraPlanilha(plan)


    todasEstacoes = Station.objects.all()
    todasEstacoes.delete()

    for reg in col:
    	r = ObjectView(col[reg])
    	q = Station(Codigo = r.Codigo, Nome=r.Nome, Estado = r.Estado, UF=r.UF,
    		Altitude = r.Altitude, Tmed=r.Tmed, Tmax = r.Tmax, 
    		Tmin = r.Tmin, TmaxAbs = r.TmaxAbs, TminAbs=r.TminAbs, 
    		Pres = r.Pres, Inso = r.Inso, Evap = r.Evap, Neb = r.Neb, 
    		NebHora = r.NebHora, UR = r.UR, URHora = r.URHora, 
	    	Prec = r.Prec, PrecMax = r.PrecMax, PrecNDias = r.PrecNDias,
    		PDec = r.PDec, PdecND = r.PdecND, NPSec = r.NPSec, 
    		VentoInt = r.VentoInt, Ventou = r.Ventou, Ventov = r.Ventov,
    		VentoDirRes = r.VentoDirRes, VentoDirPred = r.VentoDirPred,
    		NNormais = r.NNormais, LatLong = u'({0},{1})'.format(r.Latitude, r.Longitude)  )
    	q.save()

