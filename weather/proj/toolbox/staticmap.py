# -*- coding: utf-8 -*- 
#!/usr/bin/env python 

import requests
from proj import settings
import shutil

#GOOGLE STATIC API KEY
API_KEY    = 'AIzaSyDLoBDJBVGCajNFLGcLhBVNB3OnBpym68M'
HTTP_OK    = 200
URL        = 'https://maps.googleapis.com/maps/api/staticmap?{0}'
FORMATO    = 'jpg'

class StaticMap:


    def __init__(self):
        self.markers = []
        self.filename = None

    def processa(self, center,\
                 size='800x600',\
                 type='hybrid',\
                 zoom=10101010101010101010 ):


        arquivo  ='{0}.{1}'.format(self.filename, FORMATO)

        strmark=''
        for pos in self.markers:
            strmark += 'markers={0},{1}&'.format(pos[1], pos[0]) 

        mask= 'center={0},{1}&zoom={2}&size={3}&maptype={4}&{5} key={6}'

        url_postfix = mask.format(center[1], center[0],\
                                  zoom,\
                                  size,\
                                  type,\
                                  strmark,
                                  API_KEY)

        url = URL.format(url_postfix)

        r = requests.get(url, stream=True)
        if r.status_code != HTTP_OK:
            raise 'Erro ao consultar Google API'
        else:
            filename ='{0}{1}'.format(settings.MEDIA_ROOT, arquivo)
            with open(filename, 'wb') as fd:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, fd)


        return '{0}{1}'.format(settings.MEDIA_URL, arquivo)

