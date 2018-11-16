# -*- coding: utf-8 -*-

from src.string_matching import *


def finite_automaton_matcher(T, δ, m):
    """
    Θ(n)
    """
    n = len(T)
    shifts = []
    q = 0
    for i in range(0, n):
        q = δ(q, T[i])
        if q == m:
            shifts.append(i - m + 1)
    return shifts


def compute_transition_function(P, Σ):
    """
    compute δ
    O(m * |Σ|)

    Arguments:
        P {List[a] (a ∈ Σ)} -- pattern
        Σ {Set} -- character set
    """
    def dict_to_func(dic):
        def δ(q, a):
            return dic[q][a]
        return δ

    m = len(P)
    dic = dict()
    for q in range(0, m + 1):
        dic[q] = dict()
        for a in Σ:
            # compute σ(x) = max {k: Pk is suffix of x}
            k = min(m + 1, q + 2)
            while True:
                k -= 1
                Pk = P[0:k]
                Pq = P[0:q] + [a]
                if is_suffix(Pk, Pq):
                    break

            dic[q][a] = k

    δ = dict_to_func(dic)

    return (δ, dic)


def is_suffix(x: List, y: List) -> bool:
    """x ] y"""
    lx = len(x)
    ly = len(y)
    if lx > ly:
        return False
    return exact_match(x, y[ly - lx: ly])


if __name__ == '__main__':
    print('x')
