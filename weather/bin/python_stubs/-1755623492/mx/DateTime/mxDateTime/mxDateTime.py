# encoding: utf-8
# module mx.DateTime.mxDateTime.mxDateTime
# from /usr/lib/python2.7/dist-packages/mx/DateTime/mxDateTime/mxDateTime.so
# by generator 1.138
"""
mxDateTime -- Generic date/time types. Version 3.2.7

Copyright (c) 1997-2000, Marc-Andre Lemburg; mailto:mal@lemburg.com
Copyright (c) 2000-2013, eGenix.com Software GmbH; mailto:info@egenix.com

                 All Rights Reserved

See the documentation for further information on copyrights,
or contact the author.
"""

# imports
import mx.DateTime as __mx_DateTime


# Variables with simple values

Gregorian = 'Gregorian'

Julian = 'Julian'

now_resolution = 1e-09

POSIX = 1

__version__ = '3.2.7'

# functions

def cmp(value1, value2, accuracy=0.0): # real signature unknown; restored from __doc__
    """
    cmp(value1,value2[,accuracy=0.0])
    
    Compares two DateTime[Delta] objects. If accuracy is
    given, then equality will result in case the absolute
    difference between the two values is less than or equal
    to accuracy.
    """
    pass

def DateTime(year, month=1, day=1, hour=0, minute=0, second=0.0): # real signature unknown; restored from __doc__
    """
    DateTime(year,month=1,day=1,hour=0,minute=0,second=0.0)
    
    Returns a DateTime-object reflecting the given date
    and time. Seconds can be given as float to indicate
    fractions. Note that the function does not accept keyword args.
    """
    pass

def DateTimeDelta(days, hours=0.0, minutes=0.0, seconds=0.0): # real signature unknown; restored from __doc__
    """
    DateTimeDelta(days[,hours=0.0,minutes=0.0,seconds=0.0])
    
    Returns a DateTimeDelta-object reflecting the given
    day and time delta.  Note that the function does not accept
    keyword args.
    """
    pass

def DateTimeDeltaFromDays(days): # real signature unknown; restored from __doc__
    """
    DateTimeDeltaFromDays(days)
    
    Returns a DateTimeDelta-object reflecting the given time
    value given in days (fractions are allowed).
    """
    pass

def DateTimeDeltaFromSeconds(seconds): # real signature unknown; restored from __doc__
    """
    DateTimeDeltaFromSeconds(seconds)
    
    Returns a DateTimeDelta-object reflecting the given time
    value.
    """
    pass

def DateTimeFromAbsDateTime(absdate, abstime=0.0, calendar=None): # real signature unknown; restored from __doc__
    """
    DateTimeFromAbsDateTime(absdate[,abstime=0.0,calendar=Gregorian])
    
    Returns a DateTime-object for the given absolute values.
    Note that the function does not accept keyword args.
    """
    pass

def DateTimeFromAbsDays(absdays): # real signature unknown; restored from __doc__
    """
    DateTimeFromAbsDays(absdays)
    
    Returns a DateTime-object reflecting the given time
    value (days since the epoch).
    """
    pass

def DateTimeFromCOMDate(comdate): # real signature unknown; restored from __doc__
    """
    DateTimeFromCOMDate(comdate)
    
    Returns a DateTime-object reflecting the given date
    and time.
    """
    pass

def JulianDateTime(year, month=1, day=1, hour=0, minute=0, second=0.0): # real signature unknown; restored from __doc__
    """
    JulianDateTime(year,month=1,day=1,hour=0,minute=0,second=0.0)
    
    Returns a DateTime-object reflecting the given Julian date
    and time. Seconds can be given as float to indicate
    fractions.  Note that the function does not accept keyword args.
    """
    pass

def now(): # real signature unknown; restored from __doc__
    """
    now()
    
    Returns a DateTime-object reflecting the current local time.
    """
    pass

def setnowapi(fct): # real signature unknown; restored from __doc__
    """
    setnowapi(fct)
    
    Sets the current time API used by now(). This must be
    a callable function which returns the current local time in
    Unix ticks.
    """
    pass

def strptime(p_str, formatstr, default=None): # real signature unknown; restored from __doc__
    """
    strptime(str,formatstr,default=None)
    
    Returns a DateTime-object reflecting the parsed
    date and time; default can be given to set default values
    for parts not given in the string. If not given,
    1.1.0001 0:00:00.00 is used instead.
    """
    pass

def utc(): # real signature unknown; restored from __doc__
    """
    utc()
    
    Returns a DateTime-object reflecting the current UTC time.
    """
    pass

# classes

