# encoding: utf-8
# module pandas.tslib
# from /usr/local/lib/python2.7/dist-packages/pandas/tslib.so
# by generator 1.138
# no doc

# imports
import collections as collections # /usr/lib/python2.7/collections.pyc
import locale as locale # /usr/lib/python2.7/locale.pyc
import calendar as calendar # /usr/lib/python2.7/calendar.pyc
import re as re # /usr/lib/python2.7/re.pyc
import operator as operator # <module 'operator' (built-in)>
import numpy as np # /usr/local/lib/python2.7/dist-packages/numpy/__init__.pyc
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import pytz as pytz # /usr/local/lib/python2.7/dist-packages/pytz/__init__.pyc
import time as time # <module 'time' (built-in)>
from datetime import datetime_date, datetime_time

from thread import _thread_allocate_lock

import datetime as __datetime
import dateutil.tz as __dateutil_tz


# Variables with simple values

compat_NaT = None

field = 'dayofweek'

have_pytz = True

IGNORECASE = 2

iNaT = -9223372036854775808

_CACHE_MAX_SIZE = 5

_maybe_method_name = 'year'

_method_name = 'total_seconds'

# functions

def apply_offset(*args, **kwargs): # real signature unknown
    pass

def array_strptime(*args, **kwargs): # real signature unknown
    """
    Parameters
        ----------
        values : ndarray of string-like objects
        fmt : string-like regex
        exact : matches must be exact if True, search if False
        coerce : if invalid values found, coerce to NaT
    """
    pass

def array_to_datetime(*args, **kwargs): # real signature unknown
    pass

def array_to_timedelta64(*args, **kwargs): # real signature unknown
    """
    convert an ndarray to an array of ints that are timedeltas
            force conversion if coerce = True,
            else will raise if cannot convert
    """
    pass

def build_field_sarray(*args, **kwargs): # real signature unknown
    """ Datetime as int64 representation to a structured array of fields """
    pass

def callable(p_object): # real signature unknown; restored from __doc__
    """
    callable(object) -> bool
    
    Return whether the object is callable (i.e., some kind of function).
    Note that classes are callable, as are instances with a __call__() method.
    """
    return False

def cast_from_unit(*args, **kwargs): # real signature unknown
    """
    return a casting of the unit represented to nanoseconds
            round the fractional part of a float to our precision, p
    """
    pass

def cast_to_nanoseconds(*args, **kwargs): # real signature unknown
    pass

def convert_str_to_tsobject(*args, **kwargs): # real signature unknown
    pass

def convert_to_timedelta(*args, **kwargs): # real signature unknown
    pass

def dates_normalized(*args, **kwargs): # real signature unknown
    pass

def datetime_to_datetime64(*args, **kwargs): # real signature unknown
    pass

def dateutil_parse(*args, **kwargs): # real signature unknown
    """ lifted from dateutil to get resolution """
    pass

def date_normalize(*args, **kwargs): # real signature unknown
    pass

def format_array_from_datetime(*args, **kwargs): # real signature unknown
    """
    return a np object array of the string formatted values
    
        Parameters
        ----------
        values : a 1-d i8 array
        tz : the timezone (or None)
        format : optional, default is None
              a strftime capable string
        na_rep : optional, default is None
              a nat format
    """
    pass

def get_date_field(*args, **kwargs): # real signature unknown
    """
    Given a int64-based datetime index, extract the year, month, etc.,
        field and return an array of these values.
    """
    pass

def get_start_end_field(*args, **kwargs): # real signature unknown
    """
    Given an int64-based datetime index return array of indicators
        of whether timestamps are at the start/end of the month/quarter/year
        (defined by frequency).
    """
    pass

def get_timezone(*args, **kwargs): # real signature unknown
    pass

def get_time_micros(*args, **kwargs): # real signature unknown
    """ Datetime as int64 representation to a structured array of fields """
    pass

def get_value_box(*args, **kwargs): # real signature unknown
    pass

def i8_to_pydt(*args, **kwargs): # real signature unknown
    """ Inverse of pydt_to_i8 """
    pass

def ints_to_pydatetime(*args, **kwargs): # real signature unknown
    pass

def ints_to_pytimedelta(*args, **kwargs): # real signature unknown
    pass

def isleapyear(*args, **kwargs): # real signature unknown
    pass

def is_platform_windows(): # reliably restored by inspect
    # no doc
    pass

def is_timestamp_array(*args, **kwargs): # real signature unknown
    pass

def iteritems(obj, **kwargs): # reliably restored by inspect
    """
    replacement for six's iteritems for Python2/3 compat
           uses 'iteritems' if available and otherwise uses 'items'.
    
           Passes kwargs to method.
    """
    pass

