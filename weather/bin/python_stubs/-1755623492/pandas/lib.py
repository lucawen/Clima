# encoding: utf-8
# module pandas.lib
# from /usr/local/lib/python2.7/dist-packages/pandas/lib.so
# by generator 1.138
# no doc

# imports
import pandas.tslib as tslib # /usr/local/lib/python2.7/dist-packages/pandas/tslib.so
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import numpy as np # /usr/local/lib/python2.7/dist-packages/numpy/__init__.pyc
import sys as sys # <module 'sys' (built-in)>
from datetime import pydate, pydatetime

from pandas.tslib import NaT, Timedelta, Timestamp

import distutils.version as __distutils_version


# Variables with simple values

iNaT = -9223372036854775808

is_numpy_prior_1_6_2 = False

# functions

def apply_frame_axis0(*args, **kwargs): # real signature unknown
    pass

def array_equivalent_object(*args, **kwargs): # real signature unknown
    """
    perform an element by element comparion on 1-d object arrays
            taking into account nan positions
    """
    pass

def array_to_timestamp(*args, **kwargs): # real signature unknown
    pass

def arrmap(*args, **kwargs): # real signature unknown
    pass

def astype_intsafe(*args, **kwargs): # real signature unknown
    pass

def astype_str(*args, **kwargs): # real signature unknown
    pass

def astype_unicode(*args, **kwargs): # real signature unknown
    pass

def checknull(*args, **kwargs): # real signature unknown
    pass

def checknull_old(*args, **kwargs): # real signature unknown
    pass

def clean_index_list(*args, **kwargs): # real signature unknown
    """ Utility used in pandas.core.index._ensure_index """
    pass

def convert_sql_column(*args, **kwargs): # real signature unknown
    pass

def convert_timestamps(*args, **kwargs): # real signature unknown
    pass

def count_level_2d(*args, **kwargs): # real signature unknown
    pass

def dicts_to_array(*args, **kwargs): # real signature unknown
    pass

def duplicated(*args, **kwargs): # real signature unknown
    pass

def fast_multiget(*args, **kwargs): # real signature unknown
    pass

def fast_unique(*args, **kwargs): # real signature unknown
    pass

def fast_unique_multiple(*args, **kwargs): # real signature unknown
    pass

def fast_unique_multiple_list(*args, **kwargs): # real signature unknown
    pass

def fast_unique_multiple_list_gen(*args, **kwargs): # real signature unknown
    pass

def fast_zip(*args, **kwargs): # real signature unknown
    """ For zipping multiple ndarrays into an ndarray of tuples """
    pass

def fast_zip_fillna(*args, **kwargs): # real signature unknown
    """ For zipping multiple ndarrays into an ndarray of tuples """
    pass

def generate_bins_dt64(*args, **kwargs): # real signature unknown
    """ Int64 (datetime64) version of generic python version in groupby.py """
    pass

def generate_slices(*args, **kwargs): # real signature unknown
    pass

def get_blkno_indexers(*args, **kwargs): # real signature unknown
    """
    Enumerate contiguous runs of integers in ndarray.
    
        Iterate over elements of `blknos` yielding ``(blkno, slice(start, stop))``
        pairs for each contiguous run found.
    
        If `group` is True and there is more than one run for a certain blkno,
        ``(blkno, array)`` with an array containing positions of all elements equal
        to blkno.
    
        Returns
        -------
        iter : iterator of (int, slice or array)
    """
    pass

def get_level_sorter(*args, **kwargs): # real signature unknown
    """
    argsort for a single level of a multi-index, keeping the order of higher
        levels unchanged. `starts` points to starts of same-key indices w.r.t
        to leading levels; equivalent to:
            np.hstack([label[starts[i]:starts[i+1]].argsort(kind='mergesort')
                + starts[i] for i in range(len(starts) - 1)])
    """
    pass

def get_reverse_indexer(*args, **kwargs): # real signature unknown
    """
    Reverse indexing operation.
    
        Given `indexer`, make `indexer_inv` of it, such that::
    
            indexer_inv[indexer[x]] = x
    
        .. note:: If indexer is not unique, only first occurrence is accounted.
    """
    pass

def group_count(*args, **kwargs): # real signature unknown
    pass

def has_infs_f4(*args, **kwargs): # real signature unknown
    pass

def has_infs_f8(*args, **kwargs): # real signature unknown
    pass

def indexer_as_slice(*args, **kwargs): # real signature unknown
    pass

def indices_fast(*args, **kwargs): # real signature unknown
    pass

def infer_dtype(*args, **kwargs): # real signature unknown
    """ we are coercing to an ndarray here """
    pass

