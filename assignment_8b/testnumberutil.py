"""
>>> from numberutil import aswords
>>> aswords(0)
'zero'
>>> aswords(10)
'ten'
>>> aswords(25)
'twenty five'
>>> aswords(20)
'twenty'
>>> aswords(100)
'one hundred'
>>> aswords(105)
'one hundred and five'
>>> aswords(125)
'one hundred and twenty five'
>>> aswords(130)
'one hundred and thirty'
"""

import doctest as dt
dt.testmod(verbose=True)