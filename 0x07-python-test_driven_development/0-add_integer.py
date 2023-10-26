#!/usr/bin/python3
""" Defines adding of two interger values a and b """
def add_integer(a, b=98):
     # Check if a and b are integers or floats
     if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer or float")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer or float")

     if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

        return(int(a) + int(b))
