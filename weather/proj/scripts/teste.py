# -*- coding: utf-8 -*- 
#!/usr/bin/env python 

import django
from toolbox.staticmap import StaticMap

from monitor.models import FocoFIRMS, FocoWFABBA, Alarme
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.gdal import OGRGeometry
from django.contrib.gis.geos import GEOSGeometry, Polygon

"""
    Exmplo Gera Gráfico
    center = [-20.06843,-44.00069]
    markers  = [(-20.06843,-44.00069), (-20.1643,-44.169)]

    mapa = StaticMap()
    mapa.markers = markers
    path = mapa.processa(center)
    print path
"""


def urlFiltro():

    url = 'http://geonode.brandt.local/geoserver/geonode/ows?service=WFS&\
version=1.0.0&request=GetFeature&\
typeName=geonode:poligonorolamoca&\
outputFormat=application/json'
            
    return url

def addAlarme(_alg, _id, _msg, pos):
    query = Alarme.objects.filter( algoritimo = _alg,\
                                foco_id = _id)
    if len(query) == 0:

        #Gera Mapa
        center = [pos[0],pos[1]]
        markers  = [center]

        mapa = StaticMap()
        mapa.markers = markers
        path = mapa.processa(center)

        print _alg, _id, path

        obj = Alarme(algoritimo = _alg,\
                     foco_id    = _id,\
                     msg        = path)
        obj.save()


def run():
    url = urlFiltro()
    ds = DataSource(url)
    layer = ds[0]
    col = layer.get_geoms()
    poly = col[0][0]
    
    for item in FocoFIRMS.objects.all():
        layer.spatial_filter = item.posicao.extent
        if len(layer) > 0:
            addAlarme( 'FIRMS',\
                       item.id,\
                       '',\
                       item.posicao)

    for item in FocoWFABBA.objects.all():
        layer.spatial_filter = item.posicao.extent
        if len(layer) > 0:
            addAlarme( 'WFABBA',\
                       item.id,\
                       '',\
                       item.posicao)


