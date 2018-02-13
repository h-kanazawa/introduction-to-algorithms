# -*- coding: utf-8 -*-

from src.minimum import *


def test_min_and_max():
    A = [10]
    E = (10, 10)
    assert min_and_max(A) == E

    A = [10, 0]
    E = (0, 10)
    assert min_and_max(A) == E

    A = [0, 10]
    E = (0, 10)
    assert min_and_max(A) == E

    for i in range(1, 30, 3):
        A = [random.randrange(-100, 100) for x in range(i)]
        assert min_and_max(A) == (min(A), max(A))