def maybe_get_tz(*args, **kwargs): # real signature unknown
    """
    (Maybe) Construct a timezone object from a string. If tz is a string, use it to construct a timezone object.
        Otherwise, just return tz.
    """
    pass

def monthrange(*args, **kwargs): # real signature unknown
    pass

def normalize_date(*args, **kwargs): # real signature unknown
    """
    Normalize datetime.datetime value to midnight. Returns datetime.date as a
        datetime.datetime at midnight
    
        Returns
        -------
        normalized : datetime.datetime or Timestamp
    """
    pass

def parse_date(timestr, *args, **kwargs): # reliably restored by inspect
    # no doc
    pass

def parse_datetime_string(*args, **kwargs): # real signature unknown
    """
    parse datetime string, only returns datetime.
        Also cares special handling matching time patterns.
    
        Returns
        -------
        datetime
    """
    pass

def parse_datetime_string_with_reso(*args, **kwargs): # real signature unknown
    """
    parse datetime string, only returns datetime
    
        Returns
        -------
        datetime
    """
    pass

def parse_str_array_to_datetime(*args, **kwargs): # real signature unknown
    """ Shortcut to parse str array for quicker DatetimeIndex construction """
    pass

def pydt_to_i8(*args, **kwargs): # real signature unknown
    """
    Convert to int64 representation compatible with numpy datetime64; converts
        to UTC
    """
    pass

def re_compile(pattern, flags=0): # reliably restored by inspect
    """ Compile a regular expression pattern, returning a pattern object. """
    pass

def re_escape(pattern): # reliably restored by inspect
    """ Escape all non-alphanumeric characters in pattern. """
    pass

def shift_months(*args, **kwargs): # real signature unknown
    """
    Given an int64-based datetime index, shift all elements
        specified number of months using DateOffset semantics
    
        day: {None, 'start', 'end'}
           * None: day of month
           * 'start' 1st day of month
           * 'end' last day of month
    """
    pass

def tot_seconds(*args, **kwargs): # real signature unknown
    pass

def tz_convert(*args, **kwargs): # real signature unknown
    pass

def tz_convert_single(*args, **kwargs): # real signature unknown
    pass

def tz_localize_to_utc(*args, **kwargs): # real signature unknown
    """
    Localize tzinfo-naive DateRange to given time zone (using pytz). If
        there are ambiguities in the values, raise AmbiguousTimeError.
    
        Returns
        -------
        localized : DatetimeIndex
    """
    pass

def unique_deltas(*args, **kwargs): # real signature unknown
    pass

def _dateutil_gettz(name=None): # reliably restored by inspect
    # no doc
    pass

def _delta_to_nanoseconds(*args, **kwargs): # real signature unknown
    pass

def _does_string_look_like_datetime(*args, **kwargs): # real signature unknown
    pass

def _getlang(*args, **kwargs): # real signature unknown
    pass

def _get_rule_month(D): # real signature unknown; restored from __doc__
    """
    Return starting month of given freq, default is December.
    
        Example
        -------
        >>> _get_rule_month('D')
        'DEC'
    
        >>> _get_rule_month('A-JAN')
        'JAN'
    """
    pass

def _get_utcoffset(*args, **kwargs): # real signature unknown
    pass

def _localize_pydatetime(*args, **kwargs): # real signature unknown
    """ Take a datetime/Timestamp in UTC and localizes to timezone tz. """
    pass

def _make_error_func(*args, **kwargs): # real signature unknown
    pass

def _make_nan_func(*args, **kwargs): # real signature unknown
    pass

def _make_nat_func(*args, **kwargs): # real signature unknown
    pass

def _p_tz_cache_key(*args, **kwargs): # real signature unknown
    """ Python interface for cache function to facilitate testing. """
    pass

def _unbox_utcoffsets(*args, **kwargs): # real signature unknown
    pass

def __nat_unpickle(*args, **kwargs): # real signature unknown
    pass

# classes

