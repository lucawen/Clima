# -*- coding: utf-8 -*-
#!/usr/bin/env python

import django
from param.models import Unidade, Param, Limites
from projetos.models import Medicao, PtoMonit, Projeto, Campanha
from django.template import Context, Template
from json import dumps
import requests
import base64


from PIL import Image
from StringIO import StringIO



def geraGraphico(_col_pontos, _col_campanha, _parametro,  _idleg, _idclasse):

    ID_LEGISLACAO = _idleg
    ID_CLASSE = _idclasse



    cores = [   ('226666',),
                ('226666', '2E882E'),
                ('AA3939', 'AA6C39', '226666'),
                ('AA3939','AA6C39','226666','2E882E'),
                ('AA3939','AA6C39','226666','2E882E', 'FFD1AA'),
                ('AA3939', 'D46A6A', 'D49A6A', '407F7F', '55AA55',
                 '2E882E'),
                ('AA3939', 'D46A6A', 'D49A6A', '407F7F', '55AA55',
                 '2E882E', '88CC88'),
                ('FFAAAA', '550000', 'FFD1AA', '552700', '669999',
                 '003333', '88CC88', '004400'),
                ('AA3939','FFAAAA','D46A6A','801616','550000',
                 'AA6C39','FFD1AA','D49A6A','804616','552700','669999',
                 '407F7F','0D4D4D','003333','226666','88CC88','55AA55',
                 '116611','004400') ]

    template = """
{title: { text: ' ' },
xAxis: [{ categories: {{categories|safe}}, crosshair: true }],
yAxis: [{title:{ text: '{{ str_param }}'}}],
credits: { text: ' ', href: ' '},
plotOptions: { line: { lineWidth: 4, marker: { enabled: false}}},
series: [ {% for item in series %}
{ color:'{{item.color}}', data:{{item.data}}, name:'{{ item.name}}', type:'{{item.type}}'},
{% endfor %}]}
"""

    ptomonit = []
    campanha = []
    grade = {}


    """
    Seleciona no banco os registros a serem tratados
    """
    col0 = Medicao.\
          objects.\
          filter( Parametro_FK_id=ID_PARAM).\
          values("Parametro_FK_id",
                 "Campanha_FK_id",
                 "PtoMonit_FK_id",
                 "vlr").\
          order_by("Parametro_FK_id",
                   "Campanha_FK_id",
                   "PtoMonit_FK_id")

    col = []
    for item in col0:
        if item["PtoMonit_FK_id"] in col_pontos and \
           item["Campanha_FK_id"] in col_campanha:
            col.append(item)


    """
    Cria os pontos e as campanhas
    """
    for item in col:
        key = item["PtoMonit_FK_id"]
        if not key in ptomonit:
            ptomonit.append(key)

        key = item["Campanha_FK_id"]
        if not key in campanha:
            campanha.append(key)

    """
    Determina a paleta a ser usada em função do número de campanhas
    """
    for item in cores:
        if len(item) >= len(campanha):
            paleta = item
            break

    """
    Cria grade Campanhas X Pontos
    """
    for item in col:
        camp = item["Campanha_FK_id"]
        if camp in grade:
            linha = grade[camp]
        else:
            linha = [0 for itpto in ptomonit]

        pto = item["PtoMonit_FK_id"]
        index = ptomonit.index(pto)
        linha[index] = item["vlr"]

        grade[camp] = linha


    """ Determina Limites """
    lim_min = {}
    lim_max = {}
    col_limite  = Limites.objects.filter(parametro_FK_id = ID_PARAM,
                                     legislacao_FK_id = ID_LEGISLACAO,
                                     classe_FK_id = ID_CLASSE)
    if col_limite:
        obj_limite = col_limite[0]
        if obj_limite.vlr_max <> 0:
            linha = [ float(obj_limite.vlr_max) for it in ptomonit ]
            lim_max = { 'name':'', 'type':'line', 'color':'red', 'data':linha }

        if obj_limite.vlr_min <> 0:
            linha = [ float(obj_limite.vlr_min) for it in ptomonit ]
            lim_min = { 'name':'', 'type':'line', 'color':'red', 'data':linha }


    """
    Cria cria categorias
    """
    categories = []
    for item in ptomonit:
        ponto = PtoMonit.objects.get(pk=item).sigla
        categories.append('{0}'.format(ponto))


    """
    Cria  as series
    """
    series = []
    pos = 0
    for item in grade:
        obj_campanha = Campanha.objects.get(pk=item).nome
        dados = [ float(it) for it in grade[item] ]
        registro = {'name': '{0}'.format(obj_campanha),
                    'type':'column',
                    'data':dados,
                    'color': '#{0}'.format(paleta[pos])}
        series.append(registro)
        pos += 1

    """
    Adiciona limites se houver
    """
    if lim_max:
        series.append(lim_max)

    if lim_min:
        series.append(lim_min)


    """
    Texto contendo o parâmetro do gráfico
    """
    parametro = Param.objects.get(pk=ID_PARAM)
    str_param = u'{0} ({1})'.format(parametro.nome , parametro.unidade_FK)

    """
    Renderiza o template
    """
    contexto = Context({    'categories' : categories,
                            'str_param': str_param,
                            'series':series})
    templ = Template(template)
    saida = templ.render(contexto)

    saida= '{"infile":"' +  saida + '","constr":"Chart"}'
    saida = saida.replace('\n','')
    return saida

def processa(_col_pontos, _col_campanha, _col_parametro,  _idleg, _idclasse)

    URL_PHANTOM = 'http://10.3.0.29:3003'
    headers ={ 'Content-Type': 'application/json', '-X POST':'' }
    for parametro  in _col_parametro:
        saida = geraGraphico(_col_pontos, col_campanha, parametro, _idclasse)
        r = requests.post(URL_PHANTOM, data=saida, headers=headers)
        png_recovered = base64.decodestring(r.content)
        arq = int(datetime.now())
        f = open("{0}.png".format(arq), "w")
        f.write(png_recovered)
        f.close()



def run():
    pass


