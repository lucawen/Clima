# -*- coding: utf-8 -*-
#!/usr/bin/env python

import django
from param.models import Unidade, Param
from projetos.models import Medicao, PtoMonit, Projeto, Campanha
import datetime
import xlrd
import chardet

def xlsDate_as_datetime(xldate, datemode):
    # datemode: 0 for 1900-based, 1 for 1904-based
    xldate = float('0' + str(xldate))
    return (
        datetime.datetime(1899, 12, 30)
        + datetime.timedelta(days=xldate + 1462 * datemode)
        )

def run():

    conv = {}
    conv[ u'MM001' ]  =  u'MM01'
    conv[ u'MM002F']  =  u'MM02F'
    conv[ u'MM002ZF'] =  u'MM02ZF'
    conv[ u'MM002S']  =  u'MM02S'
    conv[ u'MM003']   =  u'MM03'
    conv[ u'MM004F']  =  u'MM04F'
    conv[ u'MM004ZF'] =  u'MM04ZF'
    conv[ u'MM004S']  =  u'MM04S'
    conv[ u'MM005F']  =  u'MM05F'
    conv[ u'MM005ZF'] =  u'MM05ZF'
    conv[ u'MM005S']  =  u'MM05S'
    conv[ u'PF002S']  =  u'PF002'
    conv[ u'PF006S']  =  u'PF006'
    conv[ u'SG0034']  =  u'SG004'
    conv[ u'SG005S']  =  u'SG005'


    ptoNotFound = []
    objParamRoot = Param.objects.get(id=426)
    projeto = Projeto.objects.get(id=1)

    indice = 0
    fail = 0
    dup = 0

    #caminho = '/home/wbeirigo/Clima/dados/bioagri/consolidado.xls'
    caminho = '/home/wbeirigo/Clima/dados/wilson001.xls'
    workbook = xlrd.open_workbook(caminho)
    sheet = workbook.sheet_by_index(0)
    for row in range(1, sheet.nrows):
        _laudo = sheet.cell(row,0).value
	_data = xlsDate_as_datetime( sheet.cell(row,1).value, 0)
	_ano = _data.year
	_mes = _data.month

	_ponto = sheet.cell(row,2).value
	
	try:
	    _valor = str(sheet.cell(row,3).value).encode('ascii', 'ignore')
	except:
	   continue

	_param = sheet.cell(row,4).value
	_unidad= sheet.cell(row,5).value


	if _unidad == u'~leader=~bdut.u.unitname~~':
		continue


	campanhas = Campanha.objects.filter(ano = _ano, mes = _mes)
	if len(campanhas) == 0:
		regCamp = Campanha(	Projeto_FK= projeto, 
				nome ='Campanha {0}/{1}'.format(_mes, _ano), 
				mes = _mes, 
				ano = _ano)
		regCamp.save()
	else:
		regCamp = campanhas[0]

	_unidad = _unidad.replace(' ','').replace('-','')
        unidades = Unidade.objects.filter(sigla = _unidad)
        if len(unidades) == 0:
                ObjUnidade = Unidade(sigla=_unidad, descricao = 'xxxx')
                ObjUnidade.save()
	else:
		objUnidade = unidades[0]

	parametros = Param.objects.filter(nome = _param)
        if len(parametros) == 0:
                objParam = Param(nome = _param,
                                 unidade_FK = objUnidade,
                                 monitorado = '0',
                                 tipoParametro = '0',
                                 vlrTeto = 0,
                                 vlrPiso = 0,
                                 parent = objParamRoot )
                objParam.save()
	else:
	    	objParam = parametros[0]


	_ponto = _ponto.replace(' ','').replace('-','').strip()  
	key = u'{0}'.format(_ponto)
	if key in conv:
		_ponto = conv[key]


	pontos = PtoMonit.objects.filter(sigla = _ponto)
	if len(pontos) == 0:
		pontos = PtoMonit.objects.filter(sigla = _ponto + 'S')
		if len(pontos) == 0:
		    if len(pontos) == 0:
		        if not _ponto in ptoNotFound:
		       	    ptoNotFound.append(_ponto)
			fail += 1
		        continue


	if '<' in str(_valor):
	    float_vlr = float(0)
	else:
            _vl = _valor.replace('<','').replace(',','.')
	    try:
	        float_vlr = float(_vl) 
	    except:
		print _valor, _vl
	        float_vlr = float(0)
	
	indice += 1

	if len(Medicao.objects.filter(Campanha_FK = regCamp,
                                      PtoMonit_FK = pontos[0],
                                      data = _data,
                                       Parametro_FK = objParam)) == 0:

		medicao = Medicao(Campanha_FK = regCamp, 
				  PtoMonit_FK = pontos[0],
				  Parametro_FK = objParam,
				  controle =  str(_laudo).replace('.0',''),
				  data = _data,
				  vlrLbl = _valor,
				  vlr =  float_vlr)

		medicao.save()                
	else:
		dup += 1 

    print indice, fail, sheet.nrows, dup


    for item in ptoNotFound:
	a = item.encode('ascii', 'ignore')
        print a

