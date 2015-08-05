from django.conf.urls import url
from django.contrib import admin

from . import views


urlpatterns = [    
    url(r'^$', views.mapa, name='mapa'),
    url(r'^registros/(?P<station>\d+)/(?P<parametro>\d+)/$', views.registros, ),
]

