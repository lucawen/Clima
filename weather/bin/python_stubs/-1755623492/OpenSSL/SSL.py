# encoding: utf-8
# module OpenSSL.SSL
# from /usr/lib/python2.7/dist-packages/OpenSSL/SSL.so
# by generator 1.138
"""
Main file of the SSL sub module.
See the file RATIONALE for a short explanation of why this module was written.
"""
# no imports

# Variables with simple values

FILETYPE_ASN1 = 2
FILETYPE_PEM = 1

OPENSSL_VERSION_NUMBER = 268439663

OP_ALL = 2147486719

OP_CIPHER_SERVER_PREFERENCE = 4194304

OP_COOKIE_EXCHANGE = 8192

OP_DONT_INSERT_EMPTY_FRAGMENTS = 2048

OP_EPHEMERAL_RSA = 2097152

OP_MICROSOFT_BIG_SSLV3_BUFFER = 32

OP_MICROSOFT_SESS_ID_BUG = 1

OP_MSIE_SSLV2_RSA_PADDING = 0

OP_NETSCAPE_CA_DN_BUG = 536870912

OP_NETSCAPE_CHALLENGE_BUG = 2

OP_NETSCAPE_DEMO_CIPHER_CHANGE_BUG = 1073741824

OP_NETSCAPE_REUSE_CIPHER_CHANGE_BUG = 8

OP_NO_QUERY_MTU = 4096

OP_NO_SSLv2 = 16777216
OP_NO_SSLv3 = 33554432
OP_NO_TICKET = 16384
OP_NO_TLSv1 = 67108864

OP_PKCS1_CHECK_1 = 0
OP_PKCS1_CHECK_2 = 0

OP_SINGLE_DH_USE = 1048576

OP_SSLEAY_080_CLIENT_DH_BUG = 128

OP_SSLREF2_REUSE_CERT_TYPE_BUG = 16

OP_TLS_BLOCK_PADDING_BUG = 512

OP_TLS_D5_BUG = 256

OP_TLS_ROLLBACK_BUG = 8388608

RECEIVED_SHUTDOWN = 2

SENT_SHUTDOWN = 1

SSLEAY_BUILT_ON = 3

SSLEAY_CFLAGS = 2
SSLEAY_DIR = 5
SSLEAY_PLATFORM = 4
SSLEAY_VERSION = 0

SSLv23_METHOD = 3

SSLv2_METHOD = 1

SSLv3_METHOD = 2

SSL_CB_ACCEPT_EXIT = 8194
SSL_CB_ACCEPT_LOOP = 8193

SSL_CB_ALERT = 16384

SSL_CB_CONNECT_EXIT = 4098
SSL_CB_CONNECT_LOOP = 4097

SSL_CB_EXIT = 2

SSL_CB_HANDSHAKE_DONE = 32
SSL_CB_HANDSHAKE_START = 16

SSL_CB_LOOP = 1
SSL_CB_READ = 4

SSL_CB_READ_ALERT = 16388

SSL_CB_WRITE = 8

SSL_CB_WRITE_ALERT = 16392

SSL_ST_ACCEPT = 8192
SSL_ST_BEFORE = 16384
SSL_ST_CONNECT = 4096
SSL_ST_INIT = 12288
SSL_ST_MASK = 4095
SSL_ST_OK = 3
SSL_ST_RENEGOTIATE = 12292

TLSv1_METHOD = 4

VERIFY_CLIENT_ONCE = 4

VERIFY_FAIL_IF_NO_PEER_CERT = 2

VERIFY_NONE = 0
VERIFY_PEER = 1

# functions

def SSLeay_version(*args, **kwargs): # real signature unknown
    """
    Return a string describing the version of OpenSSL in use.
    
    @param type: One of the SSLEAY_ constants defined in this module.
    """
    pass

# classes

