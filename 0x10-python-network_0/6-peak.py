#!/usr/bin/python3
"""script for finding peak in list of ints, interview prep
"""

"""
    lets go to the process
        it is not sorted, so sorting would take n(log(n))
            -> not worth sorting
        looping through and keeping track of max (brute force)
            -> O(n)

        possibly looping from each end reducing to 1/2 run time
            -> still O(n)
"""


def find_peak(list_of_integers):
    """BRUTE force implementation for question
    """
    result = None
    for tmp in list_of_integers:
        if result is None or result < tmp:
            result = tmp
    return result