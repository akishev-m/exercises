#!/usr/bin/env python

def make_decart_point(x, y):
    return {"x": x, "y": y}


def get_x(point):
    return point["x"]


def get_y(point):
    return point["y"]


def get_quadrant(point):
    x = get_x(point)
    y = get_y(point)

    if x > 0 and y > 0:
        return 1
    if x < 0 < y:
        return 2
    if x < 0 and y < 0:
        return 3
    if y < 0 < x:
        return 4

    return None

def make_rectangle(point, width, height):
    return {'point': point, 'width': width, 'height': height}


def get_start_point(rectangle):
    return rectangle['point']


def get_start_width(rectangle):
    return rectangle['width']


def get_start_height(rectangle):
    return rectangle['height']


def contains_origin(rectangle):
    up_left_point = get_start_point(rectangle)
    up_right_point = {
            'x': up_left_point['x'] + get_start_width(rectangle),
            'y': up_left_point['y']
            }
    down_left_point = {
            'x': up_left_point['x'],
            'y':up_left_point['y'] - get_start_height(rectangle)
            }
    down_right_point = {
            'x': up_right_point['x'],
            'y': down_left_point['y']
            }
    if (get_quadrant(up_left_point) == 1
        and get_quadrant(up_right_point) == 2
        and get_quadrant(down_left_point) == 3 
        and get_quadrant(down_right_point) == 4):
        return True
    else:
        return False

def temp(rectangle):
    up_left_point = get_start_point(rectangle)
    up_right_point = {
            'x': up_left_point['x'] + get_start_height(rectangle),
            'y': up_left_point['y']
            }
    return up_right_point
 

def main():
    p = make_decart_point(-4, 3)
    rectangle1 = make_rectangle(p, 5, 4)
    print(contains_origin(rectangle1))
#    print(temp(rectangle1))


if __name__ == '__main__':
    main()
