
# -*- coding: utf-8 -*- 
#!/usr/bin/env python 

from django.conf.urls import url
from django.contrib import admin
from monitor import views

urlpatterns = [    
    url(r'^mailalertafoco/(?P<idAlarme>\d+)/$', views.mailalertafoco),
]

