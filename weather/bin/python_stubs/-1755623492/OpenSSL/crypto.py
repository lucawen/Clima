# encoding: utf-8
# module OpenSSL.crypto
# from /usr/lib/python2.7/dist-packages/OpenSSL/crypto.so
# by generator 1.138
"""
Main file of crypto sub module.
See the file RATIONALE for a short explanation of why this module was written.
"""
# no imports

# Variables with simple values

FILETYPE_ASN1 = 2
FILETYPE_PEM = 1
FILETYPE_TEXT = 58

TYPE_DSA = 116
TYPE_RSA = 6

# functions

def dump_certificate(*args, **kwargs): # real signature unknown
    """
    Dump a certificate to a buffer
    
    @param type: The file type (one of FILETYPE_PEM, FILETYPE_ASN1)
    @param cert: The certificate to dump
    @return: The buffer with the dumped certificate in
    """
    pass

def dump_certificate_request(*args, **kwargs): # real signature unknown
    """
    Dump a certificate request to a buffer
    
    @param type: The file type (one of FILETYPE_PEM, FILETYPE_ASN1)
                 req  - The certificate request to dump
    @return: The buffer with the dumped certificate request in
    """
    pass

def dump_privatekey(*args, **kwargs): # real signature unknown
    """
    Dump a private key to a buffer
    
    @param type: The file type (one of FILETYPE_PEM, FILETYPE_ASN1)
    @param pkey: The PKey to dump
    @param cipher: (optional) if encrypted PEM format, the cipher to
                   use
    @param passphrase - (optional) if encrypted PEM format, this can be either
                        the passphrase to use, or a callback for providing the
                        passphrase.
    @return: The buffer with the dumped key in
    @rtype: C{str}
    """
    pass

def load_certificate(*args, **kwargs): # real signature unknown
    """
    Load a certificate from a buffer
    
    @param type: The file type (one of FILETYPE_PEM, FILETYPE_ASN1)
                 buffer - The buffer the certificate is stored in
    @return: The X509 object
    """
    pass

def load_certificate_request(*args, **kwargs): # real signature unknown
    """
    Load a certificate request from a buffer
    
    @param type: The file type (one of FILETYPE_PEM, FILETYPE_ASN1)
                 buffer - The buffer the certificate request is stored in
    @return: The X509Req object
    """
    pass

def load_crl(*args, **kwargs): # real signature unknown
    """
    Load a certificate revocation list from a buffer
    
    @param type: The file type (one of FILETYPE_PEM, FILETYPE_ASN1)
    @param buffer: The buffer the CRL is stored in
    
    @return: The PKey object
    """
    pass

def load_pkcs12(*args, **kwargs): # real signature unknown
    """
    Load a PKCS12 object from a buffer
    
    @param buffer: The buffer the certificate is stored in
                   passphrase (Optional) - The password to decrypt the PKCS12 lump
    @returns: The PKCS12 object
    """
    pass

def load_pkcs7_data(*args, **kwargs): # real signature unknown
    """
    Load pkcs7 data from a buffer
    
    @param type: The file type (one of FILETYPE_PEM or FILETYPE_ASN1)
                 buffer - The buffer with the pkcs7 data.
    @return: The PKCS7 object
    """
    pass

def load_privatekey(*args, **kwargs): # real signature unknown
    """
    Load a private key from a buffer
    
    @param type: The file type (one of FILETYPE_PEM, FILETYPE_ASN1)
    @param buffer: The buffer the key is stored in
    @param passphrase: (optional) if encrypted PEM format, this can be
                       either the passphrase to use, or a callback for
                       providing the passphrase.
    
    @return: The PKey object
    """
    pass

def sign(*args, **kwargs): # real signature unknown
    """
    Sign data with a digest
    
    @param pkey: Pkey to sign with
    @param data: data to be signed
    @param digest: message digest to use
    @return: signature
    """
    pass

def verify(*args, **kwargs): # real signature unknown
    """
    Verify a signature
    
    @param cert: signing certificate (X509 object)
    @param signature: signature returned by sign function
    @param data: data to be verified
    @param digest: message digest to use
    @return: None if the signature is correct, raise exception otherwise
    """
    pass

def X509_verify_cert_error_string(*args, **kwargs): # real signature unknown
    """
    Get X509 verify certificate error string.
    
    @param errnum: The error number.
    @return: Error string as a Python string
    """
    pass

def _exception_from_error_queue(*args, **kwargs): # real signature unknown
    """ Raise an exception from the current OpenSSL error queue. """
    pass

# classes

