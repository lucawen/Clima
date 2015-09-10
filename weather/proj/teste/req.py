# -*- coding: utf-8 -*-
#!/usr/bin/env python

from django.contrib.gis.gdal import DataSource
from django.contrib.gis.gdal import OGRGeometry

url = 'http://10.2.8.239:80/geoserver/wfs?srsName=EPSG%3A4326&typename=geonode%3Aamericadosul&outputFormat=json&version=1.0.0&service=WFS&request=GetFeature'

ponto = OGRGeometry('POINT (-43.84667 -19.98556)')
ds = DataSource(url)
layer = ds[0]
layer.spatial_filter = ponto.extent

print '--LEN-----'
print len(layer)
print '--GET-----'
print [feat.get('CNTRY_NAME') for feat in layer]
print '-------'

