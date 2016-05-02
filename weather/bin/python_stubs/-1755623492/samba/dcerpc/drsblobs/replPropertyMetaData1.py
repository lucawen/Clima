# encoding: utf-8
# module samba.dcerpc.drsblobs
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/drsblobs.so
# by generator 1.138
""" drsblobs DCE/RPC """

# imports
import dcerpc as __dcerpc
import talloc as __talloc


class replPropertyMetaData1(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    attid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    local_usn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    originating_change_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    originating_invocation_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    originating_usn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