class CRL(object):
    """
    CRL() -> CRL instance
    
    Create a new empty CRL object.
    
    @returns: The CRL object
    """
    def add_revoked(self, *args, **kwargs): # real signature unknown
        """
        Add a revoked (by value not reference) to the CRL structure
        
        @param cert: The new revoked.
        @type cert: L{X509}
        @return: None
        """
        pass

    def export(self, cert, key, type=None, days=None): # real signature unknown; restored from __doc__
        """
        export(cert, key[, type[, days]]) -> export a CRL as a string
        
        @param cert: Used to sign CRL.
        @type cert: L{X509}
        @param key: Used to sign CRL.
        @type key: L{PKey}
        @param type: The export format, either L{FILETYPE_PEM}, L{FILETYPE_ASN1}, or L{FILETYPE_TEXT}.
        @param days: The number of days until the next update of this CRL.
        @type days: L{int}
        @return: L{str}
        """
        pass

    def get_revoked(self, *args, **kwargs): # real signature unknown
        """
        Return revoked portion of the CRL structure (by value
        not reference).
        
        @return: A tuple of Revoked objects.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class Error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class NetscapeSPKIType(object):
    """
    NetscapeSPKI([enc]) -> NetscapeSPKI instance
    
    @param enc: Base64 encoded NetscapeSPKI object.
    @type enc: C{str}
    @return: The NetscapeSPKI object
    """
    def b64_encode(self, *args, **kwargs): # real signature unknown
        """
        Generate a base64 encoded string from an SPKI
        
        @return: The base64 encoded string
        """
        pass

    def get_pubkey(self, *args, **kwargs): # real signature unknown
        """
        Get the public key of the certificate
        
        @return: The public key
        """
        pass

    def set_pubkey(self, *args, **kwargs): # real signature unknown
        """
        Set the public key of the certificate
        
        @param pkey: The public key
        @return: None
        """
        pass

    def sign(self, *args, **kwargs): # real signature unknown
        """
        Sign the certificate request using the supplied key and digest
        
        @param pkey: The key to sign with
        @param digest: The message digest to use
        @return: None
        """
        pass

    def verify(self, *args, **kwargs): # real signature unknown
        """
        Verifies a certificate request using the supplied public key
        
        @param key: a public key
        @return: True if the signature is correct.
        @raise OpenSSL.crypto.Error: If the signature is invalid or there is a
            problem verifying the signature.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


NetscapeSPKI = NetscapeSPKIType


