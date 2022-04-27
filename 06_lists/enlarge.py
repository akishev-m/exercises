#!/usr/bin/env python


def show(image):
    for line in image:
        print(line)

def enlarge(string):
    new_string = []
    for (index, elem) in enumerate(string):
        line = string[index]
        new_line = ''
        for sym in line:
            new_line = new_line + sym + sym
        string[index] = new_line
        new_string.append(string[index])
        new_string.append(string[index])
    return new_string


def main():
    dot = ['****',
           '*  *',
           '*  *',
           '****'
           ]
    show(dot)
    show(enlarge(dot))

if __name__ == '__main__':
    main()
