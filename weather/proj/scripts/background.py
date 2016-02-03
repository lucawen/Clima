# -*- coding: utf-8 -*-
#!/usr/bin/env python

import django
from monitor import firms, wfabba, alarme
from  toolbox.maillib import Email

def run():

    msgs = []

    try:
	obj = firms.FIRMS()
	obj.processa()
    except:
	msgs.append('FIRMS: Erro ao processar FIRM')
    finally:	
	del obj

    try: 
        obj = wfabba.WFABBA()
	obj.processa()
    except:
	msgs.append('WFABB: Erro ao processar WFABBA')
    finally:	
	del obj



    try:
        obj = alarme.AlarmeProc()
        obj.processa()
    except:
	msgs.append('ALARME: Erro ao processar ALARME')
    finally:	
	del obj

    if msgs:
        msg = ''.join(str(e) for e in msgs)
	objMail = Email()
	objMail.EnviaMSG('Fire Monitor',
		         'ROTINA DE PROCESSAMENTO FIREMONITOR,' + msg,
                         [ 'wbeirigo@terravisiongeo.com.br', ])


