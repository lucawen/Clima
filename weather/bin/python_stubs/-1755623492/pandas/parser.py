# encoding: utf-8
# module pandas.parser
# from /usr/local/lib/python2.7/dist-packages/pandas/parser.so
# by generator 1.138
# no doc

# imports
import pandas.lib as lib # /usr/local/lib/python2.7/dist-packages/pandas/lib.so
import numpy as np # /usr/local/lib/python2.7/dist-packages/numpy/__init__.pyc
import warnings as warnings # /usr/lib/python2.7/warnings.pyc
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import sys as sys # <module 'sys' (built-in)>
import time as time # <module 'time' (built-in)>
import os as os # /usr/lib/python2.7/os.pyc
import numpy as __numpy


# Variables with simple values

DEFAULT_CHUNKSIZE = 262144

# functions

def downcast_int64(*args, **kwargs): # real signature unknown
    pass

def _compute_na_values(*args, **kwargs): # real signature unknown
    pass

def _concatenate_chunks(*args, **kwargs): # real signature unknown
    pass

def _ensure_encoded(*args, **kwargs): # real signature unknown
    pass

def _is_file_like(*args, **kwargs): # real signature unknown
    pass

def _maybe_encode(*args, **kwargs): # real signature unknown
    pass

def _maybe_upcast(*args, **kwargs): # real signature unknown
    """  """
    pass

def _to_structured_array(*args, **kwargs): # real signature unknown
    pass

# classes

class CParserError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __qualname__ = 'CParserError'


class DtypeWarning(Warning):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class k(__numpy.signedinteger, int):
    """ 64-bit integer. Character code 'l'. Python int compatible. """
    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __index__(self): # real signature unknown; restored from __doc__
        """ x[y:z] <==> x[y.__index__():z.__index__()] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass


class OverflowError(ValueError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __qualname__ = 'OverflowError'


class TextReader(object):
    """ # source: StringIO or file object """
    def debug_print(self, *args, **kwargs): # real signature unknown
        pass

    def read(self, *args, **kwargs): # real signature unknown
        """ rows=None --> read all rows """
        pass

    def remove_noconvert(self, *args, **kwargs): # real signature unknown
        pass

    def set_error_bad_lines(self, *args, **kwargs): # real signature unknown
        pass

    def set_noconvert(self, *args, **kwargs): # real signature unknown
        pass

    def _convert_column_data(self, *args, **kwargs): # real signature unknown
        pass

    def _get_converter(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    allow_leading_cols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    as_recarray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    buffer_lines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    compact_ints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    compression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    delimiter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    delim_whitespace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    header = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    header_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    header_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    index_col = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leading_cols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    low_memory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mangle_dupe_cols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    memory_map = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    na_values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    noconvert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    orig_header = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skiprows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skip_footer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    table_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tupleize_cols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    usecols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    use_unsigned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


# variables with complex values

na_values = {
    None:  # (!) real value is ''
        255
    ,
    np.ubyte: 
        255
    ,
    np.byte: 
        -128
    ,
    None:  # (!) real value is ''
        -128
    ,
    None:  # (!) real value is ''
        255
    ,
    None:  # (!) real value is ''
        -32768
    ,
    None:  # (!) real value is ''
        65535
    ,
    None:  # (!) real value is ''
        -2147483648
    ,
    None:  # (!) real value is ''
        4294967295
    ,
    None:  # (!) real value is ''
        -9223372036854775808
    ,
    np.uint0: 
        18446744073709551615L
    ,
    np.int64: 
        -9223372036854775808
    ,
    None:  # (!) real value is ''
        nan
    ,
    np.double: 
        nan
    ,
    np.uintc: 
        4294967295
    ,
    np.ushort: 
        65535
    ,
    np.int32: 
        -2147483648
    ,
    None:  # (!) real value is ''
        18446744073709551615L
    ,
    np.int16: 
        -32768
    ,
    np.bool8: 
        255
    ,
    np.object0: 
        nan
    ,
    None:  # (!) real value is ''
        nan
    ,
}

_NA_VALUES = [
    '-1.#IND',
    '1.#QNAN',
    '1.#IND',
    '-1.#QNAN',
    '#N/A N/A',
    'NA',
    '#NA',
    'NULL',
    'NaN',
    'nan',
    '',
]

__test__ = {}

