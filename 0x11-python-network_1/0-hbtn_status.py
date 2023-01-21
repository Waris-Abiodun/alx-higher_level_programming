#!/usr/bin/python3

"""
fetch https://alx-intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":

    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        feedback = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(feedback)))
        print("\t- content: {}".format(feedback))
        print("\t- utf8 content: {}".format(feedback.decode('utf-8')))
