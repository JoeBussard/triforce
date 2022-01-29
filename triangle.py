#!/bin/python
import sys # for command line arguments
import emoji
TRIANGLE_CHAR = "▲"

def print_triangle(height, size, char = TRIANGLE_CHAR):
    char_size = len(char)
    for x in char:
      if emoji.is_emoji(x):
          char_size += 1
    for level in range(height):                        # height of the n-force
        for x in range(size):                          # scale of each triangle
            print(" " * (size * char_size * (height - level - 1)), # left margin for this entire level
                    (" " * ((size - x -1) * char_size) +            # left margin before the first ▲
                    char * (2*x + 1) +                 # the ▲'s
                    " " * (char_size * (size-x))) * (level + 1),     # right margin after the last ▲
                                                       # repeat for all triangles on this level
                    sep='')                            # all spacing is handled manually
try:
    if len(sys.argv) == 3:
        sys.argv.append(TRIANGLE_CHAR)
    print(f"printing a {int(sys.argv[1])}-force of scale {int(sys.argv[2])} made up of {sys.argv[3]}'s")
    print_triangle(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])
except:
    print("usage: triangle.py <level> <scale> [substance]")        # only way to mess up is bad usage
