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

    def __init__(self):

        self.colecao = []

        try:
            connstring = HOST_CLIMA
            self.db  = psycopg2.connect(connstring)
        except:
             raise

    def getCodigoByOMM(self, omm):

        saida = ''
        try:
            sql = """
SELECT codigo
FROM "Clima_estacoes"
WHERE omm = '{0}'
            """.format(omm)
            cursor = self.db.cursor()
            cursor.execute(sql)
            saida = cursor.fetchone()
        except:
            raise

        return saida[0].encode('ascii')


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

    def criaResultado(self,values):

        labels = 'fmaANT;fmapANT;data;diaschuva;precipt;\
                    fma;velVento;calcVelVento;fmap;restricao;\
                    horaUmid;umid;umidCalc;fma;fmac'.split(';')

        linha = {}
        for item in range(len(labels)):
            if type(values[item]) == float:
                values[item] = round(values[item], FLOAT_ROUD_PLACES)
            linha[labels[item]] = values[item] 
      
        self.colecao.append(Struct(linha))
 


    def formula(self, codigo, dataBase=datetime.now()):

        
        wmoAutomatica = self.getCodigoByOMM(codigo)

        data = self.getDiasSemChuva(wmoAutomatica, MM_CHUVA,dataBase)[0] 

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
                                            HORA_MEDICAO):
            medicoes.append(item)

        for item in self.getPrecitacao(wmoAutomatica, \
                                            dataStr, 
                                            dataBase):
            precipit.append(item[1])


        if len(medicoes) + 1 ==  len(precipit):
            obj = self.getHistorico(wmoAutomatica,\
                                            dataStr, \
                                            dataBase)   
            medicoes.append(obj[0])


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
                      str(self.Resultado(fma)),
                      str(self.Resultado(fma)),
                   ]
            self.criaResultado(values)
           
            indice += 1

        return  self.colecao


def run():
    codigo = '86821'
    dataBase = datetime(2015,1,1)

    objMail = Email()
    objMail.EnviaMSG('Testes', 
                    'Este e um teste de msg',
                    ['wbeirigo@gmail.com',
                     'wilson@solvecorp.com.br', 
                     'wbeirigo@terravisiongeo.com.br', ]
                     )
    quit()

    objFMA = FMA()
    colecao = objFMA.formula(codigo)
    for i in  colecao:
        print  i.fmap