class PKCS12Type(object):
    """
    PKCS12() -> PKCS12 instance
    
    Create a new empty PKCS12 object.
    
    @returns: The PKCS12 object
    """
    def export(self, passphrase=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        export([passphrase=None][, friendly_name=None][, iter=2048][, maciter=1]
        Dump a PKCS12 object as a string.  See also "man PKCS12_create".
        
        @param passphrase: used to encrypt the PKCS12
        @type passphrase: L{str}
        @param iter: How many times to repeat the encryption
        @type iter: L{int}
        @param maciter: How many times to repeat the MAC
        @type maciter: L{int}
        @return: The string containing the PKCS12
        """
        pass

    def get_ca_certificates(self, *args, **kwargs): # real signature unknown
        """
        Return CA certificates within of the PKCS12 object
        
        @return: A newly created tuple containing the CA certificates in the chain,
                 if any are present, or None if no CA certificates are present.
        """
        pass

    def get_certificate(self, *args, **kwargs): # real signature unknown
        """
        Return certificate portion of the PKCS12 structure
        
        @return: X509 object containing the certificate
        """
        pass

    def get_friendlyname(self, *args, **kwargs): # real signature unknown
        """
        Return friendly name portion of the PKCS12 structure
        
        @returns: String containing the friendlyname
        """
        pass

    def get_privatekey(self, *args, **kwargs): # real signature unknown
        """
        Return private key portion of the PKCS12 structure
        
        @returns: PKey object containing the private key
        """
        pass

    def set_ca_certificates(self, *args, **kwargs): # real signature unknown
        """
        Replace or set the CA certificates withing the PKCS12 object.
        
        @param cacerts: The new CA certificates.
        @type cacerts: Iterable of L{X509} or L{NoneType}
        @return: None
        """
        pass

    def set_certificate(self, *args, **kwargs): # real signature unknown
        """
        Replace the certificate portion of the PKCS12 structure
        
        @param cert: The new certificate.
        @type cert: L{X509} or L{NoneType}
        @return: None
        """
        pass

    def set_friendlyname(self, *args, **kwargs): # real signature unknown
        """
        Replace or set the certificate portion of the PKCS12 structure
        
        @param name: The new friendly name.
        @type name: L{str}
        @return: None
        """
        pass

    def set_privatekey(self, *args, **kwargs): # real signature unknown
        """
        Replace or set the certificate portion of the PKCS12 structure
        
        @param pkey: The new private key.
        @type pkey: L{PKey}
        @return: None
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


PKCS12 = PKCS12Type


class PKCS7Type(object):
    # no doc
    def get_type_name(self, *args, **kwargs): # real signature unknown
        """
        Returns the type name of the PKCS7 structure
        
        @return: A string with the typename
        """
        pass

    def type_is_data(self, *args, **kwargs): # real signature unknown
        """
        Check if this NID_pkcs7_data object
        
        @return: True if the PKCS7 is of type data
        """
        pass

    def type_is_enveloped(self, *args, **kwargs): # real signature unknown
        """
        Check if this NID_pkcs7_enveloped object
        
        @returns: True if the PKCS7 is of type enveloped
        """
        pass

    def type_is_signed(self, *args, **kwargs): # real signature unknown
        """
        Check if this NID_pkcs7_signed object
        
        @return: True if the PKCS7 is of type signed
        """
        pass

    def type_is_signedAndEnveloped(self, *args, **kwargs): # real signature unknown
        """
        Check if this NID_pkcs7_signedAndEnveloped object
        
        @returns: True if the PKCS7 is of type signedAndEnveloped
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class PKeyType(object):
    """
    PKey() -> PKey instance
    
    Create a new PKey object.
    
    @return: The PKey object
    """
    def bits(self, *args, **kwargs): # real signature unknown
        """
        Returns the number of bits of the key
        
        @return: The number of bits of the key.
        """
        pass

    def check(self, *args, **kwargs): # real signature unknown
        """
        Check the consistency of an RSA private key.
        
        @return: True if key is consistent.
        @raise Error: if the key is inconsistent.
        @raise TypeError: if the key is of a type which cannot be checked.
            Only RSA keys can currently be checked.
        """
        pass

    def generate_key(self, *args, **kwargs): # real signature unknown
        """
        Generate a key of a given type, with a given number of a bits
        
        @param type: The key type (TYPE_RSA or TYPE_DSA)
        @param bits: The number of bits
        @return: None
        """
        pass

    def type(self, *args, **kwargs): # real signature unknown
        """
        Returns the type of the key
        
        @return: The type of the key.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


PKey = PKeyType


class Revoked(object):
    """
    Revoked() -> Revoked instance
    
    Create a new empty Revoked object.
    
    @returns: The Revoked object
    """
    def all_reasons(self, *args, **kwargs): # real signature unknown
        """
        Return a list of all the supported reason strings.
        
        @return: A list of reason strings.
        """
        pass

    def get_reason(self, *args, **kwargs): # real signature unknown
        """
        Return the reason of a Revoked object.
        
        @return: The reason as a string
        """
        pass

    def get_rev_date(self, *args, **kwargs): # real signature unknown
        """
        Retrieve the revocation date
        
        @return: A string giving the timestamp, in the format:
        
                         YYYYMMDDhhmmssZ
                         YYYYMMDDhhmmss+hhmm
                         YYYYMMDDhhmmss-hhmm
        """
        pass

    def get_serial(self, *args, **kwargs): # real signature unknown
        """
        Return the serial number of a Revoked structure
        
        @return: The serial number as a string
        """
        pass

    def set_reason(self, *args, **kwargs): # real signature unknown
        """
        Set the reason of a Revoked object.
        
        @param reason: The reason string.
        @type reason: L{str}
        @return: None
        """
        pass

    def set_rev_date(self, *args, **kwargs): # real signature unknown
        """
        Set the revocation timestamp
        
        @param when: A string giving the timestamp, in the format:
        
                         YYYYMMDDhhmmssZ
                         YYYYMMDDhhmmss+hhmm
                         YYYYMMDDhhmmss-hhmm
        
        @return: None
        """
        pass

    def set_serial(self, *args, **kwargs): # real signature unknown
        """
        Set the serial number of a revoked Revoked structure
        
        @param hex_str: The new serial number.
        @type hex_str: L{str}
        @return: None
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class X509Type(object):
    """
    X509() -> X509 instance
    
    Create a new X509 object.
    
    @returns: The X509 object
    """
    def add_extensions(self, *args, **kwargs): # real signature unknown
        """
        Add extensions to the certificate.
        
        @param extensions: a sequence of X509Extension objects
        @return: None
        """
        pass

    def digest(self, *args, **kwargs): # real signature unknown
        """
        Return the digest of the X509 object.
        
        @return: The digest of the object
        """
        pass

    def get_extension(self, *args, **kwargs): # real signature unknown
        """
        Get a specific extension of the certificate by index.
        
        @param index: The index of the extension to retrieve.
        @return: The X509Extension object at the specified index.
        """
        pass

    def get_extension_count(self, *args, **kwargs): # real signature unknown
        """
        Get the number of extensions on the certificate.
        
        @return: Number of extensions as a Python integer
        """
        pass

    def get_issuer(self, *args, **kwargs): # real signature unknown
        """
        Create an X509Name object for the issuer of the certificate
        
        @return: An X509Name object
        """
        pass

    def get_notAfter(self, *args, **kwargs): # real signature unknown
        """
        Retrieve the time stamp for when the certificate stops being valid
        
        @return: A string giving the timestamp, in the format:
        
                         YYYYMMDDhhmmssZ
                         YYYYMMDDhhmmss+hhmm
                         YYYYMMDDhhmmss-hhmm
                   or None if there is no value set.
        """
        pass

    def get_notBefore(self, *args, **kwargs): # real signature unknown
        """
        Retrieve the time stamp for when the certificate starts being valid
        
        @return: A string giving the timestamp, in the format:
        
                         YYYYMMDDhhmmssZ
                         YYYYMMDDhhmmss+hhmm
                         YYYYMMDDhhmmss-hhmm
                   or None if there is no value set.
        """
        pass

    def get_pubkey(self, *args, **kwargs): # real signature unknown
        """
        Get the public key of the certificate
        
        @return: The public key
        """
        pass

    def get_serial_number(self, *args, **kwargs): # real signature unknown
        """
        Return serial number of the certificate
        
        @return: Serial number as a Python integer
        """
        pass

    def get_signature_algorithm(self, *args, **kwargs): # real signature unknown
        """
        Retrieve the signature algorithm used in the certificate
        
        @return: A byte string giving the name of the signature algorithm used in
                 the certificate.
        @raise ValueError: If the signature algorithm is undefined.
        """
        pass

    def get_subject(self, *args, **kwargs): # real signature unknown
        """
        Create an X509Name object for the subject of the certificate
        
        @return: An X509Name object
        """
        pass

    def get_version(self, *args, **kwargs): # real signature unknown
        """
        Return version number of the certificate
        
        @return: Version number as a Python integer
        """
        pass

    def gmtime_adj_notAfter(self, *args, **kwargs): # real signature unknown
        """
        Adjust the time stamp for when the certificate stops being valid
        
        @param amount: The number of seconds by which to adjust the ending validity
                       time.
        @return: None
        """
        pass

    def gmtime_adj_notBefore(self, *args, **kwargs): # real signature unknown
        """
        Change the timestamp for when the certificate starts being valid to the current
        time plus an offset.
         
        @param amount: The number of seconds by which to adjust the starting validity
                       time.
        @return: None
        """
        pass

    def has_expired(self, *args, **kwargs): # real signature unknown
        """
        Check whether the certificate has expired.
        
        @return: True if the certificate has expired, false otherwise
        """
        pass

    def set_issuer(self, *args, **kwargs): # real signature unknown
        """
        Set the issuer of the certificate
        
        @param issuer: The issuer name
        @type issuer: L{X509Name}
        @return: None
        """
        pass

    def set_notAfter(self, *args, **kwargs): # real signature unknown
        """
        Set the time stamp for when the certificate stops being valid
        
        @param when: A string giving the timestamp, in the format:
        
                         YYYYMMDDhhmmssZ
                         YYYYMMDDhhmmss+hhmm
                         YYYYMMDDhhmmss-hhmm
        
        @return: None
        """
        pass

    def set_notBefore(self, *args, **kwargs): # real signature unknown
        """
        Set the time stamp for when the certificate starts being valid
        
        @param when: A string giving the timestamp, in the format:
        
                         YYYYMMDDhhmmssZ
                         YYYYMMDDhhmmss+hhmm
                         YYYYMMDDhhmmss-hhmm
        
        @return: None
        """
        pass

    def set_pubkey(self, *args, **kwargs): # real signature unknown
        """
        Set the public key of the certificate
        
        @param pkey: The public key
        @return: None
        """
        pass

    def set_serial_number(self, *args, **kwargs): # real signature unknown
        """
        Set serial number of the certificate
        
        @param serial: The serial number
        @return: None
        """
        pass

    def set_subject(self, *args, **kwargs): # real signature unknown
        """
        Set the subject of the certificate
        
        @param subject: The subject name
        @type subject: L{X509Name}
        @return: None
        """
        pass

    def set_version(self, *args, **kwargs): # real signature unknown
        """
        Set version number of the certificate
        
        @param version: The version number
        @return: None
        """
        pass

    def sign(self, *args, **kwargs): # real signature unknown
        """
        Sign the certificate using the supplied key and digest
        
        @param pkey: The key to sign with
        @param digest: The message digest to use
        @return: None
        """
        pass

    def subject_name_hash(self, *args, **kwargs): # real signature unknown
        """
        Return the hash of the X509 subject.
        
        @return: The hash of the subject
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


X509 = X509Type


class X509ExtensionType(object):
    """
    X509Extension(typename, critical, value[, subject][, issuer]) -> 
                    X509Extension instance
    
    @param typename: The name of the extension to create.
    @type typename: C{str}
    @param critical: A flag indicating whether this is a critical extension.
    @param value: The value of the extension.
    @type value: C{str}
    @param subject: Optional X509 cert to use as subject.
    @type subject: C{X509}
    @param issuer: Optional X509 cert to use as issuer.
    @type issuer: C{X509}
    @return: The X509Extension object
    """
    def get_critical(self, *args, **kwargs): # real signature unknown
        """
        Returns the critical field of the X509Extension
        
        @return: The critical field.
        """
        pass

    def get_data(self, *args, **kwargs): # real signature unknown
        """
        Returns the data of the X509Extension
        
        @return: A C{str} giving the X509Extension's ASN.1 encoded data.
        """
        pass

    def get_short_name(self, *args, **kwargs): # real signature unknown
        """
        Returns the short version of the type name of the X509Extension
        
        @return: The short type name.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass


X509Extension = X509ExtensionType


class X509NameType(object):
    """
    X509Name(name) -> New X509Name object
    
    Create a new X509Name, copying the given X509Name instance.
    
    @param name: An X509Name object to copy
    @return: The X509Name object
    """
    def der(self, *args, **kwargs): # real signature unknown
        """
        Return the DER encoding of this name
        
        @return: None
        """
        pass

    def get_components(self, *args, **kwargs): # real signature unknown
        """
        Returns the split-up components of this name.
        
        @return: List of tuples (name, value).
        """
        pass

    def hash(self, *args, **kwargs): # real signature unknown
        """
        Return the hash value of this name
        
        @return: None
        """
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
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

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass


X509Name = X509NameType


class X509ReqType(object):
    """
    X509Req() -> X509Req instance
    
    Create a new X509Req object.
    
    @return: The X509Req object
    """
    def add_extensions(self, *args, **kwargs): # real signature unknown
        """
        Add extensions to the request.
        
        @param extensions: a sequence of X509Extension objects
        @return: None
        """
        pass

    def get_pubkey(self, *args, **kwargs): # real signature unknown
        """
        Get the public key from the certificate request
        
        @return: The public key
        """
        pass

    def get_subject(self, *args, **kwargs): # real signature unknown
        """
        Create an X509Name object for the subject of the certificate request
        
        @return: An X509Name object
        """
        pass

    def get_version(self, *args, **kwargs): # real signature unknown
        """
        Get the version subfield (RFC 2459, section 4.1.2.1) of the certificate
        request.
        
        @return: an integer giving the value of the version subfield
        """
        pass

    def set_pubkey(self, *args, **kwargs): # real signature unknown
        """
        Set the public key of the certificate request
        
        @param pkey: The public key to use
        @return: None
        """
        pass

    def set_version(self, *args, **kwargs): # real signature unknown
        """
        Set the version subfield (RFC 2459, section 4.1.2.1) of the certificate
        request.
        
        @param version: The version number
        @return: None
        """
        pass

    def sign(self, *args, **kwargs): # real signature unknown
        """
        Sign the certificate request using the supplied key and digest
        
        @param pkey: The key to sign with
        @param digest: The message digest to use
        @return: None
        """
        pass

    def verify(self, *args, **kwargs): # real signature unknown
        """
        Verifies a certificate request using the supplied public key
        
        @param key: a public key
        @return: True if the signature is correct.
        @raise OpenSSL.crypto.Error: If the signature is invalid or there is a
            problem verifying the signature.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


X509Req = X509ReqType


class X509StoreType(object):
    # no doc
    def add_cert(self, *args, **kwargs): # real signature unknown
        """
        Add a certificate
        
        @param cert: The certificate to add
        @return: None
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

_C_API = None # (!) real value is ''

