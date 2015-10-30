# -*- coding: utf-8 -*- 
#!/usr/bin/env python 


from  monitor.models import KPI, KPI_Nivel
from  monitor.fma    import FMA

def run():

    data = datetime.now

    titulo = 'Formula de Monte Alegre'
    subtitulo = 'Serra do Rola Moca 10/10/2015'
    tituloY = 'Indice da Formula'
    unidade = 'indice'
    data['dia'] = data.day
    data['mes'] = data.month
    data['ano'] = data.year


    
    objFMA = FMA()
    objFMA.execute(



    col = []
    objKPI = KPI.objects.get(nome = 'FMA')
    for item in KPI_Nivel.objects.filter( KPI_FK = objKPI):
        mask  = """$ from: {0}, to: {1},\
color: '{2}',\
label: $ text: '{3}', style: $ color: '{4}' @ @ @"""

        linha = mask.format(item.v1, item.v2, \
                            item.cor, item.texto, \
                           "#606060")

        linha = linha.replace('$', '{').replace('@','}')
        col.append(linha)



# Previsao('3106200')



