# encoding: utf-8
# module pandas.index
# from /usr/local/lib/python2.7/dist-packages/pandas/index.so
# by generator 1.138
# no doc

# imports
import numpy as np # /usr/local/lib/python2.7/dist-packages/numpy/__init__.pyc
import pandas.tslib as tslib # /usr/local/lib/python2.7/dist-packages/pandas/tslib.so
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import pytz as pytz # /usr/local/lib/python2.7/dist-packages/pytz/__init__.pyc
import pandas.algos as algos # /usr/local/lib/python2.7/dist-packages/pandas/algos.so
import pandas.hashtable as _hash # /usr/local/lib/python2.7/dist-packages/pandas/hashtable.so
from pandas.tslib import Timedelta, Timestamp

import datetime as __datetime


# Variables with simple values

have_pytz = True

_SIZE_CUTOFF = 1000000

# functions

def convert_scalar(*args, **kwargs): # real signature unknown
    pass

def get_value_at(*args, **kwargs): # real signature unknown
    pass

def set_value_at(*args, **kwargs): # real signature unknown
    pass

# classes

class IndexEngine(object):
    # no doc
    def clear_mapping(self, *args, **kwargs): # real signature unknown
        pass

    def get_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def get_indexer_non_unique(self, *args, **kwargs): # real signature unknown
        """
        return an indexer suitable for takng from a non unique index
                    return the labels in the same order ast the target
                    and a missing indexer into the targets (which correspond
                    to the -1 indicies in the results
        """
        pass

    def get_loc(self, *args, **kwargs): # real signature unknown
        pass

    def get_value(self, *args, **kwargs): # real signature unknown
        """ arr : 1-dimensional ndarray """
        pass

    def set_value(self, *args, **kwargs): # real signature unknown
        """ arr : 1-dimensional ndarray """
        pass

    def _call_monotonic(self, *args, **kwargs): # real signature unknown
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    is_monotonic_decreasing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_monotonic_increasing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_unique = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mapping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    over_size_threshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    vgetter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class Int64Engine(IndexEngine):
    # no doc
    def get_backfill_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def get_pad_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def _call_monotonic(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class DatetimeEngine(Int64Engine):
    # no doc
    def get_backfill_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def get_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def get_loc(self, *args, **kwargs): # real signature unknown
        pass

    def get_pad_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def _call_monotonic(self, *args, **kwargs): # real signature unknown
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class Float64Engine(IndexEngine):
    # no doc
    def get_backfill_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def get_pad_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def _call_monotonic(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class ObjectEngine(IndexEngine):
    # no doc
    def get_backfill_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def get_pad_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def _call_monotonic(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class TimedeltaEngine(DatetimeEngine):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class _du_utc(__datetime.tzinfo):
    # no doc
    def dst(self, *args, **kwargs): # real signature unknown
        pass

    def tzname(self, *args, **kwargs): # real signature unknown
        pass

    def utcoffset(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ helper for pickle """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


# variables with complex values

UTC = pytz.UTC

_backfill_functions = {
    'float64': algos.backfill_float64,
    'int64': algos.backfill_int64,
    'object': algos.backfill_object,
}

_pad_functions = {
    'float64': algos.pad_float64,
    'int64': algos.pad_int64,
    'object': algos.pad_object,
}

__test__ = {}

