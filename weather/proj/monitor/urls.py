
# -*- coding: utf-8 -*- 
#!/usr/bin/env python 

from django.conf.urls import url
from django.contrib import admin
from monitor import views
from models import FocoWFABBA, FocoFIRMS
from djgeojson.views import GeoJSONLayerView

urlpatterns = [    
    url(r'^mailalertafoco/(?P<idAlarme>\d+)/$', views.mailalertafoco),
    url(r'^dashboard/(?P<idProjeto>\d+)/$', views.dashboard),
    url(r'^wfabba.geojson$', GeoJSONLayerView.as_view(model= FocoWFABBA, properties=('id', 'dataregUTC',))),
    url(r'^firms.geojson$', GeoJSONLayerView.as_view(model= FocoFIRMS, properties=('id', 'dataregUTC',))),
]


