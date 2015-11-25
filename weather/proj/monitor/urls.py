
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
    url(r'^firmsLayer/(?P<start>\d+)/(?P<end>\d+)/$', views.firmsLayer),
    url(r'^wfabbaLayer/(?P<start>\d+)/(?P<end>\d+)/$', views.wfabbaLayer),
    url(r'^focoPopUp/(?P<chave>\w+)/$', views.focoPopUp),
]


