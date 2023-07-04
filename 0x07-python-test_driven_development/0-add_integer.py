#!/usr/bin/python3
"""

This function adds up 2 integers

"""


def add_integer(a, b=98):
    """This Returns sum of two integers or floats as integers

    Args:
        a: The first argument.
        b: The second argument.

    Returns:
       Total Sum of the two arguments

    Raises:
        TypeError: If any of the arguments not an integer or a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
