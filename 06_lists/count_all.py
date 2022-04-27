#!/usr/bin/env python


def count_all(tup):
    voc = {}
    for elem in tup:
        num = tup.count(elem)
        voc.update({elem: tup.count(elem)})
    return voc


def main():
    new = ('catt')
    print(count_all(new))


if __name__ == '__main__':
    main()
