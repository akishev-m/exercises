#!/usr/bin/env python


def greet(name, surname):
    return f'Hello, {name} {surname}!'


def partial_apply(function, name):
    def inner(surname):
        return function(name, surname)
    return inner


def flip(func):
    def inner(name, surname):
        return func(surname, name)
    return inner


def main():
    f = partial_apply(greet, 'Dorian')
    print(f('Grey'))

    g = flip(greet)
    print(g('Christian', 'Teodor'))


if __name__ == '__main__':
    main()

