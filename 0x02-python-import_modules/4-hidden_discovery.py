#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import hidden_4

    for name in dir(hidden_4):
        if name[0] != '_':
            print("{:s}".format(name))
