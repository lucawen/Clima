# -*- coding: utf-8 -*-
#!/usr/bin/env python


from  param.models    import Param, Legislacao, Classe, Limites
import xlrd


def run():

    caminho = '/home/wbeirigo/Clima/dados/cemig/VMP_limnologia.xls'

    workbook = xlrd.open_workbook(caminho)
    sheet = workbook.sheet_by_index(0)


    col_colunas = [ (2, 3) , (4, 5) , (6, 7), (8, 9)]
    col_classe = [1, 2, 1, 2 ]
    col_legis  = [0, 0, 1, 1 ]


    for row in range(3, sheet.nrows):

        idParam =  int(sheet.cell(row, 0).value)
        obj_param = Param.objects.get(id=idParam)
        if not obj_param:
            continue

        for col in  col_colunas:
            vlr0 = sheet.cell(row, col[0]).value
            vlr1 = sheet.cell(row, col[1]).value

            if not vlr0 and not vlr1:
                continue

            try:
                valor0 = float(vlr0)
            except:
                valor0 =  0

            try:
                valor1 = float(vlr1)
            except:
                valor1 = 0

            indice = col_colunas.index(col)
            key_classe = col_classe[indice]
            obj_classe = Classe.objects.get(pk=key_classe )

            key_legis  = col_legis[indice]
            obj_legis = Legislacao.objects.get(pk=key_legis )

            registro = Limites(classe_FK = obj_classe, legislacao_FK=obj_legis, parametro_FK = obj_param, vlr_min = valor0,  vlr_max = valor1)
            Limites.save(registro)
