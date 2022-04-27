#!/usr/bin/env python

from collections.abc import Iterable


def odds(lst):
    if isinstance(lst, Iterable):
        result = lst[::2].copy()
    else:
        result = lst
    return result


def odds_from_odds(l):
    result = list(map(odds, odds(l.copy())))
    return result


def keep_odds_from_odds(l):
    if isinstance(l, Iterable):
        i = 0
        j = 0
        while i < len(l):
            if j % 2 != 0:
                del l[i]
            else:
                i += 1
            j += 1
    for el in l:
       if isinstance(el, Iterable):
           i = 0
           j = 0
           while i < len(el):
               if j % 2 != 0:
                   del el[i]
               else:
                   i +=1
               j += 1
    return l


def main():
    p = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = [1, 3, 5, 6, 7]
    m = []
    l = m 
    print(odds_from_odds(l))
    print(l)
    print(keep_odds_from_odds(l))
    print(l)


if __name__ == '__main__':
    main()