def ismember(*args, **kwargs): # real signature unknown
    """
    Checks whether
    
        Parameters
        ----------
        arr : ndarray
        values : set
    
        Returns
        -------
        ismember : ndarray (boolean dtype)
    """
    pass

def ismember_int64(*args, **kwargs): # real signature unknown
    """
    Checks whether
    
        Parameters
        ----------
        arr : ndarray of int64
        values : set
    
        Returns
        -------
        ismember : ndarray (boolean dtype)
    """
    pass

def ismember_nans(*args, **kwargs): # real signature unknown
    pass

def isnan(x, out=None): # real signature unknown; restored from __doc__
    """
    isnan(x[, out])
    
    Test element-wise for NaN and return result as a boolean array.
    
    Parameters
    ----------
    x : array_like
        Input array.
    
    Returns
    -------
    y : ndarray or bool
        For scalar input, the result is a new boolean with value True if
        the input is NaN; otherwise the value is False.
    
        For array input, the result is a boolean array of the same
        dimensions as the input and the values are True if the
        corresponding element of the input is NaN; otherwise the values are
        False.
    
    See Also
    --------
    isinf, isneginf, isposinf, isfinite
    
    Notes
    -----
    Numpy uses the IEEE Standard for Binary Floating-Point for Arithmetic
    (IEEE 754). This means that Not a Number is not equivalent to infinity.
    
    Examples
    --------
    >>> np.isnan(np.nan)
    True
    >>> np.isnan(np.inf)
    False
    >>> np.isnan([np.log(-1.),1.,np.log(0)])
    array([ True, False, False], dtype=bool)
    """
    pass

def isneginf_scalar(*args, **kwargs): # real signature unknown
    pass

def isnullobj(*args, **kwargs): # real signature unknown
    pass

def isnullobj2d(*args, **kwargs): # real signature unknown
    pass

def isnullobj2d_old(*args, **kwargs): # real signature unknown
    pass

def isnullobj_old(*args, **kwargs): # real signature unknown
    pass

def isposinf_scalar(*args, **kwargs): # real signature unknown
    pass

def isscalar(*args, **kwargs): # real signature unknown
    """
    Return True if given value is scalar.
    
        This includes:
        - numpy array scalar (e.g. np.int64)
        - Python builtin numerics
        - Python builtin byte arrays and strings
        - None
        - instances of datetime.datetime
        - instances of datetime.timedelta
        - Period
    """
    pass

def is_bool(*args, **kwargs): # real signature unknown
    pass

def is_bool_array(*args, **kwargs): # real signature unknown
    pass

def is_bytes_array(*args, **kwargs): # real signature unknown
    pass

def is_complex(*args, **kwargs): # real signature unknown
    pass

def is_datetime64_array(*args, **kwargs): # real signature unknown
    pass

def is_datetime_array(*args, **kwargs): # real signature unknown
    pass

def is_date_array(*args, **kwargs): # real signature unknown
    pass

def is_float(*args, **kwargs): # real signature unknown
    pass

def is_float_array(*args, **kwargs): # real signature unknown
    pass

def is_integer(*args, **kwargs): # real signature unknown
    pass

def is_integer_array(*args, **kwargs): # real signature unknown
    pass

def is_integer_float_array(*args, **kwargs): # real signature unknown
    pass

def is_lexsorted(*args, **kwargs): # real signature unknown
    pass

def is_period(*args, **kwargs): # real signature unknown
    pass

def is_period_array(*args, **kwargs): # real signature unknown
    pass

def is_possible_datetimelike_array(*args, **kwargs): # real signature unknown
    pass

def is_string_array(*args, **kwargs): # real signature unknown
    pass

def is_timedelta64_array(*args, **kwargs): # real signature unknown
    pass

def is_timedelta_array(*args, **kwargs): # real signature unknown
    pass

def is_timedelta_or_timedelta64_array(*args, **kwargs): # real signature unknown
    """ infer with timedeltas and/or nat/none """
    pass

def is_time_array(*args, **kwargs): # real signature unknown
    pass

def is_unicode_array(*args, **kwargs): # real signature unknown
    pass

