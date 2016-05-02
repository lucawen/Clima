# encoding: utf-8
# module mx.Tools.mxTools.mxTools
# from /usr/lib/python2.7/dist-packages/mx/Tools/mxTools/mxTools.so
# by generator 1.138
"""
mxTools -- A tool collection. Version 3.2.7

Copyright (c) 1997-2000, Marc-Andre Lemburg; mailto:mal@lemburg.com
Copyright (c) 2000-2013, eGenix.com Software GmbH; mailto:info@egenix.com

                 All Rights Reserved

See the documentation for further information on copyrights,
or contact the author.
"""
# no imports

# Variables with simple values

RTLD_DEEPBIND = 8
RTLD_GLOBAL = 256
RTLD_LAZY = 1
RTLD_LOCAL = 0
RTLD_NODELETE = 4096
RTLD_NOLOAD = 4
RTLD_NOW = 2

__version__ = '3.2.7'

# functions

def acquire(self, name, baseobjattr='baseobj'): # real signature unknown; restored from __doc__
    """
    acquire(self,name[,baseobjattr='baseobj'])
    
    Tries to get the attribute name from self.<baseobjattr>.
    If this is not defined or None, an AttributeError is
    raised. Otherwise getattr(self.<baseobjattr>,name) is
    returned. Attribute names must not start with an
    underscore (this too raises an AttributeError).
    """
    pass

def attrlist(objectlist, attrname): # real signature unknown; restored from __doc__
    """
    attrlist(objectlist,attrname)
    
    Returns a list of all attributes with the given name
    found among the objects in objectlist.
    """
    pass

def count(condition, sequence): # real signature unknown; restored from __doc__
    """
    count(condition,sequence)
    
    Count the number of objects in sequence for which the
    selection function condition returns true and return the
    result as integer.
    """
    pass

def cur_frame(offset=0): # real signature unknown; restored from __doc__
    """
    cur_frame([offset=0])
    
    Returns the current execution frame, optionally going up the
    stack by offset levels. If there are less than offset
    frames on the stack, None is returned. The function is thread
    safe.
    """
    pass

def debugging(level=None): # real signature unknown; restored from __doc__
    """
    debugging([level])
    
    Sets the value of the interpreter's debugging flag.
    Returns the flag's value before changing it or, when called
    without level, the current value.
    """
    pass

def dict(seq): # real signature unknown; restored from __doc__
    """
    dict(seq)
    
    Creates a dictionary from the given items sequence.
    The sequence must contain sub-sequences of at least length 2,
    the first entry being interpreted as the key and the second as
    the value.
    """
    pass

def dictscan(dictobj, prevposition=0): # real signature unknown; restored from __doc__
    """
    dictscan(dictobj[,prevposition=0])
    
    Dictionary scanner. Returns a tuple (key,value,position)
    containing the key,value pair and slot position of the next
    item found in the dictionaries hash table after slot
    prevposition. Raises an IndexError when the end
    of the table is reached or the prevposition index is out of
    range.
    """
    pass

def dlopen(libname, mode): # real signature unknown; restored from __doc__
    """
    dlopen(libname, mode)
    
    Load the shared lib libname using the flags given in mode.
    mode defaults to Python's standard dlopenflags.
    """
    pass

def exists(condition, sequence): # real signature unknown; restored from __doc__
    """
    exists(condition,sequence)
    Return 1 if and only if condition is true for at least one
    of the items in sequence and 0 otherwise. condition
    must be a callable object.
    """
    pass

def extract(p_object, indices, defaults=None): # real signature unknown; restored from __doc__
    """
    extract(object,indices[,defaults])
    
    Returns a list of entries object[index] for each index
    in the sequence indices. defaults must have the same length
    as indices and is used to provide default values in case
    the lookup fails.
    """
    pass

def findattr(objectlist, attrname): # real signature unknown; restored from __doc__
    """
    findattr(objectlist,attrname)
    
    Returns the first attribute with name attrname found
    among the objects in the list.
    """
    pass

def forall(condition, sequence): # real signature unknown; restored from __doc__
    """
    forall(condition,sequence)
    
    Return 1 if and only if condition is true for all
    of the items in sequence and 0 otherwise. condition
    must be a callable object.
    """
    pass

def get(p_object, index, default=None): # real signature unknown; restored from __doc__
    """
    get(object,index[,default])
    
    Returns object[index], or, if that fails, default.
    """
    pass

def ifilter(condition, p_object, indices=None): # real signature unknown; restored from __doc__
    """
    ifilter(condition,object[,indices])
    
    Returns a list of tuples (index,object[index]) such that
    condition(object[item]) is true and index is found in
    the sequence indices (defaulting to indices(object)).
    Order is preserved. condition must be a callable object.
    """
    pass

def index(condition, sequence): # real signature unknown; restored from __doc__
    """
    index(condition,sequence)
    
    Return the index of the first item for which condition
    returns true. A ValueError is raised in case no item
    is found.
    """
    pass

def indices(p_object): # real signature unknown; restored from __doc__
    """
    indices(object)
    
    Returns tuple(range(len(object))).
    """
    pass

def interactive(level=None): # real signature unknown; restored from __doc__
    """
    interactive([level])
    
    Sets the value of the interpreter's interactive flag.
    Returns the flag's value before changing it or, when called
    without level, the current value.
    """
    pass

