# -*- coding: utf-8 -*-
#!/usr/bin/env python

import pandas as pd
import django
from param.models import Unidade, Param, Limites
from projetos.models import Medicao, PtoMonit, Projeto, Campanha
from django.template import Context, Template
from json import dumps
import requests
import base64
import time
from PIL import Image
from StringIO import StringIO
from docx import Document
from docx.shared import Inches


def geraGraphico(_col_pontos, _col_campanha, _parametro,  _idleg, _idclasse):

    ID_LEGISLACAO = _idleg
    ID_CLASSE = _idclasse





    cores = [ '#73A374', '#b0ccb0', '#a8cdd7', '#c0beaf', '#cec597', '#e8b7b7', '#66A7B9', '#6a6755',
                '#B4E789', '#F4AABA', '#94AECD', '#C2C174', '#8B878F', '#C3A3D7',
                '#77B25A', '#E7ACBC', '#7E93A6', '#93B483','#BC8A97','#B6C6D6',
                '#D6C7A1','#9FA0A1','#4E763F','#495D71','#9F6270','#725E29','#5E5C57',
                '#B4E789', '#F4AABA', '#94AECD', '#C2C174', '#8B878F', '#C3A3D7',
                '#77B25A', '#E7ACBC', '#7E93A6', '#93B483','#BC8A97','#B6C6D6',
                '#D6C7A1','#9FA0A1','#4E763F','#495D71','#9F6270','#725E29','#5E5C57',
            ]

    template = """
{chart: {  width:800, plotBackgroundColor: '#E6E6E6'  },
title: { text: ' ' },
xAxis: [{ categories: {{categories|safe}} , crosshair: true, labels: {style: {fontWeight: 'bold'}}}],
yAxis: [{title:{ text: '{{ str_param }}',style: {fontWeight: 'bold'} }, labels: { style: {fontWeight: 'bold'} }}],
credits: { text: ' ', href: ' '},
plotOptions: { line: { lineWidth: 2, marker: { enabled: false}}},
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
          filter( Parametro_FK_id=_parametro).\
          values("Parametro_FK_id",
                 "Campanha_FK_id",
                 "PtoMonit_FK_id",
                 "vlrLbl",
                 "vlr").\
          order_by("Parametro_FK_id",
                   "Campanha_FK_id",
                   "PtoMonit_FK_id")

    col = []
    for item in col0:
        if item["PtoMonit_FK_id"] in _col_pontos and \
           item["Campanha_FK_id"] in _col_campanha:

            if '<' not in item['vlrLbl']:
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


    lim_min = {}
    lim_max = {}
    """ Determina Limites """
    col_limite  = Limites.objects.filter(parametro_FK_id = _parametro,
                                     legislacao_FK_id = ID_LEGISLACAO,
                                     classe_FK_id = ID_CLASSE)
    if col_limite:
        obj_limite = col_limite[0]
        if obj_limite.vlr_max != 0:
            linha = [ float(obj_limite.vlr_max) for it in ptomonit ]
            lim_max = { 'name':'VMP', 'type':'line', 'color':'red', 'data':linha }

        if obj_limite.vlr_min != 0:
            color = 'red' if lim_max  else 'blue'
            linha = [ float(obj_limite.vlr_min) for it in ptomonit ]
            lim_min = { 'name':'VMP', 'type':'line', 'color':color, 'data':linha }

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
        if sum(dados) != 0:
            registro = {'name': '{0}'.format(obj_campanha),
                        'type':'column',
                        'data':dados,
                        'color': cores[pos]}
            series.append(registro)
            pos += 1

    if len(series) == 0:
        return None

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
    parametro = Param.objects.get(pk=_parametro)
    str_param = u'{0} ({1})'.format(parametro.nome , parametro.unidade_FK)

    """
    Renderiza o template
    """
    contexto = Context({    'categories' : categories,
                            'str_param': str_param,
                            'series':series})
    templ = Template(template)
    saida = templ.render(contexto)

    saida= '{"infile":"' + saida.encode('utf-8','ignore') + '","constr":"Chart"}'
    saida = saida.replace('\n','')

    return saida

def processa(_col_pontos, _col_campanha, _col_parametro,  _idleg, _idclasse):

    document = Document()
    document.add_heading('Document Title', 0)


    URL_PHANTOM = 'http://10.3.0.29:3003'
    headers ={ 'Content-Type': 'application/json', '-X POST':'' }
    indice = 1

    col0 = Medicao.objects.\
          values("Parametro_FK_id",
                 "Campanha_FK_id",
                 "PtoMonit_FK_id",
                 "vlrLbl",
                 "vlr").\
          order_by("Campanha_FK_id",
                   "Parametro_FK_id",
                   "PtoMonit_FK_id")

    """
    grade_tabela = []
    for camp in _col_campanha:
        grade_tabela[camp] = []
        for param in _col_param:
            grade[camp][param] = []
            for pto in _col_pontos:
                grade_tabela[camp][param][pto] = ''
    """

    for item in col0:

        if item['Parametro_FK_id'] in (798,840):
            continue

        if item['Campanha_FK_id'] in _col_campanha and \
           item['PtoMonit_FK_id'] in _col_pontos and \
           item['Parametro_FK_id'] in _col_parametro:


            z = _col_campanha.index(item['Campanha_FK_id'])
            x = _col_parametro.index(item['Parametro_FK_id'])
            y = _col_pontos.index(item['PtoMonit_FK_id'])
            grade_tabela[z][x][y] = item['vlrLbl']


    for parametro  in _col_parametro:

        """ Não processa parametros Data e Profundidade"""
        if parametro in (798,840):
            continue

        saida = geraGraphico(_col_pontos, _col_campanha, parametro, _idleg, _idclasse)
        if not saida:
            continue
        r = requests.post(URL_PHANTOM, data=saida, headers=headers)
        png_recovered = base64.decodestring(r.content)
        path = "/tmp/{0}.png".format(int(time.time()*1000))
        f = open(path, "w")
        f.write(png_recovered)
        f.close()

        obj_param = Param.objects.get(pk=parametro)
        nome = obj_param.nome
        texto = obj_param.texto

        document.add_heading(u'6.{0} - {1}'.format(indice, nome), level=1)

        document.add_paragraph(texto)
        document.add_heading(u'Figura 6.{0} -Resultados obtidos para o parâmetro {1}'.format(indice, nome), level=2)
        document.add_picture(path, width=Inches(5.2))
        document.add_page_break()
        indice += 1
    path = "/tmp/{0}.docx".format(int(time.time()*1000))
    document.save(path)
    return path


