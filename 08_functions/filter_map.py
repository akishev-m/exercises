#!/usr/bin/env

def make_stars(x):
    if x > 0:
        return True, '*' * x
    return False, ''


def filter_map(function, items):
    result = []
    for item in  items:
        if function(item)[0]:
            result.append(function(item)[1])
    return result



def main():
    items = [1, 0, 5, -5, 2]
    for s in filter_map(make_stars, items):
        print(s)


if __name__ == '__main__':
    main()
