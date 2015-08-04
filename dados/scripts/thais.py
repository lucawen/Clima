# -*- coding: utf-8 -*-

import xlrd
import re

"""
Converting Degrees, Minutes, Seconds formatted coordinate strings to decimal. 
Formula:
DEC = (DEG + (MIN * 1/60) + (SEC * 1/60 * 1/60))
Assumes S/W are negative. 
"""


def dms2dec(dms_str):
    """Return decimal representation of DMS
    
    >>> dms2dec(utf8(48°53'10.18"N))
    48.8866111111F
    
    >>> dms2dec(utf8(2°20'35.09"E))
    2.34330555556F
    
    >>> dms2dec(utf8(48°53'10.18"S))
    -48.8866111111F
    
    >>> dms2dec(utf8(2°20'35.09"W))
    -2.34330555556F
    
    """
    dms_str = re.sub(r'\s', '', dms_str)
    
    if re.search('[swSW]', dms_str):
        sign = -1
    else:
        sign = 1
   
    (degree, minute, second, frac_seconds, junk) = re.split('\D+', dms_str, maxsplit=4)
    
    return sign * (int(degree) + float(minute) / 60 + float(second) / 3600 + float(frac_seconds) / 36000)


col = [
        [u'15°44\'31.0\"S', u'41°27\'09.0\"W'],
        [u'15°44\'27.0\"S', u'41°27\'23.0\"W'],
        [u'15°47\'55.0\"S', u'41°22\'47.0\"W'],
        [u'15°12\'59.0\"S', u'41°55\'55.0\"W'],
        [u'15°47\'48.0\"S', u'41°30\'11.0\"W'],
        [u'15°45\'30.0\"S', u'41°35\'55.0\"W'],
        [u'15°35\'59.0\"S', u'41°24\'45.0\"W'],
        [u'15°18\'29.0\"S', u'41°56\'20.0\"W'],
        [u'15°20\'36.0\"S', u'42°4\'46.0\"W'],
        [u'15°21\'28.0\"S', u'42°0\'56.0\"W'],
        [u'15°21\'28.0\"S', u'41°46\'33.0\"W'],
        [u'15°20\'53.0\"S', u'42°4\'58.0\"W']
]


for i in col:
    print u'[{0},{1}] ==== [{2},{3}]'.format( i[0], i[1], dms2dec(i[0]), dms2dec(i[1]) )



