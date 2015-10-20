# -*- coding: utf-8 -*-
#!/usr/bin/env python

import django
from monitor import firms, wfabba
from  toolbox.maillib import Email

def run():
    obj = firms.FIRMS()
    obj.processa()
    
    obj = wfabba.WFABBA()
    obj.processa()

    objMail = Email()
    objMail.EnviaMSG('Fire Monitor',
                'Focos de Incendio Processados com SUCESSO, FIRMS e WAFBBA',
                [ 'wbeirigo@terravisiongeo.com.br', ])


