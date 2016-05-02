# encoding: utf-8
# module pandas.hashtable
# from /usr/local/lib/python2.7/dist-packages/pandas/hashtable.so
# by generator 1.138
# no doc

# imports
import numpy as np # /usr/local/lib/python2.7/dist-packages/numpy/__init__.pyc
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>

# Variables with simple values

nan = nan

_SIZE_HINT_LIMIT = 1048583

# functions

def duplicated_int64(*args, **kwargs): # real signature unknown
    pass

def mode_int64(*args, **kwargs): # real signature unknown
    pass

def mode_object(*args, **kwargs): # real signature unknown
    pass

def unique_label_indices(*args, **kwargs): # real signature unknown
    """
    indices of the first occurrences of the unique labels
        *excluding* -1. equivelent to:
            np.unique(labels, return_index=True)[1]
    """
    pass

def value_count_object(*args, **kwargs): # real signature unknown
    pass

def value_count_scalar64(*args, **kwargs): # real signature unknown
    pass

# classes

class na_sentinel:
    """ The most base type """
    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ default object formatter """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ helper for pickle """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ helper for pickle """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """
        __sizeof__() -> int
        size of object in memory, in bytes
        """
        return 0

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    @classmethod
    def __subclasshook__(cls, *args, **kwargs): # real signature unknown
        """
        Abstract classes can override this to customize issubclass().
        
        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        pass

    __class__ = type


class Factorizer(object):
    # no doc
    def factorize(self, np_array, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Factorize values with nans replaced by na_sentinel
                >>> factorize(np.array([1,2,np.nan], dtype='O'), na_sentinel=20)
                array([ 0,  1, 20])
        """
        pass

    def get_count(self, *args, **kwargs): # real signature unknown
        pass

    def unique(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    table = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uniques = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class HashTable(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class Float64HashTable(HashTable):
    # no doc
    def factorize(self, *args, **kwargs): # real signature unknown
        pass

    def get_item(self, *args, **kwargs): # real signature unknown
        pass

    def get_labels(self, *args, **kwargs): # real signature unknown
        pass

    def lookup(self, *args, **kwargs): # real signature unknown
        pass

    def map_locations(self, *args, **kwargs): # real signature unknown
        pass

    def set_item(self, *args, **kwargs): # real signature unknown
        pass

    def unique(self, *args, **kwargs): # real signature unknown
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class Float64Vector(object):
    # no doc
    def to_array(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class Int64Factorizer(object):
    # no doc
    def factorize(self, *args, **kwargs): # real signature unknown
        pass

    def get_count(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    table = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uniques = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Int64HashTable(HashTable):
    # no doc
    def factorize(self, *args, **kwargs): # real signature unknown
        pass

    def get_item(self, *args, **kwargs): # real signature unknown
        pass

    def get_iter_test(self, *args, **kwargs): # real signature unknown
        pass

    def get_labels(self, *args, **kwargs): # real signature unknown
        pass

    def get_labels_groupby(self, *args, **kwargs): # real signature unknown
        pass

    def lookup(self, *args, **kwargs): # real signature unknown
        pass

    def map(self, *args, **kwargs): # real signature unknown
        pass

    def map_locations(self, *args, **kwargs): # real signature unknown
        pass

    def set_item(self, *args, **kwargs): # real signature unknown
        pass

    def unique(self, *args, **kwargs): # real signature unknown
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class Int64Vector(object):
    # no doc
    def to_array(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class ObjectVector(object):
    # no doc
    def to_array(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class PyObjectHashTable(HashTable):
    # no doc
    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def get_item(self, *args, **kwargs): # real signature unknown
        pass

    def get_iter_test(self, *args, **kwargs): # real signature unknown
        pass

    def get_labels(self, *args, **kwargs): # real signature unknown
        pass

    def lookup(self, *args, **kwargs): # real signature unknown
        pass

    def map_locations(self, *args, **kwargs): # real signature unknown
        pass

    def set_item(self, *args, **kwargs): # real signature unknown
        pass

    def unique(self, *args, **kwargs): # real signature unknown
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class StringHashTable(HashTable):
    # no doc
    def factorize(self, *args, **kwargs): # real signature unknown
        pass

    def get_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def get_item(self, *args, **kwargs): # real signature unknown
        pass

    def get_iter_test(self, *args, **kwargs): # real signature unknown
        pass

    def set_item(self, *args, **kwargs): # real signature unknown
        pass

    def unique(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __pyx_vtable__ = None # (!) real value is ''


# variables with complex values

__test__ = {
    u'Factorizer.factorize (line 811)': u"\n        Factorize values with nans replaced by na_sentinel\n        >>> factorize(np.array([1,2,np.nan], dtype='O'), na_sentinel=20)\n        array([ 0,  1, 20])\n        ",
}

