# -*- coding: utf-8 -*-
#!/usr/bin/env python

import django
import datetime
import xlrd
import chardet
from param.models import Unidade, Param
from projetos.models import Medicao, PtoMonit, Projeto, Campanha
from toolbox.tools import ObjectView, xlsDate_as_datetime
from projetos.regras import getCampanha
from toolbox.maillib import Email
from operator import itemgetter

PATH_ARQUIVO     = '/home/wbeirigo/Clima/dados/dadoslaborat/procmedicao.xls'
PATH_FERRAMENTA  = '/home/wbeirigo/Clima/dados/dadoslaborat/converte.xls'
ID_PROJETO       = 1


class ProcMedicao:

    def __init__(self):
        self.result = []
        self.erros = []
        self.processados = 0
        self.pontoConv = {}
        self.paramConv = {}
   

        self.__converte(0) # Pontos
        self.__converte(1) # Parametros

        self.__procExcel()


        for item in  self.result:
            self.__processaItem(item)


        """
        Áté ção
        for item in sorted( self.erros, key= itemgetter('valor', 'msg')):
            print u'{0};{1};{2};'\
                    .format(item['msg'], item['valor'], item['planilha'])
            #print u'{0}'.format( item['valor'])
        """    


 
        self.__sendMail()

    def __adderro(self, msg, valor, planilha):

        erro = { 'msg'     : msg,     \
                 'valor'   : valor,   \
                 'planilha': planilha }

        #objerro = ObjectView(erro)
        self.erros.append(erro)

    def __procExcel(self):

        workbook = xlrd.open_workbook(PATH_ARQUIVO)
        sheet = workbook.sheet_by_index(0)
        for row in range(1, sheet.nrows):
            _laudo = sheet.cell(row,0).value
            _laudo = _laudo.replace('.0','')

            _data = xlsDate_as_datetime( sheet.cell(row,1).value, 0)
            _ponto = sheet.cell(row,2).value
            _param = sheet.cell(row,4).value
            _caminho =sheet.cell(row,5).value
 
            try:
                _valor = sheet.cell(row,3).value
            except:
                continue

            registro = { 'controle' : _laudo.strip(),   \
                         'ponto' : _ponto.strip(),      \
                         'data'  : _data,       \
                         'chave' : _laudo.strip(),      \
                         'param' : _param.strip(),      \
                         'valor' : _valor,      \
                         'caminho' : _caminho.strip() }

            reg = ObjectView(registro)

            self.result.append(reg)


    def __converte(self, folha):

        workbook = xlrd.open_workbook(PATH_FERRAMENTA)
        sheet = workbook.sheet_by_index(folha)
        for row in range(1, sheet.nrows):
            _de   = sheet.cell(row,0).value
            _de   = _de.strip()

            _para = sheet.cell(row,1).value
            _para = u'{0}'.format(_para).strip()

            if folha == 0:
                self.pontoConv[_de] = _para
            else:
                self.paramConv[_de] = _para


    def __sendMail(self):
        objMail = Email()

        content = u' '
        content += u'Abaixo lista de erros encontrados ao processar as planilha dos laboratorios: <br>'
        content += u'<table border="1">'
        content += u'<thead>'
        content += u'<tr>'
        content += u'<td>Erro</td><td>Valor</td><td>Planilha</td>'
        content += u'</tr>'
        content += u'</thead>'
        for item in sorted( self.erros, key= itemgetter('valor', 'msg')):
            linha = u'<tr><td>{0}</td><td>{1}</td><td>{2}</td></tr>'\
                  .format(item['msg'], \
                         item['valor'],\
                         item['planilha'])
            content += linha
        



        content += u'</table>'
        content += u'<p> {0} Erros encontrados </p>'.format(len(self.erros))
        content += u'<p> {0} Processados </p>'.format(self.processados)

        destinatario = u'{0} <{1}>'.format('Wilson', 'wbeirigo@terravisiongeo.com.br')

        objMail.EnviaMSG('Projeto CEMIG - Consistencia Parametros Laboratorios',
                        content,
                        [ destinatario, ],
                        True )


    def __processaItem(self, item):

        """
        Parametro
        """
        if item.param in self.paramConv:
            item.param = self.paramConv[item.param].strip()


        if item.param == 'Excluir':
            return False


        col = Param.objects.filter(nome = item.param) 
        if len(col) == 0:
            self.__adderro(u'Parâmetro não existe',   \
                        item.param,               \
                        item.caminho )
            return False
        else:
            objParametro = col[0]
        del col


        """
        Local
        """
        item.ponto  = item.ponto.replace(' ','').replace('-','').strip()
       
        if item.ponto in self.pontoConv:
            item.ponto = self.pontoConv[item.ponto].strip()
            item.ponto  = item.ponto.replace(' ','').replace('-','').strip()


        if item.ponto == 'Excluir':
            return False

        col = PtoMonit.objects.filter(sigla = item.ponto)
        if len(col) == 0:
            self.__adderro(u'Ponto de monitoramento não existe',   \
                            item.ponto,                            \
                            item.caminho )
            return False
        else:
            objLocal = col[0]

        del col


        """
        Tratamento de valor
        """
        if item.valor.strip() == 'L.T.':
            return False

        if '<' in item.valor:
            float_vlr = float(0)
        else:
            _vl = item.valor.replace('<','').replace(',','.')
            try:
                float_vlr = float(_vl)
            except:
               self.__adderro(u'Erro ao converter valor',   \
                            item.valor,                  \
                            item.caminho )
               return False


        """
        Medicao
        """
        col = Medicao.objects.filter( PtoMonit_FK  = objLocal,
                                      Parametro_FK = objParametro,
                                      controle     = item.controle,
                                      data         = item.data) 
        if len(col) > 0:
            return False

    
        """
        Campanha
        """
        objCampanha = getCampanha(ID_PROJETO, item.data)

        registro = Medicao( Campanha_FK  = objCampanha,
                                PtoMonit_FK  = objLocal,
                                Parametro_FK = objParametro,
                                controle     = item.controle,
                                data         = item.data,
                                vlr          = float_vlr,
                                vlrLbl       = item.valor) 
                
        registro.save() 
        self.processados += 1 

        return True



def run():

   obj = ProcMedicao() 
