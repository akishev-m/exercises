#!/usr/bin/env python

import prompt

def collect_indexes(col):
    d = {}
    for (index, el) in enumerate(col):
        d.setdefault(el, []).append(index)
    return d


def main():
    col = prompt.string('Enter collection: ')
    d = collect_indexes(col)
    for el in d:
        print(d[el])


if __name__ == '__main__':
    main()
