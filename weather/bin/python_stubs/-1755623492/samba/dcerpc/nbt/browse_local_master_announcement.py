# encoding: utf-8
# module samba.dcerpc.nbt
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/nbt.so
# by generator 1.138
""" nbt DCE/RPC """

# imports
import dcerpc as __dcerpc
import talloc as __talloc


class browse_local_master_announcement(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    BroMajorVer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    BroMinorVer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    OSMajor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    OSMinor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Periodicity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ServerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ServerType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Signature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    UpdateCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