class ConnectionType(object):
    """
    Connection(context, socket) -> Connection instance
    
    Create a new Connection object, using the given OpenSSL.SSL.Context instance
    and socket.
    
    @param context: An SSL Context to use for this connection
    @param socket: The socket to use for transport layer
    """
    def accept(self, *args, **kwargs): # real signature unknown
        """
        Accept incoming connection and set up SSL on it
        
        @return: A (conn,addr) pair where conn is a Connection and addr is an
                 address
        """
        pass

    def bio_read(self, *args, **kwargs): # real signature unknown
        """
        When using non-socket connections this function reads
        the "dirty" data that would have traveled away on the network.
        
        @param bufsiz: The maximum number of bytes to read
        @return: The string read.
        """
        pass

    def bio_shutdown(self, *args, **kwargs): # real signature unknown
        """
        When using non-socket connections this function signals end of
        data on the input for this connection.
        
        @return: None
        """
        pass

    def bio_write(self, *args, **kwargs): # real signature unknown
        """
        When using non-socket connections this function sends
        "dirty" data that would have traveled in on the network.
        
        @param buf: The string to put into the memory BIO.
        @return: The number of bytes written
        """
        pass

    def client_random(self, *args, **kwargs): # real signature unknown
        """
        Get a copy of the client hello nonce.
        
        @return: A string representing the state
        """
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        """
        Connect to remote host and set up client-side SSL
        
        @param addr: A remote address
        @return: What the socket's connect method returns
        """
        pass

    def connect_ex(self, *args, **kwargs): # real signature unknown
        """
        Connect to remote host and set up client-side SSL. Note that if the socket's
        connect_ex method doesn't return 0, SSL won't be initialized.
        
        @param addr: A remove address
        @return: What the socket's connect_ex method returns
        """
        pass

    def do_handshake(self, *args, **kwargs): # real signature unknown
        """
        Perform an SSL handshake (usually called after renegotiate() or one of
        set_*_state()). This can raise the same exceptions as send and recv.
        
        @return: None.
        """
        pass

    def get_app_data(self, *args, **kwargs): # real signature unknown
        """
        Get application data
        
        @return: The application data
        """
        pass

    def get_cipher_list(self, *args, **kwargs): # real signature unknown
        """
        Get the session cipher list
        
        @return: A list of cipher strings
        """
        pass

    def get_client_ca_list(self, *args, **kwargs): # real signature unknown
        """
        Get CAs whose certificates are suggested for client authentication.
        
        @return: If this is a server connection, a list of X509Names representing
            the acceptable CAs as set by L{OpenSSL.SSL.Context.set_client_ca_list} or
            L{OpenSSL.SSL.Context.add_client_ca}.  If this is a client connection,
            the list of such X509Names sent by the server, or an empty list if that
            has not yet happened.
        """
        pass

    def get_context(self, *args, **kwargs): # real signature unknown
        """
        Get session context
        
        @return: A Context object
        """
        pass

    def get_peer_certificate(self, *args, **kwargs): # real signature unknown
        """
        Retrieve the other side's certificate (if any)
        
        @return: The peer's certificate
        """
        pass

    def get_peer_cert_chain(self, *args, **kwargs): # real signature unknown
        """
        Retrieve the other side's certificate (if any)
        
        @return: A list of X509 instances giving the peer's certificate chain,
                 or None if it does not have one.
        """
        pass

    def get_servername(self, *args, **kwargs): # real signature unknown
        """
        Retrieve the servername extension value if provided in the client hello
        message, or None if there wasn't one.
        
        @return: A byte string giving the server name or C{None}.
        """
        pass

    def get_shutdown(self, *args, **kwargs): # real signature unknown
        """
        Get shutdown state
        
        @return: The shutdown state, a bitvector of SENT_SHUTDOWN, RECEIVED_SHUTDOWN.
        """
        pass

    def makefile(self): # real signature unknown; restored from __doc__
        """
        The makefile() method is not implemented, since there is no dup semantics
        for SSL connections
        
        @raise NotImplementedError
        """
        pass

    def master_key(self, *args, **kwargs): # real signature unknown
        """
        Get a copy of the master key.
        
        @return: A string representing the state
        """
        pass

    def pending(self, *args, **kwargs): # real signature unknown
        """
        Get the number of bytes that can be safely read from the connection
        
        @return: The number of bytes available in the receive buffer.
        """
        pass

    def read(self, *args, **kwargs): # real signature unknown
        """
        Receive data on the connection. NOTE: If you get one of the WantRead,
        WantWrite or WantX509Lookup exceptions on this, you have to call the
        method again with the SAME buffer.
        
        @param bufsiz: The maximum number of bytes to read
        @param flags: (optional) Included for compatibility with the socket
                      API, the value is ignored
        @return: The string read from the Connection
        """
        pass

    def recv(self, *args, **kwargs): # real signature unknown
        """
        Receive data on the connection. NOTE: If you get one of the WantRead,
        WantWrite or WantX509Lookup exceptions on this, you have to call the
        method again with the SAME buffer.
        
        @param bufsiz: The maximum number of bytes to read
        @param flags: (optional) Included for compatibility with the socket
                      API, the value is ignored
        @return: The string read from the Connection
        """
        pass

    def renegotiate(self, *args, **kwargs): # real signature unknown
        """
        Renegotiate the session
        
        @return: True if the renegotiation can be started, false otherwise
        """
        pass

    def renegotiate_pending(self, *args, **kwargs): # real signature unknown
        """
        Check if there's a renegotiation in progress, it will return false once
        a renegotiation is finished.
        
        @return: Whether there's a renegotiation in progress
        """
        pass

    def send(self, *args, **kwargs): # real signature unknown
        """
        Send data on the connection. NOTE: If you get one of the WantRead,
        WantWrite or WantX509Lookup exceptions on this, you have to call the
        method again with the SAME buffer.
        
        @param buf: The string to send
        @param flags: (optional) Included for compatibility with the socket
                      API, the value is ignored
        @return: The number of bytes written
        """
        pass

    def sendall(self, *args, **kwargs): # real signature unknown
        """
        Send "all" data on the connection. This calls send() repeatedly until
        all data is sent. If an error occurs, it's impossible to tell how much data
        has been sent.
        
        @param buf: The string to send
        @param flags: (optional) Included for compatibility with the socket
                      API, the value is ignored
        @return: The number of bytes written
        """
        pass

    def server_random(self, *args, **kwargs): # real signature unknown
        """
        Get a copy of the server hello nonce.
        
        @return: A string representing the state
        """
        pass

    def set_accept_state(self, *args, **kwargs): # real signature unknown
        """
        Set the connection to work in server mode. The handshake will be handled
        automatically by read/write.
        
        @return: None
        """
        pass

    def set_app_data(self, *args, **kwargs): # real signature unknown
        """
        Set application data
        
        @param data - The application data
        @return: None
        """
        pass

    def set_connect_state(self, *args, **kwargs): # real signature unknown
        """
        Set the connection to work in client mode. The handshake will be handled
        automatically by read/write.
        
        @return: None
        """
        pass

    def set_context(self, *args, **kwargs): # real signature unknown
        """
        Switch this connection to a new session context
        
        @param context: A L{Context} instance giving the new session context to use.
        """
        pass

    def set_shutdown(self, *args, **kwargs): # real signature unknown
        """
        Set shutdown state
        
        @param state - bitvector of SENT_SHUTDOWN, RECEIVED_SHUTDOWN.
        @return: None
        """
        pass

    def set_tlsext_host_name(self, *args, **kwargs): # real signature unknown
        """
        Set the value of the servername extension to send in the client hello.
        
        @param name: A byte string giving the name.
        """
        pass

    def shutdown(self, *args, **kwargs): # real signature unknown
        """
        Send closure alert
        
        @return: True if the shutdown completed successfully (i.e. both sides
                 have sent closure alerts), false otherwise (i.e. you have to
                 wait for a ZeroReturnError on a recv() method call
        """
        pass

    def sock_shutdown(self, *args, **kwargs): # real signature unknown
        """
        See shutdown(2)
        
        @return: What the socket's shutdown() method returns
        """
        pass

    def state_string(self, *args, **kwargs): # real signature unknown
        """
        Get a verbose state description
        
        @return: A string representing the state
        """
        pass

    def total_renegotiations(self, *args, **kwargs): # real signature unknown
        """
        Find out the total number of renegotiations.
        
        @return: The number of renegotiations.
        """
        pass

    def want_read(self, *args, **kwargs): # real signature unknown
        """
        Checks if more data has to be read from the transport layer to complete an
        operation.
        
        @return: True iff more data has to be read
        """
        pass

    def want_write(self, *args, **kwargs): # real signature unknown
        """
        Checks if there is data to write to the transport layer to complete an
        operation.
        
        @return: True iff there is data to write
        """
        pass

    def write(self, *args, **kwargs): # real signature unknown
        """
        Send data on the connection. NOTE: If you get one of the WantRead,
        WantWrite or WantX509Lookup exceptions on this, you have to call the
        method again with the SAME buffer.
        
        @param buf: The string to send
        @param flags: (optional) Included for compatibility with the socket
                      API, the value is ignored
        @return: The number of bytes written
        """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


