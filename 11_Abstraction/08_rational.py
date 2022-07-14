#!/usr/bin/env python

import math


# BEGIN (write your solution here)
def make(numer, denom):
    gcd = math.gcd(int(numer), int(denom))
    rational = {
        'numer': numer / gcd,
        'denom': denom / gcd
        }
    return rational

def get_numer(rational):
    numer = rational['numer']
    return numer

def get_denom(rational):
    denom = rational['denom']
    return denom

def add(rat1, rat2):
    numer = rat1['numer'] * rat2['denom'] + rat2['numer'] * rat1['denom']
    denom = rat1['denom'] * rat2['denom']
    return make(numer, denom)


def sub(rat1, rat2):
    numer = rat1['numer'] * rat2['denom'] - rat2['numer'] * rat1['denom']
    denom = rat1['denom'] * rat2['denom']
    return make(numer, denom)

# END


def to_str(rat):
    return f"{get_numer(rat)}/{get_denom(rat)}"


def main():
    rat1 = make(3, 9)
    print(get_numer(rat1))
    print(get_denom(rat1))
    rat2 = make(10, 3)
    rat3 = add(rat1, rat2)
    print(rat3)
    rat4 = sub(rat1, rat2)
    print(rat4)
    print(to_str(rat4))


if __name__ == '__main__':
    main()