class DateTimeDeltaType(object):
    # no doc
    def absvalues(self): # real signature unknown; restored from __doc__
        """
        absvalues()
        
        Return a (absdays,absseconds) tuple. The absseconds part is
        normalized in such way that it is always < 86400.0. The
        values can be used to do date/time calculations.
        Both are signed.
        """
        pass

    def pytime(self): # real signature unknown; restored from __doc__
        """
        pytime()
        
        Returns a datetime.time object with the same values.
        """
        pass

    def pytimedelta(self): # real signature unknown; restored from __doc__
        """
        pytimedelta()
        
        Returns a datetime.timedelta object with the same values.
        """
        pass

    def rebuild(self, day=None, hour=None, minute=None, second=None): # real signature unknown; restored from __doc__
        """
        rebuild(day=None,hour=None,minute=None,second=None)
        
        Returns a DateTimeDelta object with the given time values
        replaced by new values.
        """
        pass

    def strftime(self, formatstr): # real signature unknown; restored from __doc__
        """
        strftime(formatstr)
        
        Returns a formatted string of the time (ignoring the sign).
        Of course, it only makes sense to use time related
        specifiers. The delta sign is not taken into account.
        All values are shown positive.
        """
        pass

    def tuple(self): # real signature unknown; restored from __doc__
        """
        tuple()
        
        Return a (day,hour,minute,second) tuple. The values are all
        signed and use the same conventions as the attributes of
        the same name.
        """
        pass

    def __abs__(self): # real signature unknown; restored from __doc__
        """ x.__abs__() <==> abs(x) """
        pass

    def __add__(self, y): # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
        pass

    def __cmp__(self, y): # real signature unknown; restored from __doc__
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        """
        copy([memo])
        Return a new reference for the instance. This function
        is used for the copy-protocol. Real copying doesn't take
        place, since the instances are immutable.
        """
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        """
        copy([memo])
        Return a new reference for the instance. This function
        is used for the copy-protocol. Real copying doesn't take
        place, since the instances are immutable.
        """
        pass

    def __divmod__(self, y): # real signature unknown; restored from __doc__
        """ x.__divmod__(y) <==> divmod(x, y) """
        pass

    def __div__(self, y): # real signature unknown; restored from __doc__
        """ x.__div__(y) <==> x/y """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __float__(self): # real signature unknown; restored from __doc__
        """ x.__float__() <==> float(x) """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ x.__int__() <==> int(x) """
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __mod__(self, y): # real signature unknown; restored from __doc__
        """ x.__mod__(y) <==> x%y """
        pass

    def __mul__(self, y): # real signature unknown; restored from __doc__
        """ x.__mul__(y) <==> x*y """
        pass

    def __neg__(self): # real signature unknown; restored from __doc__
        """ x.__neg__() <==> -x """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __nonzero__(self): # real signature unknown; restored from __doc__
        """ x.__nonzero__() <==> x != 0 """
        pass

    def __pos__(self): # real signature unknown; restored from __doc__
        """ x.__pos__() <==> +x """
        pass

    def __pow__(self, y, z=None): # real signature unknown; restored from __doc__
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __radd__(self, y): # real signature unknown; restored from __doc__
        """ x.__radd__(y) <==> y+x """
        pass

    def __rdivmod__(self, y): # real signature unknown; restored from __doc__
        """ x.__rdivmod__(y) <==> divmod(y, x) """
        pass

    def __rdiv__(self, y): # real signature unknown; restored from __doc__
        """ x.__rdiv__(y) <==> y/x """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __rmod__(self, y): # real signature unknown; restored from __doc__
        """ x.__rmod__(y) <==> y%x """
        pass

    def __rmul__(self, y): # real signature unknown; restored from __doc__
        """ x.__rmul__(y) <==> y*x """
        pass

    def __rpow__(self, x, z=None): # real signature unknown; restored from __doc__
        """ y.__rpow__(x[, z]) <==> pow(x, y[, z]) """
        pass

    def __rsub__(self, y): # real signature unknown; restored from __doc__
        """ x.__rsub__(y) <==> y-x """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    def __sub__(self, y): # real signature unknown; restored from __doc__
        """ x.__sub__(y) <==> x-y """
        pass


class DateTimeType(object):
    # no doc
    def absvalues(self): # real signature unknown; restored from __doc__
        """ absvalues() """
        pass

    def COMDate(self): # real signature unknown; restored from __doc__
        """
        COMDate()
        
        Return a float where the whole part is the number of days
        in the Gregorian calendar since 30.12.1899 and the fraction
        part equals abstime/86400.0.
        """
        pass

    def Format(self, *args, **kwargs): # real signature unknown
        """ strftime(formatstr) """
        pass

    def gmticks(self, offset=0.0): # real signature unknown; restored from __doc__
        """
        gmticks(offset=0.0)
        
        Return a time.time()-like value, representing the objects
        value assuming it is UTC time. offset is subtracted from
        the resulting ticks value.
        """
        pass

    def gmtime(self): # real signature unknown; restored from __doc__
        """
        gmtime()
        
        Returns a DateTime instance representing datetime in UTC
        time assuming that the stored values refer to local time.
        """
        pass

    def gmtoffset(self): # real signature unknown; restored from __doc__
        """
        gmtoffset()
        
        Returns a DateTimeDelta instance representing the UTC offset
        for datetime assuming that the stored values refer to local
        time. If you subtract this value from datetime, you'll get
        UTC time.
        """
        pass

    def Gregorian(self): # real signature unknown; restored from __doc__
        """
        Gregorian()
        Return an instance pointing to the same date and time,
        but using the Gregorian calendar. If the instance already
        uses the Gregorian calendar, a new reference to it is returned.
        """
        pass

    def Julian(self): # real signature unknown; restored from __doc__
        """
        Julian()
        Return an instance pointing to the same date and time,
        but using the Julian calendar. If the instance already
        uses the Julian calendar, a new reference to it is returned.
        """
        pass

    def localtime(self): # real signature unknown; restored from __doc__
        """
        localtime()
        
        Returns a DateTime instance representing datetime in local
        time assuming that the stored values refer to UTC time.
        """
        pass

    def pydate(self): # real signature unknown; restored from __doc__
        """
        pydate()
        
        Returns a datetime.date object with just the date values.
        """
        pass

    def pydatetime(self): # real signature unknown; restored from __doc__
        """
        pydatetime()
        
        Returns a datetime.datetime object with the same values.
        """
        pass

    def pytime(self): # real signature unknown; restored from __doc__
        """
        pytime()
        
        Returns a datetime.time object with just the time values.
        """
        pass

    def rebuild(self, year=None, month=None, day=None, hour=None, minute=None, second=None): # real signature unknown; restored from __doc__
        """
        rebuild(year=None,month=None,day=None,hour=None,minute=None,second=None)
        
        Returns a DateTime-object with the given date/time values
        replaced by new values.
        """
        pass

    def strftime(self, formatstr): # real signature unknown; restored from __doc__
        """ strftime(formatstr) """
        pass

    def ticks(self, offset=0.0, dst=-1): # real signature unknown; restored from __doc__
        """
        ticks([offset=0.0,dst=-1])
        
        Return a time.time()-like value, representing the objects
        value assuming it is local time. The conversion is done
        using mktime() with the DST flag set to dst. offset is
        subtracted from the resulting ticks value.
        """
        pass

    def timetuple(self, *args, **kwargs): # real signature unknown
        """
        tuple()
        Return a (year,month,day,hour,minute,second,day_of_week,
        day_of_year,dst) tuple.
        """
        pass

    def tuple(self): # real signature unknown; restored from __doc__
        """
        tuple()
        Return a (year,month,day,hour,minute,second,day_of_week,
        day_of_year,dst) tuple.
        """
        pass

    def weekday(self, *args, **kwargs): # real signature unknown
        """
        weekdday()
        Return the day of the week as integer; same as .day_of_week.
        This API is needed for datetime.date() compatibility.
        """
        pass

    def __add__(self, y): # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
        pass

    def __cmp__(self, y): # real signature unknown; restored from __doc__
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        """
        copy([memo])
        
        Return a new reference for the instance. This function
        is used for the copy-protocol. Real copying doesn't take
        place, since the instances are immutable.
        """
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        """
        copy([memo])
        
        Return a new reference for the instance. This function
        is used for the copy-protocol. Real copying doesn't take
        place, since the instances are immutable.
        """
        pass

    def __divmod__(self, y): # real signature unknown; restored from __doc__
        """ x.__divmod__(y) <==> divmod(x, y) """
        pass

    def __div__(self, y): # real signature unknown; restored from __doc__
        """ x.__div__(y) <==> x/y """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __float__(self): # real signature unknown; restored from __doc__
        """ x.__float__() <==> float(x) """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ x.__int__() <==> int(x) """
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __mod__(self, y): # real signature unknown; restored from __doc__
        """ x.__mod__(y) <==> x%y """
        pass

    def __mul__(self, y): # real signature unknown; restored from __doc__
        """ x.__mul__(y) <==> x*y """
        pass

    def __neg__(self): # real signature unknown; restored from __doc__
        """ x.__neg__() <==> -x """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __nonzero__(self): # real signature unknown; restored from __doc__
        """ x.__nonzero__() <==> x != 0 """
        pass

    def __pos__(self): # real signature unknown; restored from __doc__
        """ x.__pos__() <==> +x """
        pass

    def __pow__(self, y, z=None): # real signature unknown; restored from __doc__
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __radd__(self, y): # real signature unknown; restored from __doc__
        """ x.__radd__(y) <==> y+x """
        pass

    def __rdivmod__(self, y): # real signature unknown; restored from __doc__
        """ x.__rdivmod__(y) <==> divmod(y, x) """
        pass

    def __rdiv__(self, y): # real signature unknown; restored from __doc__
        """ x.__rdiv__(y) <==> y/x """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __rmod__(self, y): # real signature unknown; restored from __doc__
        """ x.__rmod__(y) <==> y%x """
        pass

    def __rmul__(self, y): # real signature unknown; restored from __doc__
        """ x.__rmul__(y) <==> y*x """
        pass

    def __rpow__(self, x, z=None): # real signature unknown; restored from __doc__
        """ y.__rpow__(x[, z]) <==> pow(x, y[, z]) """
        pass

    def __rsub__(self, y): # real signature unknown; restored from __doc__
        """ x.__rsub__(y) <==> y-x """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    def __sub__(self, y): # real signature unknown; restored from __doc__
        """ x.__sub__(y) <==> x-y """
        pass


class Error(ValueError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class RangeError(__mx_DateTime.Error):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

mxDateTimeAPI2 = None # (!) real value is ''

