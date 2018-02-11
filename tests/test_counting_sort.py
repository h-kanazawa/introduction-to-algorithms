# -*- coding: utf-8 -*-

from src.counting_sort import *


def test_counting_sort():
    k = 5
    A = [1, 3, 4, 0, 3, 3, 1, 0, 5, 4, 4, 4, 3]
    E = [0, 0, 1, 1, 3, 3, 3, 3, 4, 4, 4, 4, 5]
    assert counting_sort(A, k) == E
