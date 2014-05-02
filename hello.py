#!/usr/bin/python

import sys

def main():

    print('Hello there', sys.argv[1])

    print(repeat('Yay', False))
    print(repeat('Woo Hoo', True))

def repeat(s, exclain):
    result = s + s + s
    if exclain:
        result = result + '!!!'
    return result

if __name__ == '__main__':
    main()