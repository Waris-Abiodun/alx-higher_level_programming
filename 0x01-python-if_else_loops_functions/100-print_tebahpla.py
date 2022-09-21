#!/usr/bin/python3
char = 25
while(char >= 0):
    if (char % 2) == 0:
        print("{:s}".format(chr(char + ord("A"))), end="")
    else:
        print("{:s}".format(chr(char + ord("a"))), end="")
    char -= 1
