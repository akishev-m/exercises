#!/usr/bin/env python

def make_decart_point(x, y):
    return {"x": x, "y": y}


def get_x(point):
    return point["x"]


def get_y(point):
    return point["y"]


def make_segment(p1, p2):
    return make_decart_point(p1, p2)


def get_mid_point_of_segment(segment):
    begin = get_begin_point(segment)
    end = get_end_point(segment)
    x = (end['x'] - begin['x']) / 2
    y = (end['y'] - begin['y']) / 2
    return make_decart_point(x, y) 


def get_begin_point(segment):
    return segment['x']


def get_end_point(segment):
    return segment['y']

def main():
    begin_point = make_decart_point(4, 2)
    end_point = make_decart_point(0, 0)
    segment = make_segment(begin_point, end_point)
    print(segment)
    print(get_mid_point_of_segment(segment))


if __name__ == '__main__':
    main()
