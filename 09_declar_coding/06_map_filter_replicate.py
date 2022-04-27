#!/usr/bin/env python

def my_map(f, xs):
    for i in xs:
        i = f(i)
        yield i


def my_filter(f, xs):
    for i in xs:
        if f(i):
            yield i


def replicate_each(n, xs):   
    for i in xs:
        num = 0
        while num < n:
            num += 1
            yield i



def main():
    xs = [-1, 2, -3]
    print(list(my_map(abs, xs)))
    print(list(my_filter(lambda x: x % 2 == 1, range(10))))
    print(list(replicate_each(3, [1, 'a'])))


if __name__ == '__main__':
    main()
