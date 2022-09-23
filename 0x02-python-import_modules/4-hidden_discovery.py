#!/usr/bin/python3
import hidden_4 as hid


def discover():
    name = dir(hid)
    for i in name:
        if i[:2] != '__':
            print("{:s}".format(i))


if __name__ == "__main__":

    discover()
