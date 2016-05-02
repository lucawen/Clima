# encoding: utf-8
# module OpenSSL.rand
# from /usr/lib/python2.7/dist-packages/OpenSSL/rand.so
# by generator 1.138
"""
PRNG management routines, thin wrappers.
See the file RATIONALE for a short explanation of why this module was written.
"""
# no imports

# functions

def add(*args, **kwargs): # real signature unknown
    """
    Add data with a given entropy to the PRNG
    
    @param buffer: Buffer with random data
    @param entropy: The entropy (in bytes) measurement of the buffer
    @return: None
    """
    pass

def bytes(*args, **kwargs): # real signature unknown
    """
    Get some randomm bytes as a string.
    
    @param num_bytes: The number of bytes to fetch
    @return: A string of random bytes
    """
    pass

def cleanup(*args, **kwargs): # real signature unknown
    """
    Erase the memory used by the PRNG.
    
    @return: None
    """
    pass

def egd(*args, **kwargs): # real signature unknown
    """
    Query an entropy gathering daemon (EGD) for random data and add it to the
    PRNG. I haven't found any problems when the socket is missing, the function
    just returns 0.
    
    @param path: The path to the EGD socket
    @param bytes: (optional) The number of bytes to read, default is 255
    @returns: The number of bytes read (NB: a value of 0 isn't necessarily an
              error, check rand.status())
    """
    pass

def load_file(*args, **kwargs): # real signature unknown
    """
    Seed the PRNG with data from a file
    
    @param filename: The file to read data from
    @param maxbytes: (optional) The number of bytes to read, default is
                     to read the entire file
    @return: The number of bytes read
    """
    pass

def seed(*args, **kwargs): # real signature unknown
    """
    Alias for rand_add, with entropy equal to length
    
    @param buffer: Buffer with random data
    @return: None
    """
    pass

def status(*args, **kwargs): # real signature unknown
    """
    Retrieve the status of the PRNG
    
    @return: True if the PRNG is seeded enough, false otherwise
    """
    pass

def write_file(*args, **kwargs): # real signature unknown
    """
    Save PRNG state to a file
    
    @param filename: The file to write data to
    @return: The number of bytes written
    """
    pass

# classes

class Error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



