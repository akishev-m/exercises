#!/usr/bin/env python


def updated(dic={}, **kwargs):
    res = dic.copy()
    res.update(kwargs)
    return res



def main():
    d = {'a': 1, 'b': False}
    print(updated(d, a=2, b=True, c=None))
    print(d)
    print(updated(d) == d)
    print(updated(d) is d)

if __name__ == '__main__':
    main()
