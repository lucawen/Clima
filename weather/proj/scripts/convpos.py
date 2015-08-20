
# -*- coding: utf-8 -*- 
#!/usr/bin/env python 

import django
import normais.models as db
from  normais.dms2dec import dms2dec
import re

def run():
    col = db.Station.objects.all()
    for reg in col:
        val = reg.LatLong.replace('(','').replace(')','').split(',')
        p1 = u'{0}'.format(val[0]).replace(' ', '').replace('\'', '\'0.0')
        p2 = u'{0}'.format(val[1]).replace(' ', '').replace('\'', '\'0.0')
        try:
            lati   = dms2dec(p1)
            longi = dms2dec(p2)

            reg.posicao = 'SRID=4326;POINT({0} {1})'.format(longi, lati)
            reg.save()


        except:
            print 'Erro!!!!!', val[0], val[1]