def item_from_zerodim(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    If the value is a zerodim array, return the item it contains.
    
        Examples
        --------
        >>> item_from_zerodim(1)
        1
        >>> item_from_zerodim('foobar')
        'foobar'
        >>> item_from_zerodim(np.array(1))
        1
        >>> item_from_zerodim(np.array([1]))
        array([1])
    """
    pass

def list_to_object_array(*args, **kwargs): # real signature unknown
    """
    Convert list to object ndarray. Seriously can't believe I had to write this
        function
    """
    pass

def lookup_values(*args, **kwargs): # real signature unknown
    pass

def map_indices_list(*args, **kwargs): # real signature unknown
    """
    Produce a dict mapping the values of the input array to their respective
        locations.
    
        Example:
            array(['hi', 'there']) --> {'hi' : 0 , 'there' : 1}
    
        Better to do this with Cython because of the enormous speed boost.
    """
    pass

def map_infer(*args, **kwargs): # real signature unknown
    """
    Substitute for np.vectorize with pandas-friendly dtype inference
    
        Parameters
        ----------
        arr : ndarray
        f : function
    
        Returns
        -------
        mapped : ndarray
    """
    pass

def map_infer_mask(*args, **kwargs): # real signature unknown
    """
    Substitute for np.vectorize with pandas-friendly dtype inference
    
        Parameters
        ----------
        arr : ndarray
        f : function
    
        Returns
        -------
        mapped : ndarray
    """
    pass

def max_len_string_array(*args, **kwargs): # real signature unknown
    """ return the maximum size of elements in a 1-dim string array """
    pass

def maybe_booleans_to_slice(*args, **kwargs): # real signature unknown
    pass

def maybe_convert_bool(*args, **kwargs): # real signature unknown
    pass

def maybe_convert_numeric(*args, **kwargs): # real signature unknown
    """
    Type inference function-- convert strings to numeric (potentially) and
        convert to proper dtype array
    """
    pass

def maybe_convert_objects(*args, **kwargs): # real signature unknown
    """ Type inference function-- convert object array to proper dtype """
    pass

def maybe_indices_to_slice(*args, **kwargs): # real signature unknown
    pass

def memory_usage_of_objects(*args, **kwargs): # real signature unknown
    """
    return the memory usage of an object array in bytes,
        does not include the actual bytes of the pointers
    """
    pass

def reduce(*args, **kwargs): # real signature unknown
    """
    Paramaters
        -----------
        arr : NDFrame object
        f : function
        axis : integer axis
        dummy : type of reduced output (series)
        labels : Index or None
    """
    pass

def row_bool_subset(*args, **kwargs): # real signature unknown
    pass

def row_bool_subset_object(*args, **kwargs): # real signature unknown
    pass

def sanitize_objects(*args, **kwargs): # real signature unknown
    pass

def scalar_binop(*args, **kwargs): # real signature unknown
    pass

def scalar_compare(*args, **kwargs): # real signature unknown
    pass

def slice_canonize(*args, **kwargs): # real signature unknown
    """ Convert slice to canonical bounded form. """
    pass

def slice_getitem(*args, **kwargs): # real signature unknown
    pass

def slice_get_indices_ex(*args, **kwargs): # real signature unknown
    """
    Get (start, stop, step, length) tuple for a slice.
    
        If `objlen` is not specified, slice must be bounded, otherwise the result
        will be wrong.
    """
    pass

def slice_len(*args, **kwargs): # real signature unknown
    """
    Get length of a bounded slice.
    
        The slice must not have any "open" bounds that would create dependency on
        container size, i.e.:
        - if ``s.step is None or s.step > 0``, ``s.stop`` is not ``None``
        - if ``s.step < 0``, ``s.start`` is not ``None``
    
        Otherwise, the result is unreliable.
    """
    pass

def string_array_replace_from_nan_rep(*args, **kwargs): # real signature unknown
    """ replace the values in the array with replacement if they are nan_rep; return the same array """
    pass

def time64_to_datetime(*args, **kwargs): # real signature unknown
    pass

def to_datetime(*args, **kwargs): # real signature unknown
    pass

def to_object_array(*args, **kwargs): # real signature unknown
    pass

def to_object_array_tuples(*args, **kwargs): # real signature unknown
    pass

def to_timestamp(*args, **kwargs): # real signature unknown
    pass

def try_parse_dates(*args, **kwargs): # real signature unknown
    pass

def try_parse_datetime_components(*args, **kwargs): # real signature unknown
    pass

def try_parse_date_and_time(*args, **kwargs): # real signature unknown
    pass

def try_parse_year_month_day(*args, **kwargs): # real signature unknown
    pass

def tuples_to_object_array(*args, **kwargs): # real signature unknown
    pass

def values_from_object(*args, **kwargs): # real signature unknown
    """ return my values or the object if we are say an ndarray """
    pass

def vec_binop(*args, **kwargs): # real signature unknown
    pass

def vec_compare(*args, **kwargs): # real signature unknown
    pass

def write_csv_rows(*args, **kwargs): # real signature unknown
    pass

# classes

class AxisProperty(object):
    # no doc
    def __delete__(self, obj): # real signature unknown; restored from __doc__
        """ descr.__delete__(obj) """
        pass

    def __get__(self, obj, type=None): # real signature unknown; restored from __doc__
        """ descr.__get__(obj[, type]) -> value """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __set__(self, obj, value): # real signature unknown; restored from __doc__
        """ descr.__set__(obj, value) """
        pass


class BlockPlacement(object):
    # no doc
    def add(self, *args, **kwargs): # real signature unknown
        pass

    def append(self, *args, **kwargs): # real signature unknown
        pass

    def delete(self, *args, **kwargs): # real signature unknown
        pass

    def isin(self, *args, **kwargs): # real signature unknown
        pass

    def sub(self, *args, **kwargs): # real signature unknown
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ x.__str__() <==> str(x) """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    as_array = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    as_slice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    indexer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_slice_like = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class BlockSlider(object):
    """ Only capable of sliding on axis=0 """
    def move(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    blocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    frame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    idx_slider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nblocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class cache_readonly(object):
    # no doc
    def __call__(self, *more): # real signature unknown; restored from __doc__
        """ x.__call__(...) <==> x(...) """
        pass

    def __delete__(self, obj): # real signature unknown; restored from __doc__
        """ descr.__delete__(obj) """
        pass

    def __get__(self, obj, type=None): # real signature unknown; restored from __doc__
        """ descr.__get__(obj[, type]) -> value """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __set__(self, obj, value): # real signature unknown; restored from __doc__
        """ descr.__set__(obj, value) """
        pass

    allow_setting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    func = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class InvalidApply(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __qualname__ = 'InvalidApply'


class LooseVersion(__distutils_version.Version):
    """
    Version numbering for anarchists and software realists.
        Implements the standard interface for version number classes as
        described above.  A version number consists of a series of numbers,
        separated by either periods or strings of letters.  When comparing
        version numbers, the numeric components will be compared
        numerically, and the alphabetic components lexically.  The following
        are all valid version numbers, in no particular order:
    
            1.5.1
            1.5.2b2
            161
            3.10a
            8.02
            3.4j
            1996.07.12
            3.2.pl0
            3.1.1.6
            2g6
            11g
            0.960923
            2.2beta29
            1.13++
            5.5.kw
            2.0b1pl0
    
        In fact, there is no such thing as an invalid version number under
        this scheme; the rules for comparison are simple and predictable,
        but may not always give the results you want (for some definition
        of "want").
    """
    def parse(self, *args, **kwargs): # real signature unknown
        pass

    def __cmp__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        pass

    component_re = None # (!) real value is ''


class Reducer(object):
    """
    Performs generic reduction operation on a C or Fortran-contiguous ndarray
        while avoiding ndarray construction overhead
    """
    def get_result(self, *args, **kwargs): # real signature unknown
        pass

    def _check_dummy(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class SeriesBinGrouper(object):
    """ Performs grouping operation according to bin edges, rather than labels """
    def get_result(self, *args, **kwargs): # real signature unknown
        pass

    def _check_dummy(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    arr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bins = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy_arr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy_index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ityp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    typ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class SeriesGrouper(object):
    """
    Performs generic grouping operation while avoiding ndarray construction
        overhead
    """
    def get_result(self, *args, **kwargs): # real signature unknown
        pass

    def _check_dummy(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    arr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy_arr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy_index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ityp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    labels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    typ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Slider(object):
    """ Only handles contiguous data for now """
    def advance(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def set_length(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class _PandasNull(object):
    # no doc
    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
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


# variables with complex values

pandas_null = None # (!) real value is ''

_TYPE_MAP = {
    'M': 'datetime64',
    'S': 'string',
    'U': 'unicode',
    'b': 'boolean',
    'bool': 'boolean',
    'c': 'complex',
    'categorical': 'categorical',
    'category': 'categorical',
    'complex128': 'complex',
    'complex256': 'complex',
    'datetime64[ns]': 'datetime64',
    'f': 'floating',
    'float128': 'floating',
    'float16': 'floating',
    'float32': 'floating',
    'float64': 'floating',
    'i': 'integer',
    'int16': 'integer',
    'int32': 'integer',
    'int64': 'integer',
    'int8': 'integer',
    'm': 'timedelta64',
    'string': 'string',
    'timedelta64[ns]': 'timedelta64',
    'u': 'integer',
    'uint16': 'integer',
    'uint32': 'integer',
    'uint64': 'integer',
    'uint8': 'integer',
    'unicode': 'unicode',
}

__pyx_capi__ = {
    'is_null_datetimelike': None, # (!) real value is ''
}

__test__ = {
    u'item_from_zerodim (line 322)': u"\n    If the value is a zerodim array, return the item it contains.\n\n    Examples\n    --------\n    >>> item_from_zerodim(1)\n    1\n    >>> item_from_zerodim('foobar')\n    'foobar'\n    >>> item_from_zerodim(np.array(1))\n    1\n    >>> item_from_zerodim(np.array([1]))\n    array([1])\n\n    ",
}

