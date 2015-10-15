
from django.conf.urls import url
from django.contrib import admin
from djgeojson.views import GeoJSONLayerView

from igam import views


from .models import Pontos


urlpatterns = [    
    url(r'mapaigam/pontos.geojson$', GeoJSONLayerView.as_view(model= Pontos,       \
                                                     properties=('id',)  \
                                                   ), name='data'),      \
    url(r'^mapaigam/$', views.mapaigam),
    url(r'mapaigam/pontoIgam/(?P<id>\d+)/$', views.pontoIgam),
]

