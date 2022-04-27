#!/usr/bin/env python

def hamming_weight(num):
    bin_num = bin(num)[2:]
    print(isinstance(bin_num, str))
    print(bin_num.count('1'))


def main():
    hamming_weight(8)

if __name__ == '__main__':
    main()
