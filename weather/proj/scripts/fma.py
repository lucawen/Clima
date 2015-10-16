# -*- coding: utf-8 -*-
#!/usr/bin/env python

import django
import psycopg2
from   datetime import datetime, timedelta
import math

class Estacao:

    def __init__(self):
        try:
            connstring =\
            "host='10.3.0.26' dbname='clima' user='postgres' password='wilci5w7'"
            self.db  = psycopg2.connect(connstring)
        except:
             raise

    def getDiasSemChuva(self, codigo, mmChuva, dataBase):
        
        saida = ''
        try:
            sql = """ 
SELECT  date_trunc(\'day\',"Data" + interval \'1h\' *
        ( CAST("Hora" AS integer) - 5) ),
        sum("Chuva") 
FROM "Clima_dadosestacao"
WHERE "codEstac"=\'{0}\' and "Data" <= \'{1}\' 
group by 
date_trunc(\'day\',"Data" + interval \'1h\' * 
( CAST("Hora" AS integer) - 5) )
having sum("Chuva") >= {2}\
order by 
date_trunc(\'day\',"Data" + interval \'1h\' * 
( CAST("Hora" AS integer) - 5) ) DESC 
LIMIT 1; """.format(codigo, dataBase.strftime('%d/%m/%Y'), mmChuva)

            cursor = self.db.cursor()
            cursor.execute(sql)
            saida = cursor.fetchone()
        except:
            raise


        return saida

    def getPrecitacao(self, codigo, data, dataFim):
        
        saida = ''
        try:
            sql = """
SELECT  
date_trunc(\'day\',"Data" + interval \'1h\' *
( CAST("Hora" AS integer) - 5) ), 
sum("Chuva") 
FROM    "Clima_dadosestacao" 
WHERE
"codEstac"=\'{0}\'  and 
date_trunc(\'day\',"Data" + interval \'1h\' *
        ( CAST("Hora" AS integer) - 5)) >= \'{1}\' and  
        "Data" <=  \'{2}\'  
GROUP BY date_trunc(\'day\',"Data" + interval \'1h\' *
         ( CAST("Hora" AS integer) - 5) ) \
ORDER BY date_trunc(\'day\',"Data" + interval \'1h\' *
        ( CAST("Hora" AS integer) - 5) )""".format(codigo, data, dataFim)
            cursor = self.db.cursor()
            cursor.execute(sql)
            saida = cursor.fetchall()
        except:
            raise

        return saida



    def getHistorico(self, codigo, data, dataBase, hora=99):
        
        saida = ''
        try:
            if hora == 99:
                sql = """ 
SELECT "Data","UmidInst", "VentVel", "VentDir", "TempInst", "PressInst",
        "Hora" 
FROM "Clima_dadosestacao" 
WHERE "codEstac"=\'{0}\' and
       "Data" = \'{1}\' 
ORDER BY "Hora" DESC LIMIT 1 """.format(codigo, dataBase )
            else:
                sql = """
SELECT "Data","UmidInst", "VentVel", "VentDir", "TempInst", "PressInst", 
        "Hora" 
FROM   "Clima_dadosestacao" 
WHERE  "codEstac"=\'{0}\' and 
       "Data" >= \'{1}\' and 
       "Data" <= \'{2}\' and 
       "Hora"={3} 
ORDER BY "Data" """.format(codigo, data, dataBase, hora)

            cursor = self.db.cursor()
            cursor.execute(sql)
            saida = cursor.fetchall()
        except:
            raise

        return saida

    def __del(self):
        self.db.close()


    def RestricoesChuva(self, mm, mmChuva):

        tabela = [ [ 0.00,  2.49, 1.00],\
                [ 2.50,  4.99, 0.30],\
                [ 5.00,  9.99, 0.60],\
                [10.00, mmChuva, 0.80],\
                ]
        
        saida = -99
        for faixa in tabela:
            if mm >= faixa[0] and mm <= faixa[1]:
                saida = faixa[2]
                break

        if saida == -99:
            raise ValueError('Valor errado "mm" em calculo de restricao fma.')

        return saida


    def Resultado(self, indice):
        tabela = [ [    0,   1.09, u'Nulo'],
                   [  1.1,   3.09, u'Pequeno'],
                   [  3.1,   8.09, u'Medio' ], 
                   [  8.1,  20.09, u'Alto'], 
                   [ 20.1,9999.09, u'Muito Alto'], 
                ]
        saida = "" 
        for faixa in tabela:
            if indice >= faixa[0] and indice <= faixa[1]:
                saida = faixa[2]
                break

        if saida == "":
            raise ValueError('Erro no resultado da FMA.')

        return saida



def formula(wmoAutomatica, dataBase=datetime.now()):

    MM_CHUVA     = 13
    HORA_MEDICAO = 13 + 3 # 13 + UTC
    K_FMA        = float(100)
    LN_E         = float(2.718282)
    K_VENTO      = float(0.04)

    objEstacao  = Estacao()
    data = objEstacao.getDiasSemChuva(wmoAutomatica, MM_CHUVA,dataBase)[0] 

    # O sistema retorna o dia em que ocorreu a chuva       
    # temos que remover um dia
    data += timedelta(days=1)

    dataStr =  data.strftime('%d/%m/%Y') 

    medicoes = []
    precipit = []

    for item in objEstacao.getHistorico(wmoAutomatica,\
                                        dataStr, \
                                        dataBase,
                                        HORA_MEDICAO):
       medicoes.append(item)

    for item in objEstacao.getPrecitacao(wmoAutomatica, \
                                         dataStr, 
                                         dataBase):
        precipit.append(item[1])


    if len(medicoes) + 1 ==  len(precipit):
        obj = objEstacao.getHistorico(wmoAutomatica,\
                                        dataStr, \
                                        dataBase)   
        medicoes.append(obj[0])


    fmap = float(0)
    fma = float(0)
    indice = 0
    print   'fma-ANT;fmap-ANT;data;diaschuva;precipt;\
            fma;velVento;calcVelVento;fmap;restricao;\
            horaUmid;umid;umidCalc;fma;fmac;'
    
    for item in medicoes:

        fmaAnt = fma
        fmaPAnt = fmap

        data = item[0]
        umidade = float(item[1])
        velVento = float(item[2])
        mmPrecipt = precipit[indice]

        if fma > 0:
            restricao = objEstacao.RestricoesChuva(mmPrecipt, MM_CHUVA )
        else:
            restricao = 1

        horaUmid = item[6]

        calcItem = float(K_FMA/ umidade  )
        fma = (fma * restricao)  + calcItem 

        calcVelVento  = K_VENTO * velVento  
        calcItemFMAP =  math.pow(LN_E, calcVelVento) 
        fmap += calcItemFMAP

        print '{0};{1};{2};{3};{4};{5};\
               {6};{7};{8};{9};{10};{11};\
               {12};{13};{14};{15}'.\
                format(
                    fmaAnt,
                    fmaPAnt,
                    data,
                    indice,
                    mmPrecipt,
                    fma,
                    velVento,
                    calcVelVento,
                    fmap,
                    restricao,
                    horaUmid,
                    umidade,
                    calcItem,
                    str(objEstacao.Resultado(fma)),
                    str(objEstacao.Resultado(fma)),
                    '-'
                    ).replace('.',',')
        indice += 1




def run():
    codigo = 'QTU1NQ'
    dataBase = datetime(2015,1,1)
    formula(codigo, dataBase)









