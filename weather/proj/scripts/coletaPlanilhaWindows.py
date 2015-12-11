import os
import sys
import xlrd
import xlwt
import datetime as dt

arquivos = []
resultados = []
import datetime as dt
def Converte_Data(param):
	try:
		data_int = xlrd.xldate_as_tuple(int(param), 0)
		saida_1 = dt.date(data_int[0], data_int[1], data_int[2])
	except:
		saida_1 = dt.date(1900,1,1)
	return saida_1


caminho = '//brandt.local/arquivos/Users/Area_Tecnica/PROJETO CEMIG'

for dirpath, dirs, files in os.walk(caminho):	
	for dir in dirs:
		for file in files:
			if file[-3:] == 'xls':
				caminho = '{0}\\{1}'.format(dirpath, file)
				workbook = xlrd.open_workbook(caminho)
				sheet = workbook.sheet_by_index(0)
				data = [[sheet.cell_value(r, col)
                for col in range(sheet.ncols)] 
                    for r in range(sheet.nrows)]
				if data[0][0] == 'Relatorio No:':
					arquivos.append(caminho)	
					resultados.append(data)	

metodos = {}
unidades = []
linhas = []
saida = []

book = xlwt.Workbook()
sheet1 = book.add_sheet("SAIDA")

index = 0
for planilha in resultados:					
	limites = len(planilha[6]) - 3
	posVlr = 2 + limites
	ponto = planilha[8][posVlr]
	data = planilha[9][posVlr]
	numrel = planilha[0][1]
	for item in planilha[10:]:
		metodo = item[0]
		if not metodo in metodos:
			metodos[metodo] = item[1]		
		if not  item[1] in unidades:
			unidades.append(item[1])
		
		vlr = item[posVlr]					
		numcol = 0
		if 	metodo.strip() != '' and   \
			metodo[:7] not in ['LEGENDA', '* VMP -'] and \
			metodo not in ['Data Amostragem','Hora Amostragem','Ultima Chuva','Tempo'] and \
			ponto.strip() != '' and \
			vlr.strip() != '':
			for elem in [numrel, Converte_Data(data), ponto,vlr,metodo, item[1]]:						
				row = sheet1.row(index)
				row.write(numcol, elem)
				numcol += 1
			index +=1
		
		
book.save("d:/wilson001.xls")

for item in arquivos:
	print item

for item in metodos:
	print [ item, metodos[item] ]




		
