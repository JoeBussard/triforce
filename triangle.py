#!/bin/python
import sys # for command line arguments
TRIANGLE_CHAR = "▲"

def print_triangle(height, size):
    for level in range(height):                        # height of the n-force
        for x in range(size):                          # scale of each triangle
            print(" " * (size * (height - level - 1)), # left margin for this entire level
                    (" " * (size - x - 1) +            # left margin before the first ▲
                    TRIANGLE_CHAR * (2*x + 1) +        # the ▲'s
                    " " * (size - x)) * (level+1),     # right margin after the last ▲
                                                       # repeat for all triangles on this level
                    sep='')                            # all spacing is handled manually
try:
    print(f"printing a {int(sys.argv[1])}-force of scale {int(sys.argv[2])}")
    print_triangle(int(sys.argv[1]), int(sys.argv[2])) # validate input, assume negative triforces are empty
except:
    print("usage: triangle.py <level> <scale>")        # only way to mess up is bad usage
