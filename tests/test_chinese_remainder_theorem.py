# -*- coding: utf-8 -*-

from src.chinese_remainder_theorem import *


def test_chinese_remainder_theorem_pair():
    assert chinese_remainder_theorem_pair(2, 3, 3, 5) == 8
    assert chinese_remainder_theorem_pair(2, 3, 5, 13) == 42

def test_chinese_remainder_theorem():
    n = [3, 5, 7]
    a = [2, 3, 2]
    assert chinese_remainder_theorem(n, a) == 23
