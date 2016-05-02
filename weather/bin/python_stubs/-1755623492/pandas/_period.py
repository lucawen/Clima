# encoding: utf-8
# module pandas._period
# from /usr/local/lib/python2.7/dist-packages/pandas/_period.so
# by generator 1.138
# no doc

# imports
import operator as operator # <module 'operator' (built-in)>
import pandas.compat as compat # /usr/local/lib/python2.7/dist-packages/pandas/compat/__init__.pyc
import numpy as np # /usr/local/lib/python2.7/dist-packages/numpy/__init__.pyc
import pandas.tslib as tslib # /usr/local/lib/python2.7/dist-packages/pandas/tslib.so
import pandas.tseries.offsets as offsets # /usr/local/lib/python2.7/dist-packages/pandas/tseries/offsets.pyc
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import pandas.lib as lib # /usr/local/lib/python2.7/dist-packages/pandas/lib.so
from pandas.tslib import NaT, Timedelta, Timestamp, _get_utcoffset


# Variables with simple values

D_RESO = 5

have_pytz = True

H_RESO = 4

iNaT = -9223372036854775808

MS_RESO = 1

S_RESO = 2

T_RESO = 3

US_RESO = 0

_DIFFERENT_FREQ = 'Input has different freq={1} from Period(freq={0})'

_DIFFERENT_FREQ_INDEX = 'Input has different freq={1} from PeriodIndex(freq={0})'

# functions

def dt64arr_to_periodarr(*args, **kwargs): # real signature unknown
    """
    Convert array of datetime64 values (passed in as 'i8' dtype) to a set of
        periods corresponding to desired frequency, per period convention.
    """
    pass

def extract_ordinals(*args, **kwargs): # real signature unknown
    pass

def get_period_field(*args, **kwargs): # real signature unknown
    pass

def get_period_field_arr(*args, **kwargs): # real signature unknown
    pass

def parse_time_string(arg, freq=None, dayfirst=None, yearfirst=None): # reliably restored by inspect
    """
    Try hard to parse datetime string, leveraging dateutil plus some extra
        goodies like quarter recognition.
    
        Parameters
        ----------
        arg : compat.string_types
        freq : str or DateOffset, default None
            Helps with interpreting time string if supplied
        dayfirst : bool, default None
            If None uses default from print_config
        yearfirst : bool, default None
            If None uses default from print_config
    
        Returns
        -------
        datetime, datetime/dateutil.parser._result, str
    """
    pass

def periodarr_to_dt64arr(*args, **kwargs): # real signature unknown
    """
    Convert array to datetime64 values from a set of ordinals corresponding to
        periods per period convention.
    """
    pass

def period_asfreq(*args, **kwargs): # real signature unknown
    """
    Convert period ordinal from one frequency to another, and if upsampling,
        choose to use start ('S') or end ('E') of period.
    """
    pass

def period_asfreq_arr(*args, **kwargs): # real signature unknown
    """
    Convert int64-array of period ordinals from one frequency to another, and
        if upsampling, choose to use start ('S') or end ('E') of period.
    """
    pass

def period_format(*args, **kwargs): # real signature unknown
    pass

def period_ordinal(*args, **kwargs): # real signature unknown
    pass

def period_ordinal_to_dt64(*args, **kwargs): # real signature unknown
    pass

def resolution(*args, **kwargs): # real signature unknown
    pass

def _ordinal_from_fields(*args, **kwargs): # real signature unknown
    pass

def _quarter_to_myear(*args, **kwargs): # real signature unknown
    pass

def _validate_end_alias(*args, **kwargs): # real signature unknown
    pass

# classes

