#! /usr/bin/env python
# This free software incorporates by reference the text of the WTFPL, Version 2

"""
This is where your module level help string goes.

.. module:: `SequentialRange`
   :platform: Unix, Windows
   :synopsis: Put a synopsis of what this module does here.

.. moduleauthor:: Michael Morehouse <michael@yawpitchroll.com>
"""

# IMPORT STANDARD MODULES
# import standard modules here

# IMPORT LOCAL MODULES
from terminallogger import get_terminal_logger

LOGGER = get_terminal_logger(__name__)

class SequentialRange(set):
    '''
    This is my docstring for SequentialRange class.
    '''
    def __init__(self, iterable):
        super(SequentialRange, self).__init__(iterable)
    # end __init__

    def __repr__(self):
        """
        If the record does is not logging.INFO, return True
        """
        return ", ".join([str(i) for i in sorted(self)])
    # end some_method
# end SequentialRange

def getSequentialRange(iterable):
    """
    Help string that describes getSequentialRange

    :arg somearg: describe what somearg is
    :type somearg: type of somearg
    :returns: what this function returns
    :rtype: type of the returned object
    """
    return SequentialRange(iterable)
# end getSequentialRange

def main():
    """
    Simply run help if called directly.
    """
    print getSequentialRange(range(1,24,3))
#     import __main__
#     help(__main__)
# end main

__all__ = ['SequentialRange', 'getSequentialRange']

if __name__ == '__main__':
    main()