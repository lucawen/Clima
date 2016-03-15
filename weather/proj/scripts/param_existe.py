# -*- coding: utf-8 -*-
#!/usr/bin/env python

import pandas as pd

def run():
    df = pd.read_excel('/media/projeto_cemig/01_SOFTWARE/param_existe.xls', 0, index_col=0)

    for it in df.index.unique():
        print(it.encode('utf-8'))





