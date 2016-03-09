import pandas as pd
from projetos.models import Medicao, PtoMonit
from param.models import Param
#import openpyxl

def run():
    qs = Medicao.objects.filter(Campanha_FK_id=15, PtoMonit_FK__parent_id=2235).values('Parametro_FK', 'PtoMonit_FK', 'id')
    df = pd.DataFrame.from_records(qs)

    saida = pd.pivot_table(df, index=[ 'Parametro_FK'], columns=['PtoMonit_FK'], values=['id'], fill_value=0)

    db_param  =  list(Param.objects.all().values('id', 'nome', 'unidade_FK__sigla').order_by('nome'))
    db_pontos  = list(PtoMonit.objects.all().values('id', 'sigla').order_by('sigla'))

    colunas = [ item[1] for item in  list(saida.columns)]
    pontos = [ item for item in db_pontos if item['id'] in colunas ]
    param = [ item for item in db_param if item['id'] in list(saida.index)]

    linhas = []

    """Header"""
    linhaBranco = [ '' for item in colunas]

    for x in param:
        linhas.append(list(linhaBranco))

    col_datas = []
    pos_profund = []

    for key_param in saida.index:
        reg_param = [ item for item in param if item['id'] == key_param][0]
        pos_param = param.index(reg_param)

        for key_pto in saida.loc[key_param].index:
            reg_pto = [ item for item in pontos if item['id'] == key_pto[1] ][0]
            pos_pto = pontos.index(reg_pto)

            key_vlr = saida.loc[key_param].get(key_pto)
            if key_vlr == 0:
                continue
            if key_param == 840:
                vlr = Medicao.objects.get(pk=key_vlr).data
            else:
                vlr = Medicao.objects.get(pk=key_vlr).vlrLbl
            linhas[pos_param][pos_pto] = vlr

    pos = 0
    for item in linhas:
        if sum([1 for it in item if it!='']) < 2:
            continue
        item.insert(0, param[pos]['unidade_FK__sigla'])
        item.insert(0, param[pos]['nome'])
        item.insert(0, param[pos]['id'])
        print(item)
        pos +=1


