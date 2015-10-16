# -*- coding: utf-8 -*-
#!/usr/bin/env python

import django
from monitor import firms, wfabba
import smtplib

def sendmail():
    fromaddr = 'wilson@solvecorp.com.br'
    toaddrs  = 'wbeirigo@terravisiongeo.com.br'

    message = """From: Sistema FIREMONITOR <wilson@solvecorp.com.br>
To: Wilson Beirigo Duarte <wbeirigo@iterravisiongeo.com.br>
Subject: Focos de Incendio 
Focos de incedio FIRMS e WAFBBA processados
    """

    username = 'wilson@solvecorp.com.br'
    password = 'wilci5w7'

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, message)
    server.quit()


def run():
    obj = firms.FIRMS()
    obj.processa()
    
    obj = wfabba.WFABBA()
    obj.processa()

    sendmail()


