# -*- coding: utf-8 -*-
#!/usr/bin/env python

import django
from monitor import firms, wfabba

def run():
    obj = firms.FIRMS()
    obj.processa()
    
    obj = wfabba.WFABBA()
    obj.processa()


