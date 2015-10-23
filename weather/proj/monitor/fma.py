# -*- coding: utf-8 -*-
#!/usr/bin/env python

import django
import psycopg2
from   datetime import datetime, timedelta
import math
from toolbox.tools import  Struct
from toolbox.maillib import Email


HOST_CLIMA   = "host='10.3.0.26' \
                dbname='clima'\
                user='postgres'\
                password='wilci5w7'"

MM_CHUVA     = 13
HORA_MEDICAO = 13 + 3 # 13 + UTC
K_FMA        = float(100)
LN_E         = float(2.718282)
K_VENTO      = float(0.04)
FLOAT_ROUD_PLACES = 4


class FMA:


    def __conn(self):
        try:
            connstring = HOST_CLIMA
            db  = psycopg2.connect(connstring)
            return db
        except:
             raise



    def __init__(self):

        self.colecao = []


    def getCodigoByOMM(self, omm, db):

        saida = ''
        try:
            sql = """
SELECT codigo
FROM "Clima_estacoes"
WHERE omm = '{0}'
            """.format(omm)
            cursor = db.cursor()
            cursor.execute(sql)
            saida = cursor.fetchone()
        except:
            raise

        return saida[0].encode('ascii')


    def getDiasSemChuva(self, codigo, mmChuva, dataBase, db):
        
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

            cursor = db.cursor()
            cursor.execute(sql)
            saida = cursor.fetchone()
        except:
            raise


        return saida

    def getPrecitacao(self, codigo, data, dataFim, db):
        
        saida = None
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
            cursor = db.cursor()
            cursor.execute(sql)
            saida = cursor.fetchall()
        except:
            raise

        return saida



    def getHistorico(self, codigo, data, dataBase,db, hora=99):
        
        saida = ''
        try:
            if hora == 99:
                sql = """ 
SELECT "Data","UmidInst", "VentVel", "VentDir", "TempInst", "PressInst",
        "Hora", id 
FROM "Clima_dadosestacao" 
WHERE "codEstac"=\'{0}\' and
       "Data" = \'{1}\' 
ORDER BY "Hora" DESC LIMIT 1 """.format(codigo, dataBase )
            else:
                sql = """
SELECT "Data","UmidInst", "VentVel", "VentDir", "TempInst", "PressInst", 
        "Hora" , id
FROM   "Clima_dadosestacao" 
WHERE  "codEstac"=\'{0}\' and 
       "Data" >= \'{1}\' and 
       "Data" <= \'{2}\' and 
       "Hora"={3} 
ORDER BY "Data" """.format(codigo, data, dataBase, hora)

            cursor = db.cursor()
            cursor.execute(sql)
            saida = cursor.fetchall()
        except:
            raise

        return saida



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
        tabela = [ [    0,   1.09, u'Nulo',      '#AA3939'],
                   [  3.1,   8.09, u'Medio',     '#2D882D'], 
                   [  8.1,  20.09, u'Alto',      '#AA6C39'], 
                   [ 20.1,9999.09, u'Muito Alto','#AA3939'], 
                ]
        saida = (0,0) 
        for faixa in tabela:
            if indice >= faixa[0] and indice <= faixa[1]:
                saida = ( faixa[2], faixa[3] )
                break

        if saida == "":
            raise ValueError('Erro no resultado da FMA.')

        return saida

    def criaResultado(self,values):

        labels = 'fmaANT;fmapANT;data;diaschuva;precipt;\
                    fma;velVento;calcVelVento;fmap;restricao;\
                    horaUmid;umid;umidCalc;lblfma;lblfmap;colorfma;colorfmap'.split(';')

        linha = {}
        for item in range(len(labels)):
            if type(values[item]) == float:
                values[item] = round(values[item], FLOAT_ROUD_PLACES)
            linha[labels[item].strip()] = values[item] 
      
        self.colecao.append(Struct(linha))
 


    def formula(self, codigo, dataBase=datetime.today().date()):


        objDB =self. __conn()

        wmoAutomatica = self.getCodigoByOMM(codigo, objDB)

        data = self.getDiasSemChuva(wmoAutomatica, MM_CHUVA,dataBase, objDB)[0] 

        # O sistema retorna o dia em que ocorreu a chuva       
        # temos que remover um dia
        data += timedelta(days=1)

        dataStr =  data.strftime('%d/%m/%Y') 

        medicoes = []
        precipit = []

        indice = 0
        for item in self.getHistorico(wmoAutomatica,\
                                            dataStr, \
                                            dataBase,
                                            objDB,\
                                            HORA_MEDICAO):
            medicoes.append(item)

        
        if len(medicoes) + 1 ==  len(precipit):
            obj = self.getHistorico(wmoAutomatica,\
                                    dataStr, \
                                    dataBase,\
                                    objDB)
            medicoes.append(obj[0])

        for item in self.getPrecitacao(wmoAutomatica, \
                                            dataStr, 
                                            dataBase,\
                                            objDB):
            precipit.append(item[1])


        del objDB

        fmap = float(0)
        fma = float(0)

        colecao = []
        for item in medicoes:

            fmaAnt = fma
            fmaPAnt = fmap

            data = item[0]
            umidade = float(item[1])
            velVento = float(item[2])
            mmPrecipt = precipit[indice]

            if fma > 0:
                restricao = self.RestricoesChuva(mmPrecipt, MM_CHUVA )
            else:
                restricao = 1

            horaUmid = item[6]

            calcItem = float(K_FMA/ umidade  )
            fma = (fma * restricao)  + calcItem 

            calcVelVento  = K_VENTO * velVento  
            calcItemFMAP =  math.pow(LN_E, calcVelVento) 
            fmap += calcItemFMAP

            lblfma, colorfma     = self.Resultado(fma)
            lblfmap, colorfmap   = self.Resultado(fmap)

            values =[ fmaAnt,
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
                      lblfma,
                      lblfmap,
                      colorfma,
                      colorfmap
                   ]
            self.criaResultado(values)
           
            indice += 1


        return  self.colecao

"""
def run():
    codigo = '86821'
    dataBase = datetime(2015,1,1)

    objFMA = FMA()
    colecao = objFMA.formula(codigo)
    for i in  colecao:
        print  i.fmap
"""







