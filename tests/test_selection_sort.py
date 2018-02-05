# -*- coding: utf-8 -*-

from src.selection_sort import sort


def test_sort():
    i = [5, 3, 2, 7, 10, 9, 3]
    e = [2, 3, 3, 5, 7, 9, 10]
    assert sort(i) == e
