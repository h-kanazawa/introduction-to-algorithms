# -*- coding: utf-8 -*-

from src.cut_rod import *


def run(f):
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    ans = [1, 5, 8, 10, 13, 17, 18, 22, 25, 30]
    for i in range(1, 11):
        assert ans[i - 1] == f(p, i)


def test_cut_rod():
    run(cut_rod)
    run(memoized_cut_rod)
    run(bottom_up_cut_rod)
