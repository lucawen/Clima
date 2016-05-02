# encoding: utf-8
# module pandas._sparse
# from /usr/local/lib/python2.7/dist-packages/pandas/_sparse.so
# by generator 1.138
# no doc

# imports
import operator as operator # <module 'operator' (built-in)>
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import sys as sys # <module 'sys' (built-in)>
import numpy as np # /usr/local/lib/python2.7/dist-packages/numpy/__init__.pyc

# functions

def get_blocks(*args, **kwargs): # real signature unknown
    pass

def get_reindexer(*args, **kwargs): # real signature unknown
    pass

def reindex_integer(*args, **kwargs): # real signature unknown
    pass

def sparse_add(*args, **kwargs): # real signature unknown
    pass

def sparse_div(*args, **kwargs): # real signature unknown
    pass

def sparse_floordiv(*args, **kwargs): # real signature unknown
    pass

def sparse_mul(*args, **kwargs): # real signature unknown
    pass

def sparse_nanadd(*args, **kwargs): # real signature unknown
    pass

def sparse_nandiv(*args, **kwargs): # real signature unknown
    pass

def sparse_nanfloordiv(*args, **kwargs): # real signature unknown
    pass

def sparse_nanmul(*args, **kwargs): # real signature unknown
    pass

def sparse_nanpow(*args, **kwargs): # real signature unknown
    pass

def sparse_nanrdiv(*args, **kwargs): # real signature unknown
    pass

def sparse_nanrfloordiv(*args, **kwargs): # real signature unknown
    pass

def sparse_nanrpow(*args, **kwargs): # real signature unknown
    pass

def sparse_nanrsub(*args, **kwargs): # real signature unknown
    pass

def sparse_nanrtruediv(*args, **kwargs): # real signature unknown
    pass

def sparse_nansub(*args, **kwargs): # real signature unknown
    pass

def sparse_nantruediv(*args, **kwargs): # real signature unknown
    pass

def sparse_pow(*args, **kwargs): # real signature unknown
    pass

def sparse_rdiv(*args, **kwargs): # real signature unknown
    pass

def sparse_rfloordiv(*args, **kwargs): # real signature unknown
    pass

def sparse_rpow(*args, **kwargs): # real signature unknown
    pass

def sparse_rsub(*args, **kwargs): # real signature unknown
    pass

def sparse_rtruediv(*args, **kwargs): # real signature unknown
    pass

def sparse_sub(*args, **kwargs): # real signature unknown
    pass

def sparse_truediv(*args, **kwargs): # real signature unknown
    pass

# classes

class SparseIndex(object):
    """ Abstract superclass for sparse index types """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class BlockIndex(SparseIndex):
    """
    Object for holding block-based sparse indexing information
    
        Parameters
        ----------
    """
    def check_integrity(self, *args, **kwargs): # real signature unknown
        """
        Check:
                - Locations are in ascending order
                - No overlapping blocks
                - Blocks to not start after end of index, nor extend beyond end
        """
        pass

    def equals(self, *args, **kwargs): # real signature unknown
        pass

    def intersect(self, *args, **kwargs): # real signature unknown
        """
        Intersect two BlockIndex objects
        
                Parameters
                ----------
        
                Returns
                -------
                intersection : BlockIndex
        """
        pass

    def lookup(self, *args, **kwargs): # real signature unknown
        """ Returns -1 if not found """
        pass

    def make_union(self, *args, **kwargs): # real signature unknown
        """
        Combine together two BlockIndex objects, accepting indices if contained
                in one or the other
        
                Parameters
                ----------
                other : SparseIndex
        
                Notes
                -----
                union is a protected keyword in Cython, hence make_union
        
                Returns
                -------
                union : BlockIndex
        """
        pass

    def put(self, *args, **kwargs): # real signature unknown
        pass

    def reindex(self, *args, **kwargs): # real signature unknown
        pass

    def take(self, *args, **kwargs): # real signature unknown
        pass

    def to_block_index(self, *args, **kwargs): # real signature unknown
        pass

    def to_int_index(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    blengths = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    blocs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nblocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ngaps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    npoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class BlockMerge(object):
    """
    Object-oriented approach makes sharing state between recursive functions a
        lot easier and reduces code duplication
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class BlockIntersection(BlockMerge):
    """ not done yet """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class BlockUnion(BlockMerge):
    """
    Object-oriented approach makes sharing state between recursive functions a
        lot easier and reduces code duplication
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class IntIndex(SparseIndex):
    """
    Object for holding exact integer sparse indexing information
    
        Parameters
        ----------
        length : integer
        indices : array-like
            Contains integers corresponding to
    """
    def check_integrity(self, *args, **kwargs): # real signature unknown
        """
        Only need be strictly ascending and nothing less than 0 or greater than
                totall ength
        """
        pass

    def equals(self, *args, **kwargs): # real signature unknown
        pass

    def intersect(self, *args, **kwargs): # real signature unknown
        pass

    def lookup(self, *args, **kwargs): # real signature unknown
        pass

    def make_union(self, *args, **kwargs): # real signature unknown
        pass

    def put(self, *args, **kwargs): # real signature unknown
        pass

    def reindex(self, *args, **kwargs): # real signature unknown
        pass

    def take(self, *args, **kwargs): # real signature unknown
        pass

    def to_block_index(self, *args, **kwargs): # real signature unknown
        pass

    def to_int_index(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    indices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ngaps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    npoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


# variables with complex values

__test__ = {}

