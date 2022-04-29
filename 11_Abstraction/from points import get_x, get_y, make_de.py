from points import get_x, get_y, make_decart_point

def make_segment(p1, p2):
    return make_decart_point(p1, p2)


def get_mid_point_of_segment(segment):
    begin, end = segment
    x = (get_x(end) - get_x(begin)) / 2
    y = (get_y(end) - get_y(begin)) / 2
    return x, y


def get_begin_point(segment):
    (p1, p2) = segment
    return p1


def get_end_point(segment):
    (p1, p2) = segment
    return p2