# encoding: utf-8
# module samba.dcerpc.winbind
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/winbind.so
# by generator 1.138
""" winbind DCE/RPC """

# imports
import dcerpc as __dcerpc


# Variables with simple values

WINBIND_IDMAP_LEVEL_SIDS_TO_XIDS = 1

WINBIND_IDMAP_LEVEL_XIDS_TO_SIDS = 2

# no functions
# classes

class winbind(__dcerpc.ClientConnection):
    """
    winbind(binding, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    """
    def DsrUpdateReadOnlyServerDnsRecords(self, site_name, dns_ttl, dns_names): # real signature unknown; restored from __doc__
        """ S.DsrUpdateReadOnlyServerDnsRecords(site_name, dns_ttl, dns_names) -> dns_names """
        pass

    def get_idmap(self, level, ids): # real signature unknown; restored from __doc__
        """ S.get_idmap(level, ids) -> ids """
        pass

    def information(self): # real signature unknown; restored from __doc__
        """ S.information() -> None """
        pass

    def remote_control(self): # real signature unknown; restored from __doc__
        """ S.remote_control() -> None """
        pass

    def SamLogon(self, logon_level, logon, validation_level): # real signature unknown; restored from __doc__
        """ S.SamLogon(logon_level, logon, validation_level) -> (validation, authoritative) """
        pass

    def __init__(self, binding, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