Connection = ConnectionType


class ContextType(object):
    """
    Context(method) -> Context instance
    
    OpenSSL.SSL.Context instances define the parameters for setting up new SSL
    connections.
    
    @param method: One of SSLv3_METHOD, SSLv23_METHOD, or
                   TLSv1_METHOD.
    """
    def add_client_ca(self, *args, **kwargs): # real signature unknown
        """
        Add the CA certificate to the list of preferred signers for this context.
        
        The list of certificate authorities will be sent to the client when the
        server requests a client certificate.
        
        @param certificate_authority: certificate authority's X509 certificate.
        @return: None
        """
        pass

    def add_extra_chain_cert(self, *args, **kwargs): # real signature unknown
        """
        Add certificate to chain
        
        @param certobj: The X509 certificate object to add to the chain
        @return: None
        """
        pass

    def check_privatekey(self, *args, **kwargs): # real signature unknown
        """
        Check that the private key and certificate match up
        
        @return: None (raises an exception if something's wrong)
        """
        pass

    def get_app_data(self, *args, **kwargs): # real signature unknown
        """
        Get the application data (supplied via set_app_data())
        
        @return: The application data
        """
        pass

    def get_cert_store(self, *args, **kwargs): # real signature unknown
        """
        Get the certificate store for the context
        
        @return: A X509Store object
        """
        pass

    def get_timeout(self, *args, **kwargs): # real signature unknown
        """
        Get the session timeout
        
        @return: The session timeout
        """
        pass

    def get_verify_depth(self, *args, **kwargs): # real signature unknown
        """
        Get the verify depth
        
        @return: The verify depth
        """
        pass

    def get_verify_mode(self, *args, **kwargs): # real signature unknown
        """
        Get the verify mode
        
        @return: The verify mode
        """
        pass

    def load_client_ca(self, *args, **kwargs): # real signature unknown
        """
        Load the trusted certificates that will be sent to the client (basically
         telling the client "These are the guys I trust").  Does not actually
        imply any of the certificates are trusted; that must be configured
        separately.
        
        @param cafile: The name of the certificates file
        @return: None
        """
        pass

    def load_tmp_dh(self, *args, **kwargs): # real signature unknown
        """
        Load parameters for Ephemeral Diffie-Hellman
        
        @param dhfile: The file to load EDH parameters from
        @return: None
        """
        pass

    def load_verify_locations(self, *args, **kwargs): # real signature unknown
        """
        Let SSL know where we can find trusted certificates for the certificate
        chain
        
        @param cafile: In which file we can find the certificates
        @param capath: In which directory we can find the certificates
        @return: None
        """
        pass

    def set_app_data(self, *args, **kwargs): # real signature unknown
        """
        Set the application data (will be returned from get_app_data())
        
        @param data: Any Python object
        @return: None
        """
        pass

    def set_cipher_list(self, *args, **kwargs): # real signature unknown
        """
        Change the cipher list
        
        @param cipher_list: A cipher list, see ciphers(1)
        @return: None
        """
        pass

    def set_client_ca_list(self, *args, **kwargs): # real signature unknown
        """
        Set the list of preferred client certificate signers for this server context.
        
        This list of certificate authorities will be sent to the client when the
        server requests a client certificate.
        
        @param certificate_authorities: a sequence of X509Names.
        @return: None
        """
        pass

    def set_default_verify_paths(self, *args, **kwargs): # real signature unknown
        """
        Use the platform-specific CA certificate locations
        
        @return: None
        """
        pass

    def set_info_callback(self, *args, **kwargs): # real signature unknown
        """
        Set the info callback
        
        @param callback: The Python callback to use
        @return: None
        """
        pass

    def set_options(self, *args, **kwargs): # real signature unknown
        """
        Add options. Options set before are not cleared!
        
        @param options: The options to add.
        @return: The new option bitmask.
        """
        pass

    def set_passwd_cb(self, *args, **kwargs): # real signature unknown
        """
        Set the passphrase callback
        
        @param callback: The Python callback to use
        @param userdata: (optional) A Python object which will be given as
                         argument to the callback
        @return: None
        """
        pass

    def set_session_id(self, *args, **kwargs): # real signature unknown
        """
        Set the session identifier, this is needed if you want to do session
        resumption (which, ironically, isn't implemented yet)
        
        @param buf: A Python object that can be safely converted to a string
        @returns: None
        """
        pass

    def set_timeout(self, *args, **kwargs): # real signature unknown
        """
        Set session timeout
        
        @param timeout: The timeout in seconds
        @return: The previous session timeout
        """
        pass

    def set_tlsext_servername_callback(self, *args, **kwargs): # real signature unknown
        """
        Specify a callback function to be called when clients specify a server name.
        
        @param callback: The callback function.  It will be invoked with one
            argument, the Connection instance.
        """
        pass

    def set_verify(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Set the verify mode and verify callback
        
        @param mode: The verify mode, this is either VERIFY_NONE or
                     VERIFY_PEER combined with possible other flags
        @param callback: The Python callback to use
        @return: None
        
        See SSL_CTX_set_verify(3SSL) for further details.
        """
        pass

    def set_verify_depth(self, *args, **kwargs): # real signature unknown
        """
        Set the verify depth
        
        @param depth: An integer specifying the verify depth
        @return: None
        """
        pass

    def use_certificate(self, *args, **kwargs): # real signature unknown
        """
        Load a certificate from a X509 object
        
        @param cert: The X509 object
        @return: None
        """
        pass

    def use_certificate_chain_file(self, *args, **kwargs): # real signature unknown
        """
        Load a certificate chain from a file
        
        @param certfile: The name of the certificate chain file
        @return: None
        """
        pass

    def use_certificate_file(self, *args, **kwargs): # real signature unknown
        """
        Load a certificate from a file
        
        @param certfile: The name of the certificate file
        @param filetype: (optional) The encoding of the file, default is PEM
        @return: None
        """
        pass

    def use_privatekey(self, *args, **kwargs): # real signature unknown
        """
        Load a private key from a PKey object
        
        @param pkey: The PKey object
        @return: None
        """
        pass

    def use_privatekey_file(self, *args, **kwargs): # real signature unknown
        """
        Load a private key from a file
        
        @param keyfile: The name of the key file
        @param filetype: (optional) The encoding of the file, default is PEM
        @return: None
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


Context = ContextType


class Error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class SysCallError(Error):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class WantReadError(Error):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class WantWriteError(Error):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class WantX509LookupError(Error):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class ZeroReturnError(Error):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

_C_API = None # (!) real value is ''

