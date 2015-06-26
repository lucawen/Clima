#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests import Request, Session
import lxml.html
from lxml import cssselect
import re
import logging
from datetime import datetime
import json

from pacote.tools import Tools
from pacote.modelos import Estacao, DadosEstacao
import psycopg2  

__author__ = "Wilson Beirigo Duarte"
__maintainer__ = "Wilson Beirigo Duarte"
__version__ = "0.1"
__script_name__ = "estacao.py"
        
                               
class ImportaDadosEstacao:
    
    HEADER = {'content-type': 'application/json', 'Accept-Language': 'pt-BR'}
    MAX_INTERACOES = 10 
    
    def __init__(self):
        self.colecao = []
        self.inter = 0
        self.inicio = datetime.now()
        self.fim = datetime.now()
        self.segundos = 0
        self.registros = 0
        self.logging  = None

    def __decrypt(self, chave):
        """ Decifra o codigo passado no formulario
        """

        milhar = {'MD':0, 'MT':1, 'Mj': 2, 'Mz':3, 'ND':4 }
        centena = {'Y':6, 'c':7, 'g': 2, 'k':3 }
        dezena = {'w':0, 'x':1, 'y': 2, 'z':3, '0':4 }
        unidade = {'Ng':6, 'Nw':7, 'OA': 8, 'OQ':9 }

        try:
            nMil = chave[:2] 
            nCent = chave[2]
            nDez = chave[3]
            nUnid = chave[4:]

            resp = '{0}{1}{2}{3}'.format(milhar[nMil], centena[nCent], dezena[nDez], unidade[nUnid])
        except:
            print chave
            self.logging.error('Erro ao decodficar Captcha:{0}'.format(chave))   
            
            
        
        return resp
    
    def __Scrap1(self, codEstacao, sessao):
                      
        URL = 'http://www.inmet.gov.br/sonabra/pg_dspDadosCodigo.php?{0}=='
                        
        resposta = ''
        try:
            url = URL.format(codEstacao)
            req = Request('GET', url)           
            entrada = sessao.prepare_request(req)            
            resp = sessao.send(entrada)
            padrao = re.compile(r'<input type="hidden" name="aleaValue" value="(\w{6})==">')            
            chave = padrao.findall(resp.text)
            resposta = chave[0]
        except:
            self.logging.error(('Falhou pesquisa UM ItemEstacao:{0}'.format(codEstacao)))            
            raise
                                                       
        return resposta
    
    def __Scrap2(self, codEstacao, param, sessao):
          
        URL = 'http://www.inmet.gov.br/sonabra/pg_dspDadosCodigo.php?{0}=='          
        try:            
            saida = ''
            urlpost = URL.format(codEstacao)      
            req = Request('POST', urlpost, data=param, headers=sessao.headers)
            entrada = sessao.prepare_request(req)
            resp = sessao.send(entrada)            
            saida = lxml.html.fromstring(resp.text)
        except:
            self.logging.error('Falhou pesquisa DOIS ItemEstacao:{0} Parametro:{1}'.format(codEstacao, param))            
            raise                         
    
        return saida
      
    def __Scrap3(self, html):
        
        tabela = []
        rows = []         
        try:
            rows = html.cssselect("tr")           
        except:
            self.logging.error('Erro CSSSELCT:{0} '.format(str(html)))
            raise
        
        tbl = []
        for row in rows:
            tbl.append(list())
            for td in row.cssselect("td"):
                tbl[-1].append(unicode(td.text_content()))

        if len(tbl) > 8:
            tabela = tbl[8:]
        
        return tabela            
    
    def __Scrap(self, codEstacao, strtInicio, strtFim):
                        
        sessao = Session()
        self.inter = 0
        while True:              
            self.inter += 1
            tabela = []
            try:            
                captcha = self.__Scrap1(codEstacao, sessao)        
                resposta = self.__decrypt(captcha)
                param = { 'aleaNum':resposta, 'aleaValue': captcha, 'dtafim':strtFim,  'dtaini': strtInicio}
                texto = self.__Scrap2(codEstacao, param, sessao)
                tabela = self.__Scrap3(texto)
            except:
                pass
            if len(tabela)>0 or self.inter > self.MAX_INTERACOES:                
                break                
            
        sessao.close()
                    
        if len(tabela) > 0:
            for reg in tabela:
                registro = DadosEstacao()     
                registro.FromLinha(reg, codEstacao)
                self.colecao.append(registro.__dict__)                 
        else:
            msg  = 'Falhou pesquisa estação {}'.format(codEstacao)
            print(msg)
            self.logging.info(msg)
                        
        
    def __GravaLog(self, codEstacao):
        self.fim = datetime.now()
        uptime = self.fim - self.inicio
        self.segundos = uptime.__str__()         
        self.registros = len(self.colecao)                        
        STRING_LOG = 'Estação:{0}    Inicio:{1}    Fim:{2}    Tentativas:{3}    Tempo:{4}    QtdRegistros{5}'
        strSaida = STRING_LOG.format(codEstacao, self.inicio, self.fim, self.inter, self.segundos, self.registros)            
        self.logging.info(strSaida)
        self.colecao = []
        self.inicio = datetime.now()
        self.fim = datetime.now()
        self.segundos = 0
        self.registros = 0

                
    def ProcessaImportacao(self, nome_arquivo, qtdRegistros, inicio, fim, estacoes, logging):
        
        self.logging = logging
                
        inter = 0
        col = []
        i = 0
        for codEstacao in estacoes:
            print "{0}/{1}".format(i, len(estacoes))
            self.__Scrap(codEstacao, inicio, fim)
            col.extend(self.colecao)            
            self.__GravaLog(codEstacao)
            i+=1
            
            if (len(col) > qtdRegistros):
                dados = json.dumps(col)
                arquivo = nome_arquivo.format(inter)
                Tools.gravaArquivo(arquivo, dados)
                col = []
                inter += 1
            
        dados = json.dumps(col)
        arquivo = nome_arquivo.format(inter)
        Tools.gravaArquivo(arquivo, dados)
        col = []
        inter += 1






        
        arquivo = NOME_ARQUIVO.format(inter)
        Tools.gravaArquivo(arquivo, dados)

        
if __name__ == "__main__":
            
    ARQUIVO_LOG = 'C:/tv/Clima/workspace/bases/importadados.log'
    NOME_ARQUIVO = 'C:/tv/Clima/workspace/bases/saida{0}.json'
    QTD_REGISTROS_GRAVAR = 50000
    STRING_CONEXAO = "dbname='Terravision' user='postgres' host='localhost' password='wilci5w7'"
    path='C:/tv/Clima/workspace/bases/'    
    inicio = '30/03/2015'
    fim = '06/04/2015'
        
    logging.basicConfig(filename=ARQUIVO_LOG,level=logging.DEBUG)
    logging.info("Inicio." + datetime.now().strftime("%B %d,:%Y %H:%M:%S "))    
        
    db = psycopg2.connect(STRING_CONEXAO) 
                
    objEstacao = Estacao()
    estacoes = objEstacao.getEstacoes(db)
    del objEstacao
    
    ImportaDadosEstacao().ProcessaImportacao(NOME_ARQUIVO, QTD_REGISTROS_GRAVAR, inicio, fim, estacoes, logging)
       
    objDadadosEstacao = DadosEstacao()    
    objDadadosEstacao.InsereDB(db, path)
    
    del db    
        
    logging.info("FIM." + datetime.now().strftime("%B %d,:%Y %H:%M:%S "))
        
    print('Fim')
