# -*- coding: utf-8 -*-
#!/usr/bin/env python


from automaticas.graficos import GeraGraficos
from datetime import datetime 

 
def run():

    obj = GeraGraficos()

    obj.pool('86852', datetime(2015,1,1), 'M', 'estacao do wilson')




