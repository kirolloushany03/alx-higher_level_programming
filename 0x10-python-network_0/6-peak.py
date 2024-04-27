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
    # Base case: if the list has only one element, it is a peak
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    
    # Find the middle index
    mid = len(list_of_integers) // 2
    
    # Check if the middle element is a peak
    if (mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and \
        (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
        return list_of_integers[mid]
    
    # If the middle element is not a peak, recursively search in the half where the neighbor is greater
    if mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])