#!/usr/bin/env python

def triangle(num):
    string = [1]
    index = 1
    while index <= num:
        new_str = [1]
        new_str.extend(string)
        index2 = 1
        while index2 < len(string):
            new_str[index2] = string[index2 - 1] + string[index2]
            index2 += 1
        string = new_str
        index += 1
    print(string)


def main():
    triangle(4)

if __name__ == '__main__':
    main()
