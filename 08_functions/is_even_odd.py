#!/usr/bin/env python3

def is_odd(n):
    return True if not is_even(n)


def is_even(n):
    return True if n % 2 == 0 else False
    

def main():
    print(is_even(4))


if __name__ == '__main__':
    main()
