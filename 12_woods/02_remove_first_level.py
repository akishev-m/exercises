#!/usr/bin/env python

def remove_first_level(tree):
    new_tree = [] 
    for it in tree:
        try:
            for element in it:
                new_tree = new_tree + [element]
        except TypeError:
            next
    return new_tree


def main():
    tree = [1, 2, [3, 5], [[4,3], 2]]
    print(remove_first_level(tree))


if __name__ == '__main__':
    main()
