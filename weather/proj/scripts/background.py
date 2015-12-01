# -*- coding: utf-8 -*-
#!/usr/bin/env python

import django
from monitor import firms, wfabba, alarme
from  toolbox.maillib import Email

def run():
    obj = firms.FIRMS()
    obj.processa()
    del obj
    
    obj = wfabba.WFABBA()
    obj.processa()
    del obj


    obj = alarme.AlarmeProc()
    obj.processa()
    del obj


    objMail = Email()
    objMail.EnviaMSG('Fire Monitor',\
                'Focos de Incendio Processados com SUCESSO, FIRMS e WAFBBA,\
                Alarmes processados com sucesso',\
                [ 'wbeirigo@terravisiongeo.com.br', ])

