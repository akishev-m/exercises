#!/usr/bin/evo python

def diff_keys(old, new_d):
    res = {'kept':'', 'added': '', 'removed': ''}
    res['kept'] = set(old.keys() & new_d.keys())
    res['added'] = set(new_d.keys() - old.keys())
    res['removed'] = set(old.keys() - new_d.keys())
    print(res)

def main():
    old1 = {'name': 'Bob', 'age': 42}
    new1 = {}
    old2 = {}
    new2 = {'name': 'Bob', 'age': 42}
    old3 = {'a': 2}
    new3 = {'a': 1}

    diff_keys(old1, new1)
    diff_keys(old2, new2)
    diff_keys(old3, new3)


if __name__ == '__main__':
    main()
