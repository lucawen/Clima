from django.conf.urls import url
from django.contrib import admin

from normais import views


urlpatterns = [    
    url(r'^$', views.grafico, name='grafico'),
    url(r'^estacoes/$', views.estacoes ),
    url(r'^grafico/(?P<station>\d+)/$', views.grafico ),
]

