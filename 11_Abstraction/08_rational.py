#!/usr/bin/env python

import math


# BEGIN (write your solution here)
def make(numer, denom):
    gcd = int(math.gcd(numer, denom))
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
    begin_point = make_decart_point(4, 2)
    end_point = make_decart_point(0, 0)
    segment = make_segment(begin_point, end_point)
    print(segment)
    print(get_mid_point_of_segment(segment))


if __name__ == '__main__':
    main()
