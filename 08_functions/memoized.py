#!/usr/bin/env python

def memoized(func):
    res = {}

    def inner(args):
        if args not in res:
            res.update({args: func(args)})
        return res[args]

    return inner

@memoized
def f(x):
    print('Calculating...')
    return x * 10


def main():
    print(f(1))
    print(f(1))
    print(f(42))
    print(f(42))
    print(f(1))


if __name__ == '__main__':
    main()
