# -*- coding: utf-8 -*-

from src.recursive_activity_selector import *


def test_recursive_activity_selector():
    s = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    f = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    n = len(s) - 1
    actual = recursive_activity_selector(s, f, 0, n)
    assert [1, 4, 8, 11] == actual


def test_greedy_activity_selector():
    s = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    f = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    actual = greedy_activity_selector(s, f)
    assert [1, 4, 8, 11] == actual
