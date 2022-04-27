#!/usr/bin/env python

def is_int(x):
    return isinstance(x, int)

def each2d(func, lst):
    xs = (
            func(item) for sublist in 
            lst for item in 
            sublist
            )
    xs_l = []
    for item in xs:
        if item:
            continue
        else:
            return False
    return True

def some2d(func, lst):
    xs = (
            func(item) for sublist in 
            lst for item in 
            sublist
            )
    for item in xs:
        if not item:
            continue
        else:
            return True
    return False


def sum2d(func, lst):
    xs = (
            item for sublist in 
            lst for item in 
            sublist if is_int(item)
            )
    return sum(list(xs))


def main():
#    print(each2d(is_int, [[1, 2], [3, 4]]))
#    print(each2d(is_int, [[1, None], [3, 4]]))
#    print(each2d(is_int, []))
    print(some2d(is_int, [[None, "foo"], [(), {}]]))
    print(some2d(is_int, [[None, "foo"], [0, {}]]))
    print(some2d(is_int, []))
#    print(sum2d(is_int, [[1, "Foo", 100], [False, 10, None]]))

    
if __name__ == '__main__':
    main()
