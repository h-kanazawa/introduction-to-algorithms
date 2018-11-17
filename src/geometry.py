# -*- coding: utf-8 -*-

import numpy as np


def direction(pi, pj, pk):
    return np.cross(pk - pi, pj - pi)


def on_segment(pi, pj, pk):
    """
    returns whether pk is on "segment" (pi, pj)

    pi, pj, pk is on a line
    """
    xi, yi = pi
    xj, yj = pj
    xk, yk = pk

    return (
        (min(xi, xj) <= xk and xk <= max(xi, xj)) and
        (min(yi, yj) <= yk and yk <= max(yi, yj))
    )


def segments_intersect(p1, p2, p3, p4):
    d1 = direction(p3, p4, p1)
    d2 = direction(p3, p4, p2)
    d3 = direction(p1, p2, p3)
    d4 = direction(p1, p2, p4)

    if (
        ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and
        ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0))
    ):
        return True

    return (
        d1 == 0 and on_segment(p3, p4, p1) or
        d2 == 0 and on_segment(p3, p4, p2) or
        d3 == 0 and on_segment(p1, p2, p3) or
        d4 == 0 and on_segment(p1, p2, p4)
    )


if __name__ == '__main__':
    print('x')
