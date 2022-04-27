#!/usr/bin/env python


def apply_diff(tar, diff):
    add = diff.get('add', {})
    remove = diff.get('remove', {})
    tar.update(add)
    tar.difference_update(remove)

def main():
    target = {'a', 'b'}
    diff = {'add': '', 'remove': ''}
    apply_diff(target, diff)
    print(target)


if __name__ == '__main__':
    main()
