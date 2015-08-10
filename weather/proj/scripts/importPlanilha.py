# -*- coding: utf-8 -*-
#!/usr/bin/env python

import django
from tools import PlanilhaExcel, ObjectView
from normais.models import Parametro, Classe, Resultado, Station, ResultStr
import datetime

def run():

    todos = Resultado.objects.all()
    #   todos.delete()

    exc  = PlanilhaExcel()
    """
    arquivos = Parametro.objects.all()
    for arq in arquivos:


        if arq.codigo == 19:
            continue

        print arq.id, arq.Nome, datetime.datetime.now().time().isoformat()

        rowInic = 4
        if  arq.Nome == u'Máx. Absoluto Prec. Acum. - 24 Hs'  or  \
            arq.Nome == u'Temp. Máx. Absoluta (ºC)' or  \
            arq.Nome == u'Temp. Mín. Absoluta (ºC)': 
            rowInic = 6

    
        if arq.Nome == u'Direção Predominante do Vento' or \
           arq.Nome == u'Direção Resultante do Vento' or \
           arq.Nome == u'Componente Meridional do Vento' or \
           arq.Nome == u'Componente Zonal do Vento' or \
           arq.Nome == u'Intensidade e Direção do Vento a 10 (m.s-1)':
            rowInic = 5


        if arq.Nome == u'Direção Predominante do Vento' or \
           arq.Nome == u'Direção Resultante do Vento':
            tipo = 'C'
        else:
            tipo = 'N'


        arquivo = '/home/wbeirigo/Clima/dados/{0}'.format(arq.Planilha)

        cp = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'stb', 'out', 'nov', 'dez', 'tot']
        pos = [ arq.jan, arq.fev, arq.mar, arq.abr, arq.mai, arq.jun, arq.jul, arq.ago, arq.stb, arq.out, arq.nov, arq.dez, arq.tot]

        campos = []
        campos.append(['codigo', 'C', 0])
        indice = 0
        for it in cp:
            campos.append([ cp[indice], tipo, pos[indice] ] )
            indice += 1

        plan = {'planilha': arquivo, 'campos':campos, 'key':'codigo',  'rowInic': rowInic  } 
        col = exc.leituraPlanilha(plan)



        for reg in col:

    	    r = ObjectView(col[reg])

            codstac = r.codigo.replace('*','')
    
            if codstac == '':
                print codstac, reg 
                continue

            try:
                station = Station.objects.get(Codigo =  codstac)
            except:
                print 'Nao achou estação', codstac  
                continue


            parametro = Parametro.objects.get(Nome = arq.Nome)


            if arq.Nome == u'Direção Predominante do Vento' or \
               arq.Nome == u'Direção Resultante do Vento':
                result = ResultStr(     Station_FK = station, Parametro_FK = parametro,
                                        jan = r.jan, fev=r.fev, mar = r.mar,
                                        abr = r.abr, mai=r.mai, jun = r.jun,
                                        jul = r.jul, ago=r.ago, stb = r.stb,
                                        out = r.out, nov=r.nov, dez = r.dez,
                                        tot = r.tot )                                        
            else:

                result = Resultado(     Station_FK = station, Parametro_FK = parametro,
                                        jan = r.jan, fev=r.fev, mar = r.mar,
                                        abr = r.abr, mai=r.mai, jun = r.jun,
                                        jul = r.jul, ago=r.ago, stb = r.stb,
                                        out = r.out, nov=r.nov, dez = r.dez,
                                        tot = r.tot )                                        
            
            result.save()
    """

    todos = Resultado.objects.filter(Parametro_FK__codigo=19)
    todos.delete()
    for reg in Station.objects.all():

        param19 = Parametro.objects.get(codigo=19)
        ccol8 = Resultado.objects.filter(Parametro_FK__codigo = 8, Station_FK__id = reg.id)
        ccol9 = Resultado.objects.filter(Parametro_FK__codigo = 9, Station_FK__id = reg.id)
        if len(ccol8) > 0 and len(ccol9) > 0:
            col8 = ccol8[0]
            col9 = ccol9[0]


            result = Resultado( Station_FK = reg, Parametro_FK = param19,
                                jan =   (col9.jan - col8.jan), 
                                fev=    (col9.fev - col8.fev), 
                                mar =   (col9.mar - col8.mar), 
                                abr =   (col9.abr - col8.abr), 
                                mai=    (col9.mai - col8.mai), 
                                jun =   (col9.jun - col8.jun), 
                                jul =   (col9.jul - col8.jul), 
                                ago=    (col9.ago - col8.ago), 
                                stb =   (col9.stb - col8.stb), 
                                out =   (col9.out - col8.out), 
                                nov=    (col9.nov - col8.nov), 
                                dez =   (col9.dez - col8.dez), 
                                tot =   (col9.tot - col8.tot),  )                                        
            
            result.save()

