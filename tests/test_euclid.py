# -*- coding: utf-8 -*-

from src.euclid import *

def test_recursive_euclid():
    assert recursive_euclid(30, 21) == 3
    assert recursive_euclid(16, 21) == 1
    assert recursive_euclid(128, 72) == 8


def test_euclid():
    assert euclid(30, 21) == 3
    assert euclid(16, 21) == 1
    assert euclid(128, 72) == 8


def test_recursive_extended_euclid():
    """page 778"""
    assert recursive_extended_euclid(99, 78) == (3, -11, 14)
    assert recursive_extended_euclid(78, 21) == (3, 3, -11)
    assert recursive_extended_euclid(21, 15) == (3, -2, 3)
    assert recursive_extended_euclid(15, 6) == (3, 1, -2)
    assert recursive_extended_euclid(6, 3) == (3, 0, 1)
    assert recursive_extended_euclid(3, 0) == (3, 1, 0)
