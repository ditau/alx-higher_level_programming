#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    if list_of_integers is None or list_of_integers == []:
        return None

    lo = 0
    hi = len(list_of_integers) - 1  # Adjusted to correct the index range

    while lo < hi:
        mid = (lo + hi) // 2  # Corrected calculation of mid index
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            lo = mid + 1
        else:
            hi = mid

    return list_of_integers[lo]