class Components(tuple):
    """ Components(days, hours, minutes, seconds, milliseconds, microseconds, nanoseconds) """
    def _asdict(self, *args, **kwargs): # real signature unknown
        """ Return a new OrderedDict which maps field names to their values """
        pass

    @classmethod
    def _make(cls, *args, **kwargs): # real signature unknown
        """ Make a new Components object from a sequence or iterable """
        pass

    def _replace(self, *args, **kwargs): # real signature unknown
        """ Return a new Components object replacing specified fields with new values """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
        """ Return self as a plain tuple.  Used by copy and pickle. """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        """ Exclude the OrderedDict from pickling """
        pass

    def __init__(self, days, hours, minutes, seconds, milliseconds, microseconds, nanoseconds): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(_cls, days, hours, minutes, seconds, milliseconds, microseconds, nanoseconds): # reliably restored by inspect
        """ Create new instance of Components(days, hours, minutes, seconds, milliseconds, microseconds, nanoseconds) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return a nicely formatted representation string """
        pass

    days = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 0"""

    hours = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 1"""

    microseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 5"""

    milliseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 4"""

    minutes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 2"""

    nanoseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 6"""

    seconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 3"""


    _fields = (
        'days',
        'hours',
        'minutes',
        'seconds',
        'milliseconds',
        'microseconds',
        'nanoseconds',
    )
    __dict__ = None # (!) real value is ''
    __slots__ = ()


class DateParseError(ValueError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __qualname__ = 'DateParseError'


class LocaleTime(object):
    """
    Stores and handles locale-specific information related to time.
    
        ATTRIBUTES:
            f_weekday -- full weekday names (7-item list)
            a_weekday -- abbreviated weekday names (7-item list)
            f_month -- full month names (13-item list; dummy value in [0], which
                        is added by code)
            a_month -- abbreviated month names (13-item list, dummy value in
                        [0], which is added by code)
            am_pm -- AM/PM representation (2-item list)
            LC_date_time -- format string for date/time representation (string)
            LC_date -- format string for date representation (string)
            LC_time -- format string for time representation (string)
            timezone -- daylight- and non-daylight-savings timezone representation
                        (2-item list of sets)
            lang -- Language used by instance (2-item tuple)
    """
    def _LocaleTime__calc_am_pm(self, *args, **kwargs): # real signature unknown
        pass

    def _LocaleTime__calc_date_time(self, *args, **kwargs): # real signature unknown
        pass

    def _LocaleTime__calc_month(self, *args, **kwargs): # real signature unknown
        pass

    def _LocaleTime__calc_timezone(self, *args, **kwargs): # real signature unknown
        pass

    def _LocaleTime__calc_weekday(self, *args, **kwargs): # real signature unknown
        pass

    def _LocaleTime__pad(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Set all attributes.
        
                Order of methods called matters for dependency reasons.
        
                The locale language is set at the offset and then checked again before
                exiting.  This is to make sure that the attributes were not set with a
                mix of information from more than one locale.  This would most likely
                happen when using threads where one thread calls a locale-dependent
                function while another thread changes the locale while the function in
                the other thread is still running.  Proper coding would call for
                locks to prevent changing the locale while locale-dependent code is
                running.  The check here is done in case someone does not think about
                doing this.
        
                Only other possible issue is if someone changed the timezone and did
                not call tz.tzset .  That is an issue for the programmer, though,
                since changing the timezone is worthless without that call.
        """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __qualname__ = 'LocaleTime'


class _Timestamp(__datetime.datetime):
    # no doc
    def to_datetime(self, *args, **kwargs): # real signature unknown
        pass

    def to_datetime64(self, *args, **kwargs): # real signature unknown
        """ Returns a numpy.datetime64 object with 'ns' precision """
        pass

    def _get_field(self, *args, **kwargs): # real signature unknown
        pass

    def _get_start_end_field(self, *args, **kwargs): # real signature unknown
        pass

    def __add__(self, y): # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
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

    def __radd__(self, y): # real signature unknown; restored from __doc__
        """ x.__radd__(y) <==> y+x """
        pass

    def __rsub__(self, y): # real signature unknown; restored from __doc__
        """ x.__rsub__(y) <==> y-x """
        pass

    def __sub__(self, y): # real signature unknown; restored from __doc__
        """ x.__sub__(y) <==> x-y """
        pass

    nanosecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class _NaT(_Timestamp):
    # no doc
    def __add__(self, y): # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
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

    def __radd__(self, y): # real signature unknown; restored from __doc__
        """ x.__radd__(y) <==> y+x """
        pass

    def __rsub__(self, y): # real signature unknown; restored from __doc__
        """ x.__rsub__(y) <==> y-x """
        pass

    def __sub__(self, y): # real signature unknown; restored from __doc__
        """ x.__sub__(y) <==> x-y """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class NaTType(_NaT):
    """ (N)ot-(A)-(T)ime, the time equivalent of NaN """
    def astimezone(self, *args, **kwargs): # real signature unknown
        pass

    def combine(self, *args, **kwargs): # real signature unknown
        pass

    def ctime(self, *args, **kwargs): # real signature unknown
        pass

    def date(self, *args, **kwargs): # real signature unknown
        pass

    def dst(self, *args, **kwargs): # real signature unknown
        pass

    def fromordinal(self, *args, **kwargs): # real signature unknown
        pass

    def fromtimestamp(self, *args, **kwargs): # real signature unknown
        pass

    def isocalendar(self, *args, **kwargs): # real signature unknown
        pass

    def isoformat(self, *args, **kwargs): # real signature unknown
        pass

    def isoweekday(self, *args, **kwargs): # real signature unknown
        pass

    def now(self, *args, **kwargs): # real signature unknown
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        pass

    def strftime(self, *args, **kwargs): # real signature unknown
        pass

    def strptime(self, *args, **kwargs): # real signature unknown
        pass

    def time(self, *args, **kwargs): # real signature unknown
        pass

    def timetuple(self, *args, **kwargs): # real signature unknown
        pass

    def timetz(self, *args, **kwargs): # real signature unknown
        pass

    def today(self, *args, **kwargs): # real signature unknown
        pass

    def toordinal(self, *args, **kwargs): # real signature unknown
        pass

    def total_seconds(self, *args, **kwargs): # real signature unknown
        pass

    def to_datetime(self, *args, **kwargs): # real signature unknown
        pass

    def tzname(self, *args, **kwargs): # real signature unknown
        pass

    def utcfromtimestamp(self, *args, **kwargs): # real signature unknown
        pass

    def utcnow(self, *args, **kwargs): # real signature unknown
        pass

    def utcoffset(self, *args, **kwargs): # real signature unknown
        pass

    def utctimetuple(self, *args, **kwargs): # real signature unknown
        pass

    def weekday(self, *args, **kwargs): # real signature unknown
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        pass

    def __long__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        pass

    day = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dayofweek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dayofyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    daysinmonth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    days_in_month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    microsecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    millisecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    minute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nanosecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    quarter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    second = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    week = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __qualname__ = 'NaTType'


