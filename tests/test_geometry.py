# -*- coding: utf-8 -*-

from src.geometry import *


def test_segments_intersect():
    p1 = np.array([4, 3])
    p2 = np.array([1, 1])
    p3 = np.array([1, 3])
    p4 = np.array([2, 2])
    assert segments_intersect(p1, p2, p3, p4) == False

    p1 = np.array([4, 3])
    p2 = np.array([1, 1])
    p3 = np.array([1, 3])
    p4 = np.array([3, 2])
    assert segments_intersect(p1, p2, p3, p4) == True

    p1 = np.array([4, 3])
    p2 = np.array([1, 1])
    p3 = np.array([1, 3])
    p4 = np.array([4, 2])
    assert segments_intersect(p1, p2, p3, p4) == True
