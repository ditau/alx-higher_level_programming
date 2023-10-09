#!/usr/bin/python3
# 5-no_c.py


def no_c(my_string):
    """Remove all characters c and C from a string."""
    copy = [a for a in my_string if a != 'c' and a != 'C']
    return ("".join(copy))
