HOST   = "host='10.2.8.239' \
         dbname='geonode_data'\
         user='geonode'\
         password='FsBUYSRW'"

# -*- coding: utf-8 -*-
#!/usr/bin/env python

import psycopg2

camadas = ["_1peng02u_ger_pl_buffer_eixo_geo__wgs84",
            "_1peng02u_ger_pl_dutos_zee_geo_wgs84",
            "_1peng02u_ger_pl_eixo_utm_wgs84_25s",
            "_1peng02u_ger_pl_ferrovia_geo_wgs84",
            "_1peng02u_ger_pl_monotrilho_geo_wgs84",
            "_1peng02u_ger_pl_monotrilho_sirgas2000",
            "_1peng02u_ger_pl_monotrilho_sirgas2000_1                          ",
            "_1peng02u_ger_pl_municipio_ibge_2005_geo_wgs84                    ",
            "_1peng02u_ger_pl_rodovia_geo_wgs84                                ",
            "_1peng02u_ger_pl_uc_estadual_protecaointegral_geo_wgs84           ",
            "_1peng02u_ger_pl_uc_estadual_usosustentave_geo_wgs84              ",
            "_1peng02u_ger_pl_uc_estadual_usosustentave_geo_wgs84_1            ",
            "_1peng02u_ger_pl_uc_estadual_usosustentave_geo_wgs84_2 ",
            "_1peng02u_ger_pl_uc_estadual_usosustentave_geo_wgs84_3 ",
            "_1peng02u_ger_pl_uc_estadual_usosustentave_geo_wgs84_4 ",
            "_1peng02u_ger_pl_uc_estadual_usosustentave_geo_wgs84_5 ",
            "_1peng02u_ger_pl_uc_federal_geo_wgs84_1                ",
            "_1peng02u_ger_pl_uc_federal_geo_wgs84_2                ",
            "_1peng02u_ger_pl_uc_federal_geo_wgs84_3                    ",
            "_1peng02u_ger_pl_uc_federal_geo_wgs84_4                    ",
            "_1peng02u_ger_pl_uc_federal_geo_wgs84_5                    ",
            "_1peng02u_ger_pl_uc_federal_geo_wgs84_6                    ",
            "_1peng02u_ger_pl_uc_municipal_protecaointegral_geo_wgs84   ",
            "_1peng02u_ger_pl_uc_municipal_usosustentave_geo_wgs84      ",
            "_1peng02u_ger_pl_uc_municipal_usosustentave_geo_wgs84_1    ",
            "_1peng02u_ger_pl_uc_municipal_usosustentave_geo_wgs84_2    ",
            "_1peng02u_ger_pl_uc_municipal_usosustentave_geo_wgs84_3    ",
            "_1peng02u_ger_pl_uc_municipal_usosustentave_geo_wgs84_4    ",
            "_1peng02u_ger_pl_uc_municipal_usosustentave_geo_wgs84_5    ",
            "_1peng02u_ger_pl_uc_municipal_usosustentave_geo_wgs84_6    ",
            "_1peng02u_ger_pl_zoneamento_aprm_billings_geo_wgs84        ",
            "_1peng02u_ger_pl_zoneamento_aprm_billings_geo_wgs84_1      ",
            "_1peng02u_ger_pl_zoneamento_terrestre_geo_wgs84            ",
            "plano_diretor                                              ",]


try:
    connstring = HOST
    db  = psycopg2.connect(connstring)
except:
    raise


for tabela in camadas:
    tab = tabela.strip()
    try:
        sql = "DROP TABLE {0};".format(tab)
        print sql
        cursor = db.cursor()
        cursor.execute(sql)
    except:
        raise




