# -*- coding: utf-8 -*-
#!/usr/bin/env python

import django
from normais.regras import NormalGraficos

def run():
    teste = NormalGraficos(380).getGrafico()
    print teste