def invdict(d): # real signature unknown; restored from __doc__
    """
    invdict(d)
    
    Creates a dictionary with inverse mappings from the
    given dictionary d.
    """
    pass

def irange(p_object, indices=None): # real signature unknown; restored from __doc__
    """
    irange(object[,indices])
    
    Returns a tuple of tuples (index,object[index]), one
    for each item in the sequence indices or, if this is not
    given, in trange(len(object)).
    """
    pass

def iremove(p_object, indices): # real signature unknown; restored from __doc__
    """
    iremove(object,indices)
    
    Removes the items indexed by indices from object.
    For sequences the index list must be sorted ascending;
    an IndexError will be raised otherwise (object is then
    left in an undefined state).
    """
    pass

def lists(sequence): # real signature unknown; restored from __doc__
    """
    lists(sequence)
    
    Same as tuples(), except that a tuple of lists is created.
    """
    pass

def makeref(id): # real signature unknown; restored from __doc__
    """
    makeref(id)
    
    Provided that id is a valid address of a Python object,
    this function returns a new reference to it. You can use this
    function to reaccess objects lost during garbage collection.
    USE WITH CARE - since this can cause core dumps !
    """
    pass

def mapply(callable_objects, args=(), kw={}): # real signature unknown; restored from __doc__
    """
    mapply(callable_objects,args=(),kw={})
    
    Calls the callable_objects in the given order with the same
    arguments and returns a tuple with the return values.
    """
    pass

def method_mapply(objects, methodname, args=(), kw={}): # real signature unknown; restored from __doc__
    """
    method_mapply(objects,methodname,args=(),kw={})
    
    Calls the method methodname of all objects in the given
    order with the same arguments and returns a tuple with
    the return values.
    """
    pass

def mget(*args, **kwargs): # real signature unknown
    """
    extract(object,indices[,defaults])
    
    Returns a list of entries object[index] for each index
    in the sequence indices. defaults must have the same length
    as indices and is used to provide default values in case
    the lookup fails.
    """
    pass

def mgetattr(*args, **kwargs): # real signature unknown
    """
    findattr(objectlist,attrname)
    
    Returns the first attribute with name attrname found
    among the objects in the list.
    """
    pass

def napply(number_of_calls, function, args=(), kw={}): # real signature unknown; restored from __doc__
    """
    napply(number_of_calls,function,args=(),kw={})
    
    Calls the function number_of_calls times with the same
    arguments and returns a tuple with the return values.
    """
    pass

def optimization(level=None): # real signature unknown; restored from __doc__
    """
    optimization([level])
    
    Sets the value of the interpreter's optimization flag.
    Returns the flag's value before changing it or, when called
    without level, the current value.
    """
    pass

def range_len(p_object): # real signature unknown; restored from __doc__
    """
    range_len(object)
    Returns range(len(object)).
    """
    pass

def reverse(seq): # real signature unknown; restored from __doc__
    """
    reverse(seq)
    
    Creates a new sequence with reversed order of the items in
    seq. If seq is a tuple, then a tuple is returned. Otherwise
    a list is returned.
    """
    pass

def setdict(seq, value=None): # real signature unknown; restored from __doc__
    """
    setdict(seq,value=None)
    
    Creates a dictionary from the given items sequence.
    The sequence must hashable entries which are used as
    dictionary keys. The values are all set to value.
    """
    pass

def sign(number): # real signature unknown; restored from __doc__
    """
    sign(number)
    
    Returns the signum of the number, i.e. -1 for negative
    numbers, +1 for positive ones and 0 in case it is equal to 0
    """
    pass

def sizeof(p_object): # real signature unknown; restored from __doc__
    """
    sizeof(object)
    
    Returns the size in memory of the object in bytes.
    Note that this doesn't show any extra space allocated by
    the object.
    """
    pass

def trange(start=0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    trange([start=0,]stop[,step=1])
    
    Returns tuple(range(start,stop,step))
    """
    pass

def trange_len(*args, **kwargs): # real signature unknown
    """
    indices(object)
    
    Returns tuple(range(len(object))).
    """
    pass

def truth(p_object): # real signature unknown; restored from __doc__
    """
    truth(object)
    
    Return the truth value of object as True or False singleton.Note that the two singletons are actually the integers 1 and 0.
    """
    pass

def tuples(sequence): # real signature unknown; restored from __doc__
    """
    tuples(sequence)
    
    Returns a list much like apply(map,(None,)+tuple(sequence)))
    does. Only with a bit more intuitive name. This function does
    not optimize for the case where the sequences are of different
    size and the resulting list of tuples will always
    have the length of the first sequence. Missing entries
    from the other sequences are filled in with None.
    """
    pass

def verbosity(level=None): # real signature unknown; restored from __doc__
    """
    verbosity([level])
    
    Sets the value of the interpreter's verbosity flag.
    Returns the flag's value before changing it or, when called
    without level, the current value.
    """
    pass

def verscmp(a, b): # real signature unknown; restored from __doc__
    """
    verscmp(a,b)
    
    Compares two version strings and returns -1,0,1 for
    <,==,> resp.
    """
    pass

# classes

class Error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class ProgrammingError(RuntimeError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

NotGiven = NotGiven

