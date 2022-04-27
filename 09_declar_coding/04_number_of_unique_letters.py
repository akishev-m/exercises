#!/usr/bin/env python

from os import lstat


def number_of_unique_letters(lst):
    d = {el.upper(): index for index, el in enumerate(lst) if el.isalpha()}
    print(len(d))


def main():
    a = ""
    b = "abc"
    c = "A-a-a-a-a-a!"
    d = "\\(O_o)/"
    e = "AaBbCcDd"
    lst = [a, b, c, d, e]
    i = 0
    while i < len(lst):
        print(number_of_unique_letters(lst[i]))
        i += 1

if __name__ == '__main__':
    main()
