#!/usr/bin/env python

import prompt


def all_unique(iterator):
    num = {}
    for el in iterator:
        num[el] = num.get(el, 0)  + 1
        if num[el] > 1:
            return False
    return True




def main():
    iterator = ('cat')
    print(all_unique(iterator))

if __name__ == '__main__':
    main()
