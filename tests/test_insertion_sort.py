# -*- coding: utf-8 -*-

from src.insertion_sort import sort, desc_sort


def test_sort():
    i = [5, 3, 2, 7, 10, 9, 3]
    e = [2, 3, 3, 5, 7, 9, 10]
    assert sort(i) == e


def test_desc_sort():
    i = [5, 3, 2, 7, 10, 9, 3]
    e = [10, 9, 7, 5, 3, 3, 2]
    assert desc_sort(i) == e
