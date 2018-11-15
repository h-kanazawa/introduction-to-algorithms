# -*- coding: utf-8 -*-

from src.modular_exponentiation import *


def test_to_binarh():
    assert to_binary(560) == [1, 0, 0, 0, 1, 1, 0, 0, 0, 0]


def test_modular_exponentiation():
    assert modular_exponentiation(23, 1, 1) == 0
    assert modular_exponentiation(23, 1, 2) == 1
    assert modular_exponentiation(23, 1, 3) == 2
    assert modular_exponentiation(23, 1, 4) == 3

    assert modular_exponentiation(7, 560, 561) == 1

    assert modular_exponentiation(11, 5, 19) == 11 ** 5 % 19
    assert modular_exponentiation(13, 8, 143) == 13 ** 8 % 143
