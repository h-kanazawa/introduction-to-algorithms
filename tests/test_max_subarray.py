# -*- coding: utf-8 -*-

from src.max_subarray import find_max_subarray, find_max_crossing_subarray


def test_find_max_subarray():
    A = [1, -1, 4, -3, 5, 9, -2, 4, -5, 2, -8]
    e = (2, 7, 17)
    assert find_max_subarray(A, 0, len(A) - 1) == e


def test_find_max_subarray_when_all_elements_are_negative():
    A = [-1, -2, -3, -2, -1, -4, -3, -5]
    e = (0, 0, -1)
    assert find_max_subarray(A, 0, len(A) - 1) == e


def test_find_max_subarray_when_answer_is_one_element():
    A = [-1, 2, -3, 1, 0]
    e = (1, 1, 2)
    assert find_max_subarray(A, 0, len(A) - 1) == e


def test_find_max_crossing_subarray():
    A = [4, -1, -3, 4, 5, 9, -2, 4, -5, 2, -8]
    low = 1
    mid = 4
    high = 8
    e = (3, 7, 20)
    assert find_max_crossing_subarray(A, low, mid, high) == e
