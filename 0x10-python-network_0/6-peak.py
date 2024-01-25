#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    if list_of_integers is None or list_of_integers == []:
        return None

    lo = 0
    hi = len(list_of_integers) - 1

    while lo < hi:
        mid = ((hi - lo) // 2) + lo
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            lo = mid + 1
        else:
            hi = mid

    peak = lo  # Corrected to store the potential peak index

    # Check if the potential peak is actually a peak
    if (peak == 0 or list_of_integers[peak] >= list_of_integers[peak - 1]) and \
       (peak == len(list_of_integers) - 1 or list_of_integers[peak] >= list_of_integers[peak + 1]):
        return list_of_integers[peak]
    else:
        return None
