# -*- coding: utf-8 -*-
#!/usr/bin/env python

import django
from tools import PlanilhaExcel, ObjectView
from normais.models import Parametro, Classe

def run():

    exc  = PlanilhaExcel()


    campos = [
                ['ID',   'C', 0],
                ['Classe',   'C', 1],
                ['Arquivo',   'C', 2],
                ['Nome',     'C', 3],
                ['LinhaTitulo',  'C', 4], 
                ['ColEstacao',   'N', 5],      
                ['jan', 'N', 6], 
                ['fev', 'N', 7], 
                ['mar', 'N', 8], 
                ['abr', 'N', 9], 
                ['mai', 'N',10], 
                ['jun', 'N',11], 
                ['jul', 'N', 12], 
                ['ago', 'N', 13], 
                ['stb', 'N', 14], 
                ['out', 'N', 15], 
                ['nov', 'N', 16], 
                ['dez', 'N', 17], 
                ['tot', 'N', 18], 
    ]

    plan = {'planilha': '/home/wbeirigo/Clima/dados/Planilha.xls', 'campos':campos, 'key':'ID', 'aba':'Folha1', 'rowInic':3  } 
    col = exc.leituraPlanilha(plan)

    todas= Parametro.objects.all()
    todas.delete()

    for reg in col:
    	r = ObjectView(col[reg])

        try:
            vr = Classe.objects.get(Nome = r.Nome)
        except Classe.DoesNotExist:
            vr = Classe(Nome = r.Classe)
            vr.save()


        if r.ID != 99:
            q = Parametro(  Nome = r.Nome, Classe_FK = vr, 
                            Planilha = r.Arquivo,
                            jan = r.jan, fev = r.fev, mar = r.mar,
                            abr = r.abr, mai = r.mai, jun = r.jun,
                            jul = r.jul, ago = r.ago, stb = r.stb,
                            out = r.out, nov = r.nov, dez = r.dez,
                            tot = r.tot) 
    	    q.save()

