
# -*- coding: utf-8 -*- 
#!/usr/bin/env python 

from django.conf.urls import url
from django.contrib import admin
from roi import views

urlpatterns = [    
    url(r'^roi/$', views.roi),
]


