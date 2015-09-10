# -*- coding: utf-8 -*- 
#!/usr/bin/env python 

from django.contrib.gis.gdal import DataSource
import os
import sys
from os import walk

path = '/home/wbeirigo/Clima/dados/cemig'
f = []
for (dirpath, dirnames, filenames) in walk(path):
    f.extend(filenames)
    break

pm = []


for itFile in f:
    ds = DataSource(path + '/' + itFile)
    layer = ds[0]

    campos =  layer.get_fields('Name')
    pontos =  [pt.tuple for pt in layer.get_geoms()]

    for indice in range(len(pontos)):
        pm.append( [ campos[indice].encode('ascii', 'ignore'), str(pontos[indice][0]), str(pontos[indice][1]) ] )
             


for pt in pm:
    print u'{0};{1};{2};'.format(pt[0], pt[1].replace('.',','), pt[2].replace('.',','))
