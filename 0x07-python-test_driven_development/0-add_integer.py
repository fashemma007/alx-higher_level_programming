#!/usr/bin/python3
"""
Defines an addition function.
`Usage`
``add_integer(...)``` returns the addition of the two arguments. For numbers, that value is equivalent to using the ``+`` operator.
"""


def add_integer(a, b=98):
    """
    Returns the integer addition of a and b.

    `Float` arguments are typecasted to `ints` before addition is performed.

    Raises:
    `TypeError`: If either of a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
