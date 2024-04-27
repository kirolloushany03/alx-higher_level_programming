#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""


def find_peak(lst):
    """Function that finds a peak in a list of unsorted integers"""
    length = len(lst)
    if length == 0:
        return None

    def peak(length, m):
        """ " Helper function to find the peak"""
        if (m == 0 or lst[m] >= lst[m - 1]) and (
            m == length - 1 or lst[m] >= lst[m + 1]
        ):
            return lst[m]
        if m > 0 and lst[m - 1] > lst[m]:
            return peak(m, m // 2)
        return peak(length, m + (length - m) // 2)

    return peak(length, length // 2)
