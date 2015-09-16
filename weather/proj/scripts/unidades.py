# -*- coding: utf-8 -*-
#!/usr/bin/env python

import django
from param.models import Unidade, Param
import datetime


param = [ 
[u'Coliformes Totais', u'NMP/100mL'],
[u'Surfactantes Ani\xf4nicos', u'mg MBAS/L'],
[u'Sulfato', u'mg SO4/L'],
[u'Solidos Suspensos Totais', u'mg SST/L'],
[u'Zoob\xeanton Qualitativo', u'ind./m2'],
[u'Ultima Chuva', u'NOUNIT'],
[u'Nitrato (N)', u'mg N_NO3/L'],
[u'Nitrato', u'mg NO3/L'],
[u'Sulfeto', u'mg S2-/L'],
[u'Nitrog\xeanio Amoniacal ', u'mg N_NH3/L'],
[u'Cloreto', u'mg Cl-/L'],
[u'Sulfeto de Hidrog\xeanio', u'mg H2S/L'],
[u'Manganes Dissolvido', u'mg Mn/L'],
[u'Dureza Total ', u'mg CaCO3/L'],
[u'Solidos Sedimentaveis', u'ml/L'],
[u'Cobre Dissolvido', u'mg Cu/L'],
[u'Tempo', u'NOUNIT'],
[u'Fen\xf3is ', u'mg/L'],
[u'Hora Amostragem', u'H'],
[u'* VMP - Valores m\xe1ximos permitidos, conforme CONAMA_357_2005_A.DOCE_Classe 2, COPAM_1_2008_A.DOCE_Classe 2', ''],
[u'Alum\xednio Total', u'mg Al/L'],
[u'Ferro Dissolvido', u'mg Fe/L'],
[u'Clorofila a', u'\xb5g/L'],
[u'Demanda Quimica de Oxig\xeanio', u'mg O2/L'],
[u'F\xf3sforo Total', u'mg P/L'],
[u'Nitrog\xeanio Total', u'mg N/L'],
[u'Oleos Graxas Vegetal ', u'mg/L'],
[u'Turbidez ', u'NTU'],
[u'Data Amostragem', u'NOUNIT'],
[u'Dureza Calcica ', u'mg CaCO3/L'],
[u'Demanda Bioquimica de Oxig\xeanio', u'mg O2/L'],
[u'LEGENDA', ''],
[u'* VMP - Valores m\xe1ximos permitidos, conforme CONAMA_357_2005_A.DOCE_Classe 2', ''],
[u'Nitrito', u'mg NO2/L'],
[u'Zoob\xeanton Quantitativo', u'ind./m2'],
[u'Alcalinidade Total', u'mg CaCO3/L'],
[u'S\xf3lidos Dissolvidos Totais', u'mg SDT/L'],
[u'* VMP - Valores m\xe1ximos permitidos, conforme CONAMA_430_Efluente', ''],
[u'Estreptococos Fecais', u'UFC/100mL'],
[u'Coliformes Termotolerantes', u'UFC/100mL'],
[u'Cor Verdadeira', u'mg Pt/L'],
[u'Nitrito (N)', u'mg N_NO2/L'],
[u'Oleos e Graxas Totais', u'mg/L'],
[u'Oleos Graxas Mineral ', u'mg/L'],
[u'Cianobacteria', u'cel./mL'],
]



def run():

    todos = Param.objects.exclude(id=2)
    todos.delete()

    objRoot = Param.objects.get(id=2)

    for item in param:

	objUnidade = Unidade.objects.filter(sigla = item[1])
	if len(objUnidade) == 0:
		Obj = Unidade(sigla=item[1], descricao = 'xxxx')
		Obj.save()	
		objUnidade = Unidade.objects.filter(sigla = item[1])

	objParam = Param.objects.filter(nome = item[0])
	if len(objParam) == 0:
		objParam = Param(nome = item[0],
				 unidade_FK = objUnidade[0], 
				 monitorado = '0',
				 tipoParametro = '0',
				 vlrTeto = 0,
				 vlrPiso = 0, 
				 parent = objRoot) 
		objParam.save()

	



