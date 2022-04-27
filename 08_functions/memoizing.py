#!/usr/bin/env python

from functools import wraps

def memoizing(num):
#    @wraps(num)
    def wrapper(func):
        res = {}

        @wraps(func)
        def inner(args):
            if args not in res:
                res.update({args: func(args)})
            if len(res) > num:
                print(res)
                for key in res:
                    res.pop(key)
                    break
            print(res)
            return res[args]

        return inner
    return wrapper


@memoizing(3)
def f(x):
    print('Calculating...')
    return x * 10


def main():
    print(f(1))
    print(f(1))
    print(f(2))
    print(f(3))
    print(f(4))
    print(f(1))


if __name__ == '__main__':
    main()
