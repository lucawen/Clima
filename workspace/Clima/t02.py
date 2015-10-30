#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests import Request, Session
import lxml.html
from lxml import cssselect
import re
import logging
from datetime import datetime, timedelta
import time
import json

from pacote.tools import Tools
from pacote.modelos import Estacao, DadosEstacao
import psycopg2  
import smtplib

__author__ = "Wilson Beirigo Duarte"
__maintainer__ = "Wilson Beirigo Duarte"
__version__ = "0.1"
__script_name__ = "estacao.py"
        
           
def sendmail(str):
    fromaddr = 'wilson@solvecorp.com.br'
    toaddrs  = 'wbeirigo@terravisiongeo.com.br'

    message = """From: Sistema FIREMONITOR <wilson@solvecorp.com.br>
To: Wilson Beirigo Duarte <iwbeirigo@iterravisiongeo.com.br>
Subject: Estacoes Climaticas 

Estacoes climaticas processadas
                """

    message += str

    username = 'wilson@solvecorp.com.br'
    password = 'wilci5w7'

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, message)
    server.quit()

        
if __name__ == "__main__":
    
    STRING_CONEXAO = "dbname='clima' user='postgres' host='10.3.0.26' password='wilci5w7'"

    db = psycopg2.connect(STRING_CONEXAO) 
    dados = DadosEstacao()
    teste = dados.getResult(db)
    str = '\n\n'
    for item in teste:
        str += '{0}\t{1}\n'.format( item[0], item[1])


    sendmail(str)
