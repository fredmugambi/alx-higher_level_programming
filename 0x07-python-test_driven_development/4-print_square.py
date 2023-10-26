#!/usr/bin/python3

def print_square(size):

     # Check if size is an integer and non-negative
    if not isinstance(size, int):
        if isinstance(size, float):
            if size < 0:
                raise TypeError("size must be an integer")
        else:
            raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

        # Print the square
    for _ in range(size):
        print("#" * size)
