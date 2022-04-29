#!/usr/bin/env python

col = [1, 2, 3, 4, 5]


def fill(coll, value, begin=0, end=''):
    if not end or end > len(coll):
        end = len(coll)
    for index, item in enumerate(coll):
        if index >= begin and index < end:
            coll[index] = value
    return coll


def main():
    fill(col, '*', 1, 19)


if __name__ == '__main__':
    main()
