# -*- coding: utf-8 -*-

from src.random_permute import permute_by_sorting, sorted_by_rank


def test_permute_by_sorting():
    A = [0, 1, 2, 3, 4]
    t = 10000
    Acc = [0, 0, 0, 0, 0]
    for i in range(0, t):
        B = permute_by_sorting(A)
        Acc = [k[0] + k[1] for k in zip(Acc, B)]

    Avgs = [a / t for a in Acc]
    # This test is not strict.
    # It will fail probablistically, but failure is very rare.
    # You can reduce probability of failure by enlarging `t` or `allowable_error`.
    # Large `t` prolong the runtime of this test.
    allowable_error = 0.2
    for a in Avgs:
        assert 2 - allowable_error < a and a < 2 + allowable_error


def test_sorted_by_rank():
    A = [0, 1, 2, 3]
    R = [-15, 20, 3, 5]
    E = [0, 2, 3, 1]
    assert sorted_by_rank(A, R) == E
