# encoding: utf-8
# module samba.dcerpc.nbt
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/nbt.so
# by generator 1.138
""" nbt DCE/RPC """

# imports
import dcerpc as __dcerpc
import talloc as __talloc


class NETLOGON_SAM_LOGON_RESPONSE_NT40(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ndr_pack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_pack(object) -> blob
        NDR pack
        """
        pass

    def __ndr_print__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_print(object) -> None
        NDR print
        """
        pass

    def __ndr_unpack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_unpack(class, blob, allow_remaining=False) -> None
        NDR unpack
        """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    command = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    domain_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lm20_token = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lmnt_token = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nt_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pdc_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