class OutOfBoundsDatetime(ValueError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __qualname__ = 'OutOfBoundsDatetime'


class relativedelta:
    """
    The relativedelta type is based on the specification of the excelent
    work done by M.-A. Lemburg in his mx.DateTime extension. However,
    notice that this type does *NOT* implement the same algorithm as
    his work. Do *NOT* expect it to behave like mx.DateTime's counterpart.
    
    There's two different ways to build a relativedelta instance. The
    first one is passing it two date/datetime classes:
    
        relativedelta(datetime1, datetime2)
    
    And the other way is to use the following keyword arguments:
    
        year, month, day, hour, minute, second, microsecond:
            Absolute information.
    
        years, months, weeks, days, hours, minutes, seconds, microseconds:
            Relative information, may be negative.
    
        weekday:
            One of the weekday instances (MO, TU, etc). These instances may
            receive a parameter N, specifying the Nth weekday, which could
            be positive or negative (like MO(+1) or MO(-2). Not specifying
            it is the same as specifying +1. You can also use an integer,
            where 0=MO.
    
        leapdays:
            Will add given days to the date found, if year is a leap
            year, and the date found is post 28 of february.
    
        yearday, nlyearday:
            Set the yearday or the non-leap year day (jump leap days).
            These are converted to day/month/leapdays information.
    
    Here is the behavior of operations with relativedelta:
    
    1) Calculate the absolute year, using the 'year' argument, or the
       original datetime year, if the argument is not present.
    
    2) Add the relative 'years' argument to the absolute year.
    
    3) Do steps 1 and 2 for month/months.
    
    4) Calculate the absolute day, using the 'day' argument, or the
       original datetime day, if the argument is not present. Then,
       subtract from the day until it fits in the year and month
       found after their operations.
    
    5) Add the relative 'days' argument to the absolute day. Notice
       that the 'weeks' argument is multiplied by 7 and added to
       'days'.
    
    6) Do steps 1 and 2 for hour/hours, minute/minutes, second/seconds,
       microsecond/microseconds.
    
    7) If the 'weekday' argument is present, calculate the weekday,
       with the given (wday, nth) tuple. wday is the index of the
       weekday (0-6, 0=Mon), and nth is the number of weeks to add
       forward or backward, depending on its signal. Notice that if
       the calculated date is already Monday, for example, using
       (0, 1) or (0, -1) won't change the day.
    """
    def _fix(self, *args, **kwargs): # real signature unknown
        pass

    def _set_months(self, *args, **kwargs): # real signature unknown
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        pass

    def __div__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        pass

    def __nonzero__(self, *args, **kwargs): # real signature unknown
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        pass


class StringIO:
    """
    class StringIO([buffer])
    
        When a StringIO object is created, it can be initialized to an existing
        string by passing the string to the constructor. If no string is given,
        the StringIO will start empty.
    
        The StringIO object can accept either Unicode or 8-bit strings, but
        mixing the two may take some care. If both are used, 8-bit strings that
        cannot be interpreted as 7-bit ASCII (that use the 8th bit) will cause
        a UnicodeError to be raised when getvalue() is called.
    """
    def close(self, *args, **kwargs): # real signature unknown
        """ Free the memory buffer. """
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        """ Flush the internal buffer """
        pass

    def getvalue(self): # real signature unknown; restored from __doc__
        """
        Retrieve the entire contents of the "file" at any time before
                the StringIO object's close() method is called.
        
                The StringIO object can accept either Unicode or 8-bit strings,
                but mixing the two may take some care. If both are used, 8-bit
                strings that cannot be interpreted as 7-bit ASCII (that use the
                8th bit) will cause a UnicodeError to be raised when getvalue()
                is called.
        """
        pass

    def isatty(self, *args, **kwargs): # real signature unknown
        """
        Returns False because StringIO objects are not connected to a
                tty-like device.
        """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """
        A file object is its own iterator, for example iter(f) returns f
                (unless f is closed). When a file is used as an iterator, typically
                in a for loop (for example, for line in f: print line), the next()
                method is called repeatedly. This method returns the next input line,
                or raises StopIteration when EOF is hit.
        """
        pass

    def read(self, *args, **kwargs): # real signature unknown
        """
        Read at most size bytes from the file
                (less if the read hits EOF before obtaining size bytes).
        
                If the size argument is negative or omitted, read all data until EOF
                is reached. The bytes are returned as a string object. An empty
                string is returned when EOF is encountered immediately.
        """
        pass

    def readline(self, *args, **kwargs): # real signature unknown
        """
        Read one entire line from the file.
        
                A trailing newline character is kept in the string (but may be absent
                when a file ends with an incomplete line). If the size argument is
                present and non-negative, it is a maximum byte count (including the
                trailing newline) and an incomplete line may be returned.
        
                An empty string is returned only when EOF is encountered immediately.
        
                Note: Unlike stdio's fgets(), the returned string contains null
                characters ('\0') if they occurred in the input.
        """
        pass

    def readlines(self, *args, **kwargs): # real signature unknown
        """
        Read until EOF using readline() and return a list containing the
                lines thus read.
        
                If the optional sizehint argument is present, instead of reading up
                to EOF, whole lines totalling approximately sizehint bytes (or more
                to accommodate a final whole line).
        """
        pass

    def seek(self, *args, **kwargs): # real signature unknown
        """
        Set the file's current position.
        
                The mode argument is optional and defaults to 0 (absolute file
                positioning); other values are 1 (seek relative to the current
                position) and 2 (seek relative to the file's end).
        
                There is no return value.
        """
        pass

    def tell(self, *args, **kwargs): # real signature unknown
        """ Return the file's current position. """
        pass

    def truncate(self, *args, **kwargs): # real signature unknown
        """
        Truncate the file's size.
        
                If the optional size argument is present, the file is truncated to
                (at most) that size. The size defaults to the current position.
                The current file position is not changed unless the position
                is beyond the new file size.
        
                If the specified size exceeds the file's current size, the
                file remains unchanged.
        """
        pass

    def write(self, *args, **kwargs): # real signature unknown
        """
        Write a string to the file.
        
                There is no return value.
        """
        pass

    def writelines(self): # real signature unknown; restored from __doc__
        """
        Write a sequence of strings to the file. The sequence can be any
                iterable object producing strings, typically a list of strings. There
                is no return value.
        
                (The name is intended to match readlines(); writelines() does not add
                line separators.)
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        pass


class _Timedelta(__datetime.timedelta):
    # no doc
    def to_pytimedelta(self, *args, **kwargs): # real signature unknown
        """
        return an actual datetime.timedelta object
                note: we lose nanosecond resolution if any
        """
        pass

    def _ensure_components(self, *args, **kwargs): # real signature unknown
        """ compute the components """
        pass

    def _has_ns(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
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

    freq = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_populated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _d = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _h = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _m = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _ms = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _ns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _s = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _sign = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _us = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class Timedelta(_Timedelta):
    """
    Represents a duration, the difference between two dates or times.
    
        Timedelta is the pandas equivalent of python's ``datetime.timedelta``
        and is interchangable with it in most cases.
    
        Parameters
        ----------
        value : Timedelta, timedelta, np.timedelta64, string, or integer
        unit : string, [D,h,m,s,ms,us,ns]
            Denote the unit of the input, if input is an integer. Default 'ns'.
        days, seconds, microseconds, milliseconds, minutes, hours, weeks : numeric, optional
            Values for construction in compat with datetime.timedelta.
            np ints and floats will be coereced to python ints and floats.
    
        Notes
        -----
        The ``.value`` attribute is always in ns.
    """
    def round(self, *args, **kwargs): # real signature unknown
        """
        return a new Timedelta rounded to this resolution
        
                Parameters
                ----------
                reso : a string indicating the rouding resolution, accepting values
                   d,h,m,s,ms,us
        """
        pass

    def total_seconds(self, *args, **kwargs): # real signature unknown
        """ Total duration of timedelta in seconds (to ns precision) """
        pass

    def to_timedelta64(self, *args, **kwargs): # real signature unknown
        """ Returns a numpy.timedelta64 object with 'ns' precision """
        pass

    def view(self, *args, **kwargs): # real signature unknown
        """ array view compat """
        pass

    def _binary_op_method_timedeltalike(self, *args, **kwargs): # real signature unknown
        pass

    def _not_implemented(self, *args, **kwargs): # real signature unknown
        pass

    def _op_unary_method(self, *args, **kwargs): # real signature unknown
        pass

    def _repr_base(self, *args, **kwargs): # real signature unknown
        """
        Parameters
                ----------
                format : None|all|even_day|sub_day|long
        
                Returns
                -------
                converted : string of a Timedelta
        """
        pass

    def _validate_ops_compat(self, *args, **kwargs): # real signature unknown
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        pass

    def __div__(self, *args, **kwargs): # real signature unknown
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __inv__(self, *args, **kwargs): # real signature unknown
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        pass

    def __rdiv__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        pass

    asm8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ return a numpy timedelta64 array view of myself """

    components = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Return a Components NamedTuple-like """

    days = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Number of Days

        .components will return the shown components
        """

    delta = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ return out delta in ns (for internal compat) """

    microseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Number of microseconds (>= 0 and less than 1 second).

        .components will return the shown components
        """

    nanoseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Number of nanoseconds (>= 0 and less than 1 microsecond).

        .components will return the shown components
        """

    resolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ return a string representing the lowest resolution that we have """

    seconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Number of seconds (>= 0 and less than 1 day).

        .components will return the shown components
        """

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __array_priority__ = 100
    __dict__ = None # (!) real value is ''
    __qualname__ = 'Timedelta'


class TimeRE(dict):
    """ Handle conversion from format directives to regexes. """
    def compile(self, *args, **kwargs): # real signature unknown
        """ Return a compiled re object for the format string. """
        pass

    def pattern(self, *args, **kwargs): # real signature unknown
        """
        Return regex pattern for the format string.
        
                Need to make sure that any characters that might be interpreted as
                regex syntax are escaped.
        """
        pass

    def _TimeRE__seqToRE(self, *args, **kwargs): # real signature unknown
        """
        Convert a list to a regex string for matching a directive.
        
                Want possible matching values to be from longest to shortest.  This
                prevents the possibility of a match occuring for a value that also
                a substring of a larger value that should have matched (e.g., 'abc'
                matching when 'abcdef' should have been the match).
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Create keys/values.
        
                Order of execution is important for dependency reasons.
        """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __qualname__ = 'TimeRE'


class Timestamp(_Timestamp):
    """
    TimeStamp is the pandas equivalent of python's Datetime
        and is interchangable with it in most cases. It's the type used
        for the entries that make up a DatetimeIndex, and other timeseries
        oriented data structures in pandas.
    
        Parameters
        ----------
        ts_input : datetime-like, str, int, float
            Value to be converted to Timestamp
        offset : str, DateOffset
            Offset which Timestamp will have
        tz : string, pytz.timezone, dateutil.tz.tzfile or None
            Time zone for time which Timestamp will have.
        unit : string
            numpy unit used for conversion, if ts_input is int or float
    """
    def astimezone(self, *args, **kwargs): # real signature unknown
        """
        Convert tz-aware Timestamp to another time zone.
        
                Parameters
                ----------
                tz : string, pytz.timezone, dateutil.tz.tzfile or None
                    Time zone for time which Timestamp will be converted to.
                    None will remove timezone holding UTC time.
        
                Returns
                -------
                converted : Timestamp
        
                Raises
                ------
                TypeError
                    If Timestamp is tz-naive.
        """
        pass

    @classmethod
    def combine(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def fromordinal(cls, *args, **kwargs): # real signature unknown
        """
        passed an ordinal, translate and convert to a ts
                    note: by definition there cannot be any tz info on the ordinal itself
        """
        pass

    @classmethod
    def fromtimestamp(cls, *args, **kwargs): # real signature unknown
        pass

    def isoformat(self, *args, **kwargs): # real signature unknown
        pass

    def normalize(self, *args, **kwargs): # real signature unknown
        """
        Normalize Timestamp to midnight, preserving
                tz information.
        """
        pass

    @classmethod
    def now(cls, tz=None): # real signature unknown; restored from __doc__
        """
        Return the current time in the local timezone.  Equivalent
                to datetime.now([tz])
        
                Parameters
                ----------
                tz : string / timezone object, default None
                    Timezone to localize to
        """
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def today(cls): # real signature unknown; restored from __doc__
        """
        Return the current time in the local timezone.  This differs
                from datetime.today() in that it can be localized to a
                passed timezone.
        
                Parameters
                ----------
                tz : string / timezone object, default None
                    Timezone to localize to
        """
        pass

    def to_julian_date(self, *args, **kwargs): # real signature unknown
        """
        Convert TimeStamp to a Julian Date.
                0 Julian date is noon January 1, 4713 BC.
        """
        pass

    def to_period(self, *args, **kwargs): # real signature unknown
        """ Return an period of which this timestamp is an observation. """
        pass

    def to_pydatetime(self, *args, **kwargs): # real signature unknown
        """ If warn=True, issue warning if nanoseconds is nonzero """
        pass

    def tz_convert(self, *args, **kwargs): # real signature unknown
        """
        Convert tz-aware Timestamp to another time zone.
        
                Parameters
                ----------
                tz : string, pytz.timezone, dateutil.tz.tzfile or None
                    Time zone for time which Timestamp will be converted to.
                    None will remove timezone holding UTC time.
        
                Returns
                -------
                converted : Timestamp
        
                Raises
                ------
                TypeError
                    If Timestamp is tz-naive.
        """
        pass

    def tz_localize(self, *args, **kwargs): # real signature unknown
        """
        Convert naive Timestamp to local time zone, or remove
                timezone from tz-aware Timestamp.
        
                Parameters
                ----------
                tz : string, pytz.timezone, dateutil.tz.tzfile or None
                    Time zone for time which Timestamp will be converted to.
                    None will remove timezone holding local time.
                ambiguous : bool, 'NaT', default 'raise'
                    - bool contains flags to determine if time is dst or not (note
                    that this flag is only applicable for ambiguous fall dst dates)
                    - 'NaT' will return NaT for an ambiguous time
                    - 'raise' will raise an AmbiguousTimeError for an ambiguous time
        
                Returns
                -------
                localized : Timestamp
        
                Raises
                ------
                TypeError
                    If the Timestamp is tz-aware and tz is not None.
        """
        pass

    @classmethod
    def utcfromtimestamp(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def utcnow(cls, *args, **kwargs): # real signature unknown
        pass

    def _has_time_component(self, *args, **kwargs): # real signature unknown
        """
        Returns if the Timestamp has a time component
                in addition to the date part
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    asm8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dayofweek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dayofyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    daysinmonth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    days_in_month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    freq = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    freqstr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_month_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_month_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_quarter_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_quarter_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_year_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_year_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    microsecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    quarter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Alias for tzinfo
        """

    week = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    weekofyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _date_repr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _repr_base = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _time_repr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    max = None # (!) real value is ''
    min = None # (!) real value is ''
    __dict__ = None # (!) real value is ''
    __qualname__ = 'Timestamp'


class tzoffset(__datetime.tzinfo):
    # no doc
    def dst(self, *args, **kwargs): # real signature unknown
        pass

    def tzname(self, *args, **kwargs): # real signature unknown
        pass

    def utcoffset(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ helper for pickle """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


class _dateutil_tzfile(__datetime.tzinfo):
    # no doc
    def dst(self, *args, **kwargs): # real signature unknown
        pass

    def tzname(self, *args, **kwargs): # real signature unknown
        pass

    def utcoffset(self, *args, **kwargs): # real signature unknown
        pass

    def _find_ttinfo(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


class _dateutil_tzlocal(__datetime.tzinfo):
    # no doc
    def dst(self, *args, **kwargs): # real signature unknown
        pass

    def tzname(self, *args, **kwargs): # real signature unknown
        pass

    def utcoffset(self, *args, **kwargs): # real signature unknown
        pass

    def _isdst(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ helper for pickle """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _dst_offset = None # (!) real value is ''
    _std_offset = None # (!) real value is ''
    __dict__ = None # (!) real value is ''


class _dateutil_tzstr(__dateutil_tz.tzrange):
    # no doc
    def _delta(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass


class _dateutil_tzutc(__datetime.tzinfo):
    # no doc
    def dst(self, *args, **kwargs): # real signature unknown
        pass

    def tzname(self, *args, **kwargs): # real signature unknown
        pass

    def utcoffset(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ helper for pickle """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


class _pytz_BaseTzInfo(__datetime.tzinfo):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    zone = None
    _tzname = None
    _utcoffset = None
    __dict__ = None # (!) real value is ''


class _TSObject(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

DEFAULTPARSER = None # (!) real value is ''

dst_cache = {}

fields = [
    'year',
    'quarter',
    'month',
    'day',
    'hour',
    'minute',
    'second',
    'millisecond',
    'microsecond',
    'nanosecond',
    'week',
    'dayofyear',
    'days_in_month',
    'daysinmonth',
    'dayofweek',
]

NaT = None # (!) real value is ''

np_NaT = None # (!) real value is ''

prop = None # (!) real value is ''

string_types = (
    basestring,
)

UTC = pytz.UTC

version_info = None # (!) real value is ''

_cache_lock = None # (!) real value is ''

_DEFAULT_DATETIME = None # (!) real value is ''

_implemented_methods = [
    'to_datetime64',
    'date',
    'now',
    'replace',
    'to_datetime',
    'today',
    'weekday',
    'isoweekday',
    'total_seconds',
]

_maybe_method = None # (!) real value is ''

_MONTHS = [
    'JAN',
    'FEB',
    'MAR',
    'APR',
    'MAY',
    'JUN',
    'JUL',
    'AUG',
    'SEP',
    'OCT',
    'NOV',
    'DEC',
]

_MONTH_ALIASES = {
    1: 'JAN',
    2: 'FEB',
    3: 'MAR',
    4: 'APR',
    5: 'MAY',
    6: 'JUN',
    7: 'JUL',
    8: 'AUG',
    9: 'SEP',
    10: 'OCT',
    11: 'NOV',
    12: 'DEC',
}

_MONTH_NUMBERS = {
    'APR': 3,
    'AUG': 7,
    'DEC': 11,
    'FEB': 1,
    'JAN': 0,
    'JUL': 6,
    'JUN': 5,
    'MAR': 2,
    'MAY': 4,
    'NOV': 10,
    'OCT': 9,
    'SEP': 8,
}

_nan_methods = [
    'weekday',
    'isoweekday',
    'total_seconds',
]

_nat_methods = [
    'date',
    'now',
    'replace',
    'to_datetime',
    'today',
]

_nat_strings = None # (!) real value is ''

_regex_cache = {}

_TimeRE_cache = {
    '%': '%',
    'A': '(?P<A>wednesday|thursday|saturday|tuesday|monday|friday|sunday)',
    'B': '(?P<B>september|february|november|december|january|october|august|march|april|june|july|may)',
    'H': '(?P<H>2[0-3]|[0-1]\\d|\\d)',
    'I': '(?P<I>1[0-2]|0[1-9]|[1-9])',
    'M': '(?P<M>[0-5]\\d|\\d)',
    'S': '(?P<S>6[0-1]|[0-5]\\d|\\d)',
    'U': '(?P<U>5[0-3]|[0-4]\\d|\\d)',
    'W': '(?P<W>5[0-3]|[0-4]\\d|\\d)',
    'X': '(?P<H>2[0-3]|[0-1]\\d|\\d):(?P<M>[0-5]\\d|\\d):(?P<S>6[0-1]|[0-5]\\d|\\d)',
    'Y': '(?P<Y>\\d\\d\\d\\d)',
    'Z': '(?P<Z>brst|utc|brt|gmt)',
    'a': '(?P<a>mon|tue|wed|thu|fri|sat|sun)',
    'b': '(?P<b>jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)',
    'c': '(?P<a>mon|tue|wed|thu|fri|sat|sun)\\s+(?P<b>jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\\s+(?P<d>3[0-1]|[1-2]\\d|0[1-9]|[1-9]| [1-9])\\s+(?P<H>2[0-3]|[0-1]\\d|\\d):(?P<M>[0-5]\\d|\\d):(?P<S>6[0-1]|[0-5]\\d|\\d)\\s+(?P<Y>\\d\\d\\d\\d)',
    'd': '(?P<d>3[0-1]|[1-2]\\d|0[1-9]|[1-9]| [1-9])',
    'f': '(?P<f>[0-9]{1,9})',
    'j': '(?P<j>36[0-6]|3[0-5]\\d|[1-2]\\d\\d|0[1-9]\\d|00[1-9]|[1-9]\\d|0[1-9]|[1-9])',
    'm': '(?P<m>1[0-2]|0[1-9]|[1-9])',
    'p': '(?P<p>am|pm)',
    'w': '(?P<w>[0-6])',
    'x': '(?P<m>1[0-2]|0[1-9]|[1-9])/(?P<d>3[0-1]|[1-2]\\d|0[1-9]|[1-9]| [1-9])/(?P<y>\\d\\d)',
    'y': '(?P<y>\\d\\d)',
}

_zero_time = None # (!) real value is ''

__all__ = []

__pyx_capi__ = {
    '_check_all_nulls': None, # (!) real value is ''
    '_get_dst_info': None, # (!) real value is ''
    '_is_tzlocal': None, # (!) real value is ''
    '_is_utc': None, # (!) real value is ''
    '_nat_scalar_rules': None, # (!) real value is ''
    'convert_to_timedelta64': None, # (!) real value is ''
    'convert_to_tsobject': None, # (!) real value is ''
    'maybe_get_tz': None, # (!) real value is ''
}

__test__ = {
    u'_get_rule_month (line 1826)': u"\n    Return starting month of given freq, default is December.\n\n    Example\n    -------\n    >>> _get_rule_month('D')\n    'DEC'\n\n    >>> _get_rule_month('A-JAN')\n    'JAN'\n    ",
}

