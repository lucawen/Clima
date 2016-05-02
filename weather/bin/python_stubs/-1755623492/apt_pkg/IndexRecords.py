# encoding: utf-8
# module apt_pkg
# from /usr/lib/python2.7/dist-packages/apt_pkg.so
# by generator 1.138
"""
Classes and functions wrapping the apt-pkg library.

The apt_pkg module provides several classes and functions for accessing
the functionality provided by the apt-pkg library. Typical uses might
include reading APT index files and configuration files and installing
or removing packages.
"""
# no imports

from object import object

class IndexRecords(object):
    """
    IndexRecords()
    
    Representation of a Release file.
    """
    def get_dist(self): # real signature unknown; restored from __doc__
        """
        get_dist() -> str
        
        Return a distribution set in the release file.
        """
        return ""

    def load(self, filename): # real signature unknown; restored from __doc__
        """
        load(filename: str)
        
        Load the file given by filename.
        """
        pass

    def lookup(self, key): # real signature unknown; restored from __doc__
        """
        lookup(key: str) -> (HashString, int)
        
        Look up the filename given by 'key' and return a tuple (hash, size),
        where the first element 'hash' is an apt_pkg.HashString object
        and the second element 'size' is an int object.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


