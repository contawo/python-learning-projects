"""
>>> from timeutil import validate
>>> validate("12")
False
>>> validate("hh:00")
False
>>> validate("111:00")
False
>>> validate("11:00 pm")
False
>>> validate("11:m p.m.")
False
>>> validate("9:23 p.m.")
True

"""

import doctest as dt
dt.testmod(verbose=True)