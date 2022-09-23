#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    z = sys.argv
    i = 1
    sum = 0
    while (i < len(z)):
        z[i] = int(z[i])
        sum += z[i]
        i += 1
    print(sum)
