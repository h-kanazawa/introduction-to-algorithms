# -*- coding: utf-8 -*-

from src.string_matching import *


def test_exact_match():
    T = ['a', 'b']
    P = ['a', 'b']
    assert exact_match(T, P) == True

    T = ['a', 'c']
    P = ['a', 'b']
    assert exact_match(T, P) == False

    T = ['a', 'b', '']
    P = ['a', 'b']
    try:
        assert exact_match(T, P) == False
        # should not pass here
        assert False
    except Exception:
        assert True


def test_naive_string_matcher():
    T = ['a', 'b']
    P = ['a', 'b']
    assert naive_string_matcher(T, P) == [0]

    T = ['a', 'b', 'c']
    P = ['a', 'b']
    assert naive_string_matcher(T, P) == [0]

    T = ['a', 'a', 'a', 'b']
    P = ['a', 'a']
    assert naive_string_matcher(T, P) == [0, 1]

    # 32.1-1
    T = [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1]
    P = [0, 0, 0, 1]
    assert naive_string_matcher(T, P) == [1, 5, 11]
