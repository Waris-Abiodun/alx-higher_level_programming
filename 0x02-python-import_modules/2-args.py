#!/usr/bin/python3
import sys
z = sys.argv
i = 0
while (i < len(z)):
    if i == 0:
        if len(z) == 1:
            print("{} argument.".format(len(z) - 1))

        elif len(z) == 2:
            print("{} argument:".format(len(z) - 1))
        else:
            print("{} arguments:" .format(len(z) - 1))
    else:
        print("{}: {}".format(i, z[i]))
    i += 1
