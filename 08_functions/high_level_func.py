#!/usr/bin/env python

import functools
import operator

def keep_truthful(args):
    result = []
    for item in args:
        if operator.truth(item):
            result.append(item)
    return result


def abs_sum(args):
    result = 0
    for item in args:
        result = result + abs(int(item))
    return result

def walk(args, index):
    new_dic = args
    for i in index:
        new_dic = operator.getitem(new_dic, i)
    return new_dic


def main():
    a = [True, False, "", "foo"]
    b = [-3, 4, -10]
    c = {'a': {7: {'b': 42}}}
    i = ["a", 7]
    print(list(keep_truthful(a)))
    print(abs_sum(b))
    print(walk(c, i))



if __name__ == '__main__':
    main()
