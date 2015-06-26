#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import re
import lxml.html
import lxml.cssselect
import psycopg2  
from decimal import Decimal

class ItemEstacao:

    def dictToObject(self, _dados):
        self.sigla = _dados['sigla'] 
        self.codigo = _dados['codigo'] 
        self.aberta = _dados['aberta'] 
        self.latitude =_dados['latitude'] 
        self.longitude = _dados['longitude'] 
        self.altitude = Decimal( _dados['altitude'].replace(',','.')) 
       
    @staticmethod
    def getRegras():
        expressao = {}
        expressao['sigla'] =  '<b><b>Estação:</b> (.*?)<br>'.decode('utf-8')
        expressao['codigo'] =  r'<a href=http://www.inmet.gov.br/sonabra/pg_dspDadosCodigo.php.(.*?)== target=_new>' 
        expressao['aberta'] =  r'</table>Aberta em: (.*?)<br>'
        expressao['latitude'] =  r'<br>Latitude: (.*?)º<br>'.decode('utf-8')
        expressao['longitude'] =  r'<br>Longitude: (.*?)º<br>'.decode('utf-8')
        expressao['altitude'] =  r'<br>Altitude: (.*?) metros</font><\\/div>' 
        return expressao

    def InsereDB(self, db):         
        try:   
            cursor = db.cursor()        
            try:              
                ponto = '[{0},{1}]'.format(self.latitude, self.longitude)
                sql = 'INSERT INTO  "Clima_estacoes"(codigo, sigla, altitude, ponto, data_abertura)  VALUES (%s, %s, %s, %s, %s);'
                dados = ( self.codigo, self.sigla, self.altitude, ponto, self.aberta )
                cursor.execute(sql, dados)            
                db.commit()
            except psycopg2.IntegrityError:
                db.rollback()
            else:
                db.commit()    
        except:
            raise

class ImportaEstacao:
    
    URL = 'http://www.inmet.gov.br/sonabra/maps/pg_mapa.php'
    REGRA = r"var html = '(.*?)';" 

    def leituraUrl(self, caminho):
        req = urllib2.Request(url=caminho)
        f = urllib2.urlopen(req)
        return f.read()
        
    def ExtraiCampo(self, valor, regra):
        try:   
            padrao = re.compile(regra)
            saida = padrao.findall(valor)           
        except:
            print 'Erro ao extrair a regra.'
            raise
        
        return saida
    
    def ExtraiCampos(self, valor, regras):   
        campos = {}
        for key in regras:
            regra = regras[key]            
            value = self.ExtraiCampo(valor, regra)
            campos[key] = value[0]
        return campos
    
    def processa(self):    
        pagina = self.leituraUrl(self.URL)            
        html = lxml.html.fromstring(pagina)
        saida = html.cssselect('script')                            
        linhas = self.ExtraiCampo(saida[1].text, self.REGRA)
                
        regrasCampos = ItemEstacao.getRegras()
        for linha in linhas:
            registro = self.ExtraiCampos(linha, regrasCampos)  
            objEstacao = ItemEstacao()          
            objEstacao.dictToObject(registro)                                
            objEstacao.InsereDB(db)            



if __name__ == "__main__":
    
    STRING_CONEXAO = "dbname='Terravision' user='postgres' host='localhost' password='wilci5w7'"
    db = psycopg2.connect(STRING_CONEXAO) 
    obj = ImportaEstacao()
    obj.processa()

