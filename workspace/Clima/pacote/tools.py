# !-*- conding: utf8 -*-
#!/usr/bin/env python2.5
from datetime import datetime
from os import listdir
from os.path import isfile, join
import urllib2, re, codecs, json


__script_name__ = "Tools.py"
__author__ = "Wilson Beirigo Duarte"
__maintainer__ = "Wilson Beirigo Duarte"
__version__ = "0.1"


class Tools:

    @staticmethod
    def leituraUrl(caminho, objProxy):
        """ Realiza a leitura de uma pagina e retorna como string
                :param str  : url da pagina            
                :returns: string contendo os dados da pagina            
        """        

        #proxy = urllib2.ProxyHandler(objProxy.getProxyRequests('http'))
        # opener = urllib2.build_opener(proxy)
        opener = urllib2.build_opener()
        urllib2.install_opener(opener)

        req = urllib2.Request(url=caminho)        
        f = urllib2.urlopen(req)
        saida = f.read()
        opener.close()
        
        return saida

    @staticmethod
    def ExtraiCampo(valor, regra):
        """ Extrai uma string do parametro "valor" a partir da expressao regular "regra"
                :param str  : valor string contendo a string a ser extraida
                :param str  : regra srtring contendo a expressao regular
                :returns: string contendo o valor filtrado pela expressao regular
        """
        try:
            padrao = re.compile(regra)
            saida = padrao.findall(valor)           
        except:
            print 'Erro ao extrair a regra.'
            raise
    
        return saida

    @staticmethod
    def ExtraiCampos(valor, regras):   
        """ Processa a extracao de campos da string "valor" utilizando as regras definidaz em "regras"
                :param str  : valor string contendo a string a ser extraida
                :param dict[campo] = regra  : Dicionario contendo as expressoes regulares e o nome dos campos
                :returns: campos contendo dicionario 
        """
        campos = {}
        for key in regras:
            try:
                regra = regras[key]            
                value = Tools.ExtraiCampo(valor, regra)[0]
                campos[key] = value
            except:
                raise               
        return campos


    @staticmethod
    def ObjectToDict(dados):
        lista = {}
        i = 0
        for item in dados:
            lista[i] = dados[item].__dict__
            i += 1
        return lista


    @staticmethod
    def GravaJson(arquivoJsonSaida, dados):
        """ Grava em disco rigido no endereco "arquivoJsonSaida" os dados da estrutura "dados"
                :param str  : caminho do arquivo a ser gravado
                :param  = dados a serem persistidos             
        """
        
        lista = Tools.ObjectToDict(dados)
               
        with open(arquivoJsonSaida, "wb") as arquivo:                        
            arquivo.write(json.dumps(lista))
            arquivo.close()


    @staticmethod
    def LoadJson(arquivo):
        """ Carrega em memoria o arquivo "arquivo"
                :param str  : caminho do arquivo a ser gravado
                :returns: dados carregados em memoria
        """            
        with codecs.open(arquivo, "r", 'utf-8') as myfile:
            json = myfile.read().replace('\n', '')
            dados = json.loads(json)
        return dados


    @staticmethod
    def tryFloat(val):
        ret = 0
        try:
            ret = float(val)
        except:
            ret = 0
        return ret

    @staticmethod
    def tryInt(val):
        ret = 0
        try:
            ret = int(val)
        except:
            ret = 0
        return ret

    @staticmethod
    def tryMDY(val):
        dt = None
        try:
            dt = datetime.strptime(val, '%d/%m/%Y').strftime('%Y-%m-%d')
        except:
            dt = datetime.strptime('01/01/1901', '%d/%m/%Y').strftime('%Y-%m-%d')
        return dt

    
    @staticmethod
    def LerArquivosDiretorio(path, extencao):
        return  [ f for f in listdir(path) if isfile(join(path,f)) and f[-5:] == extencao  ]
    
    @staticmethod
    def ExtraiStringArquivo(arquivo):
            f = open(arquivo, 'r')
            dados = f.read()
            dados = json.loads(dados)    
            f.close()
            return dados
    
    @staticmethod
    def gravaArquivo(arquivo, dados):                                
            f = open(arquivo , 'w')            
            f.write(dados)
            f.close
    
    