#!/usr/bin/python3
for num in range(100):
    if (num / 10 != num % 10) and (num / 10 < num % 10):
        print("{:02d}".format(num), end="")
        if (num != 89):
            print(", ", end="")
print("")