class Period(object):
    """
    Represents an period of time
    
        Parameters
        ----------
        value : Period or compat.string_types, default None
            The time period represented (e.g., '4Q2005')
        freq : str, default None
            One of pandas period strings or corresponding objects
        year : int, default None
        month : int, default 1
        quarter : int, default None
        day : int, default 1
        hour : int, default 0
        minute : int, default 0
        second : int, default 0
    """
    def asfreq(self, *args, **kwargs): # real signature unknown
        """
        Convert Period to desired frequency, either at the start or end of the
                interval
        
                Parameters
                ----------
                freq : string
                how : {'E', 'S', 'end', 'start'}, default 'end'
                    Start or end of the timespan
        
                Returns
                -------
                resampled : Period
        """
        pass

    @classmethod
    def now(cls, *args, **kwargs): # real signature unknown
        pass

    def strftime(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Returns the string representation of the :class:`Period`, depending
                on the selected :keyword:`format`. :keyword:`format` must be a string
                containing one or several directives.  The method recognizes the same
                directives as the :func:`time.strftime` function of the standard Python
                distribution, as well as the specific additional directives ``%f``,
                ``%F``, ``%q``. (formatting & docs originally from scikits.timeries)
        
                +-----------+--------------------------------+-------+
                | Directive | Meaning                        | Notes |
                +===========+================================+=======+
                | ``%a``    | Locale's abbreviated weekday   |       |
                |           | name.                          |       |
                +-----------+--------------------------------+-------+
                | ``%A``    | Locale's full weekday name.    |       |
                +-----------+--------------------------------+-------+
                | ``%b``    | Locale's abbreviated month     |       |
                |           | name.                          |       |
                +-----------+--------------------------------+-------+
                | ``%B``    | Locale's full month name.      |       |
                +-----------+--------------------------------+-------+
                | ``%c``    | Locale's appropriate date and  |       |
                |           | time representation.           |       |
                +-----------+--------------------------------+-------+
                | ``%d``    | Day of the month as a decimal  |       |
                |           | number [01,31].                |       |
                +-----------+--------------------------------+-------+
                | ``%f``    | 'Fiscal' year without a        | \(1)  |
                |           | century  as a decimal number   |       |
                |           | [00,99]                        |       |
                +-----------+--------------------------------+-------+
                | ``%F``    | 'Fiscal' year with a century   | \(2)  |
                |           | as a decimal number            |       |
                +-----------+--------------------------------+-------+
                | ``%H``    | Hour (24-hour clock) as a      |       |
                |           | decimal number [00,23].        |       |
                +-----------+--------------------------------+-------+
                | ``%I``    | Hour (12-hour clock) as a      |       |
                |           | decimal number [01,12].        |       |
                +-----------+--------------------------------+-------+
                | ``%j``    | Day of the year as a decimal   |       |
                |           | number [001,366].              |       |
                +-----------+--------------------------------+-------+
                | ``%m``    | Month as a decimal number      |       |
                |           | [01,12].                       |       |
                +-----------+--------------------------------+-------+
                | ``%M``    | Minute as a decimal number     |       |
                |           | [00,59].                       |       |
                +-----------+--------------------------------+-------+
                | ``%p``    | Locale's equivalent of either  | \(3)  |
                |           | AM or PM.                      |       |
                +-----------+--------------------------------+-------+
                | ``%q``    | Quarter as a decimal number    |       |
                |           | [01,04]                        |       |
                +-----------+--------------------------------+-------+
                | ``%S``    | Second as a decimal number     | \(4)  |
                |           | [00,61].                       |       |
                +-----------+--------------------------------+-------+
                | ``%U``    | Week number of the year        | \(5)  |
                |           | (Sunday as the first day of    |       |
                |           | the week) as a decimal number  |       |
                |           | [00,53].  All days in a new    |       |
                |           | year preceding the first       |       |
                |           | Sunday are considered to be in |       |
                |           | week 0.                        |       |
                +-----------+--------------------------------+-------+
                | ``%w``    | Weekday as a decimal number    |       |
                |           | [0(Sunday),6].                 |       |
                +-----------+--------------------------------+-------+
                | ``%W``    | Week number of the year        | \(5)  |
                |           | (Monday as the first day of    |       |
                |           | the week) as a decimal number  |       |
                |           | [00,53].  All days in a new    |       |
                |           | year preceding the first       |       |
                |           | Monday are considered to be in |       |
                |           | week 0.                        |       |
                +-----------+--------------------------------+-------+
                | ``%x``    | Locale's appropriate date      |       |
                |           | representation.                |       |
                +-----------+--------------------------------+-------+
                | ``%X``    | Locale's appropriate time      |       |
                |           | representation.                |       |
                +-----------+--------------------------------+-------+
                | ``%y``    | Year without century as a      |       |
                |           | decimal number [00,99].        |       |
                +-----------+--------------------------------+-------+
                | ``%Y``    | Year with century as a decimal |       |
                |           | number.                        |       |
                +-----------+--------------------------------+-------+
                | ``%Z``    | Time zone name (no characters  |       |
                |           | if no time zone exists).       |       |
                +-----------+--------------------------------+-------+
                | ``%%``    | A literal ``'%'`` character.   |       |
                +-----------+--------------------------------+-------+
        
                .. note::
        
                    (1)
                        The ``%f`` directive is the same as ``%y`` if the frequency is
                        not quarterly.
                        Otherwise, it corresponds to the 'fiscal' year, as defined by
                        the :attr:`qyear` attribute.
        
                    (2)
                        The ``%F`` directive is the same as ``%Y`` if the frequency is
                        not quarterly.
                        Otherwise, it corresponds to the 'fiscal' year, as defined by
                        the :attr:`qyear` attribute.
        
                    (3)
                        The ``%p`` directive only affects the output hour field
                        if the ``%I`` directive is used to parse the hour.
        
                    (4)
                        The range really is ``0`` to ``61``; this accounts for leap
                        seconds and the (very rare) double leap seconds.
        
                    (5)
                        The ``%U`` and ``%W`` directives are only used in calculations
                        when the day of the week and the year are specified.
        
                .. rubric::  Examples
        
                    >>> a = Period(freq='Q@JUL', year=2006, quarter=1)
                    >>> a.strftime('%F-Q%q')
                    '2006-Q1'
                    >>> # Output the last month in the quarter of this date
                    >>> a.strftime('%b-%Y')
                    'Oct-2005'
                    >>>
                    >>> a = Period(freq='D', year=2001, month=1, day=1)
                    >>> a.strftime('%d-%b-%Y')
                    '01-Jan-2006'
                    >>> a.strftime('%b. %d, %Y was a %A')
                    'Jan. 01, 2001 was a Monday'
        """
        pass

    def to_timestamp(self, *args, **kwargs): # real signature unknown
        """
        Return the Timestamp representation of the Period at the target
                frequency at the specified end (how) of the Period
        
                Parameters
                ----------
                freq : string or DateOffset, default is 'D' if self.freq is week or
                       longer and 'S' otherwise
                    Target frequency
                how: str, default 'S' (start)
                    'S', 'E'. Can be aliased as case insensitive
                    'Start', 'Finish', 'Begin', 'End'
        
                Returns
                -------
                Timestamp
        """
        pass

    def _add_delta(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def _from_ordinal(cls, *args, **kwargs): # real signature unknown
        """ fast creation from an ordinal and freq that are already validated! """
        pass

    @classmethod
    def _maybe_convert_freq(cls, *args, **kwargs): # real signature unknown
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

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __rsub__(self, y): # real signature unknown; restored from __doc__
        """ x.__rsub__(y) <==> y-x """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    def __sub__(self, y): # real signature unknown; restored from __doc__
        """ x.__sub__(y) <==> x-y """
        pass

    def __unicode__(self, *args, **kwargs): # real signature unknown
        """
        Return a string representation for a particular DataFrame
        
                Invoked by unicode(df) in py2 only. Yields a Unicode String in both
                py2/py3.
        """
        pass

    day = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dayofweek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dayofyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    daysinmonth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    days_in_month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    end_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    freq = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    freqstr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    minute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ordinal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    quarter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    second = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    week = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    weekday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    weekofyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _comparables = [
        'name',
        'freqstr',
    ]
    _typ = 'period'
    __pyx_vtable__ = None # (!) real value is ''


# variables with complex values

version_info = tslib.version_info

__test__ = {
    u'Period.strftime (line 1017)': u"\n        Returns the string representation of the :class:`Period`, depending\n        on the selected :keyword:`format`. :keyword:`format` must be a string\n        containing one or several directives.  The method recognizes the same\n        directives as the :func:`time.strftime` function of the standard Python\n        distribution, as well as the specific additional directives ``%f``,\n        ``%F``, ``%q``. (formatting & docs originally from scikits.timeries)\n\n        +-----------+--------------------------------+-------+\n        | Directive | Meaning                        | Notes |\n        +===========+================================+=======+\n        | ``%a``    | Locale's abbreviated weekday   |       |\n        |           | name.                          |       |\n        +-----------+--------------------------------+-------+\n        | ``%A``    | Locale's full weekday name.    |       |\n        +-----------+--------------------------------+-------+\n        | ``%b``    | Locale's abbreviated month     |       |\n        |           | name.                          |       |\n        +-----------+--------------------------------+-------+\n        | ``%B``    | Locale's full month name.      |       |\n        +-----------+--------------------------------+-------+\n        | ``%c``    | Locale's appropriate date and  |       |\n        |           | time representation.           |       |\n        +-----------+--------------------------------+-------+\n        | ``%d``    | Day of the month as a decimal  |       |\n        |           | number [01,31].                |       |\n        +-----------+--------------------------------+-------+\n        | ``%f``    | 'Fiscal' year without a        | \\(1)  |\n        |           | century  as a decimal number   |       |\n        |           | [00,99]                        |       |\n        +-----------+--------------------------------+-------+\n        | ``%F``    | 'Fiscal' year with a century   | \\(2)  |\n        |           | as a decimal number            |       |\n        +-----------+--------------------------------+-------+\n        | ``%H``    | Hour (24-hour clock) as a      |       |\n        |           | decimal number [00,23].        |       |\n        +-----------+--------------------------------+-------+\n        | ``%I``    | Hour (12-hour clock) as a      |       |\n        |           | decimal number [01,12].        |       |\n        +-----------+--------------------------------+-------+\n        | ``%j``    | Day of the year as a decimal   |       |\n        |           | number [001,366].              |       |\n        +-----------+--------------------------------+-------+\n        | ``%m``    | Month as a decimal number      |       |\n        |           | [01,12].                       |       |\n        +-----------+--------------------------------+-------+\n        | ``%M``    | Minute as a decimal number     |       |\n        |           | [00,59].                       |       |\n        +-----------+--------------------------------+-------+\n        | ``%p``    | Locale's equivalent of either  | \\(3)  |\n        |           | AM or PM.                      |       |\n        +-----------+--------------------------------+-------+\n        | ``%q``    | Quarter as a decimal number    |       |\n        |           | [01,04]                        |       |\n        +-----------+--------------------------------+-------+\n        | ``%S``    | Second as a decimal number     | \\(4)  |\n        |           | [00,61].                       |       |\n        +-----------+--------------------------------+-------+\n        | ``%U``    | Week number of the year        | \\(5)  |\n        |           | (Sunday as the first day of    |       |\n        |           | the week) as a decimal number  |       |\n        |           | [00,53].  All days in a new    |       |\n        |           | year preceding the first       |       |\n        |           | Sunday are considered to be in |       |\n        |           | week 0.                        |       |\n        +-----------+--------------------------------+-------+\n        | ``%w``    | Weekday as a decimal number    |       |\n        |           | [0(Sunday),6].                 |       |\n        +-----------+--------------------------------+-------+\n        | ``%W``    | Week number of the year        | \\(5)  |\n        |           | (Monday as the first day of    |       |\n        |           | the week) as a decimal number  |       |\n        |           | [00,53].  All days in a new    |       |\n        |           | year preceding the first       |       |\n        |           | Monday are considered to be in |       |\n        |           | week 0.                        |       |\n        +-----------+--------------------------------+-------+\n        | ``%x``    | Locale's appropriate date      |       |\n        |           | representation.                |       |\n        +-----------+--------------------------------+-------+\n        | ``%X``    | Locale's appropriate time      |       |\n        |           | representation.                |       |\n        +-----------+--------------------------------+-------+\n        | ``%y``    | Year without century as a      |       |\n        |           | decimal number [00,99].        |       |\n        +-----------+--------------------------------+-------+\n        | ``%Y``    | Year with century as a decimal |       |\n        |           | number.                        |       |\n        +-----------+--------------------------------+-------+\n        | ``%Z``    | Time zone name (no characters  |       |\n        |           | if no time zone exists).       |       |\n        +-----------+--------------------------------+-------+\n        | ``%%``    | A literal ``'%'`` character.   |       |\n        +-----------+--------------------------------+-------+\n\n        .. note::\n\n            (1)\n                The ``%f`` directive is the same as ``%y`` if the frequency is\n                not quarterly.\n                Otherwise, it corresponds to the 'fiscal' year, as defined by\n                the :attr:`qyear` attribute.\n\n            (2)\n                The ``%F`` directive is the same as ``%Y`` if the frequency is\n                not quarterly.\n                Otherwise, it corresponds to the 'fiscal' year, as defined by\n                the :attr:`qyear` attribute.\n\n            (3)\n                The ``%p`` directive only affects the output hour field\n                if the ``%I`` directive is used to parse the hour.\n\n            (4)\n                The range really is ``0`` to ``61``; this accounts for leap\n                seconds and the (very rare) double leap seconds.\n\n            (5)\n                The ``%U`` and ``%W`` directives are only used in calculations\n                when the day of the week and the year are specified.\n\n        .. rubric::  Examples\n\n            >>> a = Period(freq='Q@JUL', year=2006, quarter=1)\n            >>> a.strftime('%F-Q%q')\n            '2006-Q1'\n            >>> # Output the last month in the quarter of this date\n            >>> a.strftime('%b-%Y')\n            'Oct-2005'\n            >>>\n            >>> a = Period(freq='D', year=2001, month=1, day=1)\n            >>> a.strftime('%d-%b-%Y')\n            '01-Jan-2006'\n            >>> a.strftime('%b. %d, %Y was a %A')\n            'Jan. 01, 2001 was a Monday'\n        ",
}

