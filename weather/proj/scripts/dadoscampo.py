# -*- coding: utf-8 -*-
#!/usr/bin/env python


from  param.models    import Param
from  projetos.models import PtoMonit, Medicao, Projeto, Campanha
from  toolbox.tools   import ObjectView
from  toolbox.tools   import lerDataExcel, convert_excel_time
from  dateutil        import parser
import xlrd
from  toolbox.maillib import Email
from django.utils import timezone

def getCampanha(idProjeto, dataHora):

    colCampanha = Campanha.objects.\
                    filter(Projeto_FK_id = idProjeto,\
                            ano = dataHora.year,\
                            mes = dataHora.month)

    if len(colCampanha)  == 0:
        nmCamp = 'Campanha {0}/{1}'.format(dataHora.month, dataHora.year)
        objCampanha = Campanha( nome = nmCamp,
                                mes  =  dataHora.month,
                                ano  =  dataHora.year,
                                Projeto_FK = objProjeto)
        objCampanha.save()
    else:
        objCampanha = colCampanha[0]

    return objCampanha


def isMedicao(_ponto, _param, _data):

    col = Medicao.objects.filter(data = _data,
                                PtoMonit_FK = _ponto,
                                Parametro_FK = _param )

    return len(col) == 0
                                


def run():

    idProjeto = 1
    caminho = '/home/wbeirigo/Clima/dados/dadoscampo/DADOS_CAMPO.xls'
    erros = []
    errosParam = 0

    workbook = xlrd.open_workbook(caminho)
    sheet = workbook.sheet_by_index(0)
    inLancto = False

    colPos = [5,6,7,8,9,10,11,12]
    colMedicao = []

    for row in range(0, sheet.nrows):

        if row == 0:
            for col in colPos:
                idParam =  int(sheet.cell(row, col).value)
                objparam = Param.objects.filter(id = idParam)
                if len(objparam) == 0:
                    erros.append({  'linha':row, \
                                    'valor' : idParam,\
                                    'msg':'Parametro nao encontrado'\
                                 })
            errosParam = len(erros)



        if row >= 2 and errosParam == 0 :

            codEstacao = sheet.cell(row, 1).value

            objEstacao = PtoMonit.objects.filter(sigla= codEstacao)
            if len(objEstacao) == 0:
                erros.append({  'linha':row, \
                                'valor' : codEstacao,\
                                'msg':'Ponto nao existe'\
                            })
                continue

            try:

                data = lerDataExcel(sheet.cell(row,3).value)
                hr = sheet.cell(row,4).value
                hora = convert_excel_time(hr, False)
                mask = '{0} {1}'.format(data, hora)
            except:
                erros.append({  'linha' : row, \
                                'valor' : sheet.cell(row,3)  ,\
                                'msg'   : 'Data ou hora com formatos invalidos'\
                                 })
                continue

            dataHora =  parser.parse(mask)
            dataHora = timezone.make_aware(dataHora, timezone.get_current_timezone())

            valores = []
            for col in colPos:
                vlr    = sheet.cell(row, col).value
                if vlr == '':
                    vlr = 0.0

                try:
                    vlrF = float(vlr)
                except:
                   erros.append({  'linha':row, \
                                    'valor' : vlr ,\
                                    'msg':'Campo valor formato invalido'\
                                     })
                   continue

                param  = sheet.cell(0, col).value
                valores.append( [param, vlrF] )     


            registro = {'codEstacao' : codEstacao,               \
                        'data'       : dataHora,                 \
                        'controle'   : 'Linha:{0}'.format(row),  \
                        'valores'    : valores                   \
                       }


            item =ObjectView(registro)

            colMedicao.append(item)

    
    for item in colMedicao:

        objEstacao = PtoMonit.objects.get(sigla= item.codEstacao)
        objCampanha = getCampanha(idProjeto, item.data.date())

        for param, valor in item.valores:
            objParam = Param.objects.get(id= param)
            
            if isMedicao(objEstacao, objParam,  item.data):
                objMed = Medicao(Campanha_FK = objCampanha, \
                                PtoMonit_FK = objEstacao,  \
                                Parametro_FK = objParam,   \
                                controle = item.controle,  \
                                data = item.data,          \
                                vlr  = valor,         \
                                vlrLbl = '')
                objMed.save()
            

    objMail = Email()

    content = ' ' 
    content += 'Abaixo lista de erros encontrados ao processar a planilha de parametros: <br>'

    content += '<table border="1">'
    content += '<thead>'
    content += '<tr>'
    content += '<td>Linha</td><td>Valor</td><td>Erro</td>'
    content += '</tr>'
    content += '</thead>'
    for item in erros:
        content += '<tr><td>{0}</td><td>{1}</td><td>{2}</td></tr>'\
                   .format(item['linha'], item['valor'], item['msg'])
    content += '</table>'
    content += '<p> {0} Erros encontrados </p>'.format(len(erros))

    content = objMail.mask().format(content)

    destinatario = '{0} <{1}>'.format('Wilson', 'wbeirigo@terravisiongeo.com.br')

    objMail.EnviaMSG('Projeto CEMIG - Consistencia Parametros Formulario',
                    content,
                    [ destinatario, ],
                    True )

