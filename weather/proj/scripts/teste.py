# -*- coding: utf-8 -*- 
#!/usr/bin/env python 

import requests
from  toolbox.maillib import Email

def run():

    url = 'http://10.3.0.29:8080/mailalertafoco/168/'
    r = requests.get(url)
    objMail = Email()
    objMail.EnviaMSG('Fire Monitor',
                r.content,
                [ 'wbeirigo@terravisiongeo.com.br', 'wilson@solvecorp.com.br' ],
                True )


