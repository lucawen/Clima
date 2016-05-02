# encoding: utf-8
# module ntdb
# from /usr/lib/python2.7/dist-packages/ntdb.so
# by generator 1.138
""" NTDB is a simple key-value database similar to GDBM that supports multiple writers. """
# no imports

# Variables with simple values

ALLOW_NESTING = 256

CONVERT = 16

DEFAULT = 0

INSERT = 2
INTERNAL = 2

MODIFY = 3

NOLOCK = 4
NOMMAP = 8
NOSYNC = 64

REPLACE = 1

SEQNUM = 128

__docformat__ = 'restructuredText'

__version__ = '1.0'

# functions

def open(name, hash_size=0, ntdb_flags=None, flags=None, mode=0600): # real signature unknown; restored from __doc__
    """
    open(name, hash_size=0, ntdb_flags=NTDB_DEFAULT, flags=O_RDWR, mode=0600)
    Open a NTDB file.
    """
    pass

# classes

class Ntdb(object):
    """ A NTDB file """
    def add_flag(self, flag): # real signature unknown; restored from __doc__
        """ S.add_flag(flag) -> None """
        pass

    def append(self, key, value): # real signature unknown; restored from __doc__
        """
        S.append(key, value) -> None
        Append data to an existing key.
        """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """
        S.clear() -> None
        Wipe the entire database.
        """
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def delete(self, key): # real signature unknown; restored from __doc__
        """
        S.delete(key) -> None
        Delete an entry.
        """
        pass

    def enable_seqnum(self): # real signature unknown; restored from __doc__
        """ S.enable_seqnum() -> None """
        pass

    def firstkey(self): # real signature unknown; restored from __doc__
        """
        S.firstkey() -> data
        Return the first key in this database.
        """
        pass

    def get(self, key): # real signature unknown; restored from __doc__
        """
        S.get(key) -> value
        Fetch a value.
        """
        pass

    def has_key(self, key): # real signature unknown; restored from __doc__
        """
        S.has_key(key) -> None
        Check whether key exists in this database.
        """
        pass

    def iterkeys(self): # real signature unknown; restored from __doc__
        """ S.iterkeys() -> iterator """
        pass

    def lock_all(self, *args, **kwargs): # real signature unknown
        pass

    def nextkey(self, key): # real signature unknown; restored from __doc__
        """
        S.nextkey(key) -> data
        Return the next key in this database.
        """
        pass

    def read_lock_all(self, *args, **kwargs): # real signature unknown
        pass

    def read_unlock_all(self, *args, **kwargs): # real signature unknown
        pass

    def remove_flag(self, flag): # real signature unknown; restored from __doc__
        """ S.remove_flag(flag) -> None """
        pass

    def store(self, key, data, flag=None): # real signature unknown; restored from __doc__
        """ S.store(key, data, flag=REPLACE) -> NoneStore data. """
        pass

    def transaction_cancel(self): # real signature unknown; restored from __doc__
        """
        S.transaction_cancel() -> None
        Cancel the currently active transaction.
        """
        pass

    def transaction_commit(self): # real signature unknown; restored from __doc__
        """
        S.transaction_commit() -> None
        Commit the currently active transaction.
        """
        pass

    def transaction_prepare_commit(self): # real signature unknown; restored from __doc__
        """
        S.transaction_prepare_commit() -> None
        Prepare to commit the currently active transaction
        """
        pass

    def transaction_start(self): # real signature unknown; restored from __doc__
        """
        S.transaction_start() -> None
        Start a new transaction.
        """
        pass

    def unlock_all(self, *args, **kwargs): # real signature unknown
        pass

    def __delitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__delitem__(y) <==> del x[y] """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setitem__(self, i, y): # real signature unknown; restored from __doc__
        """ x.__setitem__(i, y) <==> x[i]=y """
        pass

    filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The filename of this NTDB file."""

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    seqnum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



