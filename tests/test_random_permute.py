# -*- coding: utf-8 -*-

from src.random_permute import (
    permute_by_sorting,
    sorted_by_rank,
    randomize_in_place,
    permute_without_identity,
    permute_with_all
)


N = 10000
T = 5
E = 0.2


def run_test(f, t=100, n=5, allowable_error=0.1):
    """This test is not strict.
    It will fail probablistically, but failure is very rare.
    You can reduce probability of failure by enlarging `t` or `allowable_error`.
    Large `t` prolong the runtime of this test.
    """

    A = [x for x in range(0, n)]
    Acc = [0 for x in range(0, n)]
    for i in range(0, t):
        B = f(A)
        Acc = [k[0] + k[1] for k in zip(Acc, B)]

    Avgs = [a / t for a in Acc]

    for a in Avgs:
        assert 2 - allowable_error < a and a < 2 + allowable_error


def test_permute_by_sorting():
    run_test(permute_by_sorting, N, T, E)


def test_randomize_in_place():
    run_test(randomize_in_place, N, T, E)


def test_permute_without_identity():
    run_test(permute_without_identity, N, T, E)


def test_permute_with_all():
    run_test(permute_with_all, N, T, E)


def test_sorted_by_rank():
    A = [0, 1, 2, 3]
    R = [-15, 20, 3, 5]
    E = [0, 2, 3, 1]
    assert sorted_by_rank(A, R) == E
