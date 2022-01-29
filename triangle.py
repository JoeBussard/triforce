#!/bin/python
import sys # for command line arguments
TRIANGLE_CHAR = "▲"

def print_triangle(height, size):
    for level in range(height):
        for x in range(size):
            print(" " * (size * (height - level - 1)),
                    (" " * (size - x) +
                    TRIANGLE_CHAR * (2*x + 1) +
                    " " * (size - x-1)) * (level+1))
try:
    print(f"printing a {int(sys.argv[1])}-force of scale {int(sys.argv[2])}")
    print_triangle(int(sys.argv[1]), int(sys.argv[2]))
except:
    print("usage: triangle.py <level> <scale>")
