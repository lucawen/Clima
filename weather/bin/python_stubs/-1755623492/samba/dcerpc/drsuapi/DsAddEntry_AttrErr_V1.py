# encoding: utf-8
# module samba.dcerpc.drsuapi
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/drsuapi.so
# by generator 1.138
""" drsuapi DCE/RPC """

# imports
import dcerpc as __dcerpc
import talloc as __talloc


class DsAddEntry_AttrErr_V1(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    attid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    attr_val = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dsid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    extended_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    extended_err = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_val_returned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    problem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


