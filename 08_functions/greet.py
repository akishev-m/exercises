#!/usr/bin/env python


def greet(name, *args):
    names = (name,) + args
    n = ' and '.join(names)
    n = 'Hello, ' + n + '!'
    return n


def main():
     print(greet('Bob'))
     print(greet('Moe', 'Mary'))
     print(greet(*'ABC'))


if __name__ == '__main__':
    main()
