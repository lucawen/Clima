

from arcpy import env, GetParameterAsText, AddMessage
from arcpy.da import da 

lotes = {}
tabela = GetParameterAsText(0)
env.workspace = 'D:/tv/dados/Sorocaba_Lote.gdb'

tabela = 'Lote'


shapeSearch = da.UpdateCursor(tabela, ['Inscricao', 'isDuplicado'])         
for item in shapeSearch :    
    key = item[0]    
    if key:
        if key and key in lotes:
            value = lotes[key]
        else:
            value = 0

        item[1] = 0
        shapeSearch.updateRow(item)
        lotes[key] = value + 1
    
del shapeSearch


conta = 0
for item in lotes.items():    
    if item[1] > 1:
        conta += 1
        shapeSearch = da.UpdateCursor(tabela, ['Inscricao', 'isDuplicado'], "Inscricao = '{0}'".format(item[0]))         
        for it in shapeSearch:
            it[1] = 1
            print it[0]
            shapeSearch.updateRow(it)
        del shapeSearch

del lotes

AddMessage('Encotrados {0} registros duplicados'.format(conta))




