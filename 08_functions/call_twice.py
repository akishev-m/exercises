#!/usr/bin/env python

import prompt

def call_twice(function, *args, **kwargs):
    a = function(*args, **kwargs)
    b = function(*args, **kwargs)
    return a, b


def main():
    print(call_twice(input, 'Enter value: '))


if __name__ == '__main__':
    main()
