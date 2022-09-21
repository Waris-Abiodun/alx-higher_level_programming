#!/usr/bin/python3
def remove_char_at(str, n):
    newStr = ""
    i = 0
    for char in str:
        if (i != n):
            newStr += char
        i += 1
    return newStr
