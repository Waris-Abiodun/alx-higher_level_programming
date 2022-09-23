#!/usr/bin/python3
import sys
z = sys.argv
i = 0
while (i < len(z)):
    if i == 0:
        if len(z) == 1:
            print(len(z) - 1, "arguments.")
        elif len(z) == 2:
            print(len(z) - 1, "argument:")
        else:
            print(len(z) - 1, "arguments:")

    else:
        print(i, z[i])
    i += 1
