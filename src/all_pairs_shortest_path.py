# -*- coding: utf-8 -*-

import numpy as np


INF = float('inf')


def build_shortest_path(Π, i, j):
    """Build shortest path from a predecessor matrix

    Arguments:
        Π {np.ndarray -- predecessor matrix}
        i {int} -- start
        j {int} -- goal
    """
    def f(Π, i, j, p):
        if i == j:
            p.append(i)
        elif Π[i][j] is None:
            return None
        else:
            f(Π, i, Π[i][j], p)
            p.append(j)
        return p

    return f(Π, i, j, [])


def extend_shortest_paths(L, W):
    """Θ(n^3)"""
    n = L.shape[0]
    Ld = np.zeros((n, n))
    for i in range(0, n):
        for j in range(0, n):
            Ld[i][j] = INF
            for k in range(0, n):
                Ld[i][j] = min(Ld[i][j], L[i][k] + W[k][j])
    return Ld


def slow_all_pairs_shortest_paths(W):
    """Θ(n^4)"""
    n = W.shape[0]
    L = [W]
    for m in range(1, n):
        Lm = extend_shortest_paths(L[m - 1], W)
        L.append(Lm)
    return L[n - 1]


def faster_all_pairs_shortest_paths(W):
    n = W.shape[0]
    L = [W]
    # m = 2 ^ k (k=0,1,2,3,...)
    k = 0
    m = 1
    while m < n - 1:
        L2m = extend_shortest_paths(L[k], L[k])
        L.append(L2m)
        k += 1
        m *= 2
    return L[k]


if __name__ == '__main__':
    print('x')
