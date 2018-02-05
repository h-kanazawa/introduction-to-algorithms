# -*- coding: utf-8 -*-

from src.merge_sort import sort, merge


def test_merge():
    A = [99, 99, 99, 1, 4, 6, 7, 18, 3, 5, 7, 10, 88, 88]
    e = [99, 99, 99, 1, 3, 4, 5, 6, 7, 7, 10, 18, 88, 88]
    assert merge(A, 3, 7, 11) == e


def test_sort():
    i = [5, 3, 2, 7, 10, 9, 3]
    e = [2, 3, 3, 5, 7, 9, 10]
    assert sort(i) == e
