from django.conf.urls import url
from django.contrib import admin

from normais import views


urlpatterns = [    
    url(r'^$', views.normais ),
    url(r'^normais/$', views.normais ),
    url(r'^automaticas/$', views.automaticas ),
    url(r'^grafnormais/(?P<station>\d+)/(?P<texto>\w+)/$', views.grafnormais ),
    url(r'^grafautomatica/(?P<station>\d+)/(?P<mes>\d+)/(?P<ano>\d+)/(?P<texto>\w+)/$', views.grafAutomatica ),
    url(r'^getautomaticajson/(?P<station>\d+)/$', views.getautomaticajson),
    url(r'^grafautomaticatotal/(?P<station>\d+)/(?P<texto>\w+)/$', views.grafAutomaticaTotal),
]

