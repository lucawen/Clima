


def run():

    from normais.modelos import ChartsTypes

    gc = ChartsTypes()
    """
    col = gc.getAll()
    sigla = 'LN'
    print [x for x in col if x[0] == 'LN' ][0]a
    """
    print gc.getBySigla('LN')
