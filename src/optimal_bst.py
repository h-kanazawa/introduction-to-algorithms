# -*- coding: utf-8 -*-

from typing import List


def optimal_bst(p: List[float], q: List[float], n: int):
    """
    15.5
    Optimal Binary Search Tree

    len(p) should be len(q)
    sum(p) + sum(q) should be 1

    returns 3 two-dimensional lists, `e`, `w`, and `root`
    e[1 ... n + 1, 0 ... n]
    w[1 ... n + 1, 0 ... n]
    root[1 ... n, 1 ... n]
    """
    e = [[0 for i in range(n + 1)] for j in range(n + 1)]
    w = [[0 for i in range(n + 1)] for j in range(n + 1)]
    root = [[0 for i in range(n)] for j in range(n)]

    for i in range(n + 1):
        e[i][i] = q[i]
        w[i][i] = q[i]

    for l in range(n):
        for i in range(n - l):
            j = i + l + 1
            e[i][j] = float('inf')
            w[i][j] = w[i][j - 1] + p[j - 1] + q[j]
            for r in range(i, j):
                t = e[i][r] + e[r + 1][j] + w[i][j]
                if t < e[i][j]:
                    e[i][j] = t
                    root[i][j - 1] = r + 1

    return (e, w, root)


def print_2d_list(l: List[float], f):
    sl = [', '.join([f(x) for x in row]) for row in l]
    print('\n'.join(sl) + '\n')


def print_float_2d_list(l: List[float]):
    def f(x):
        return '{:.2f}'.format(x)
    print_2d_list(l, f)


def print_int_2d_list(l: List[float]):
    def f(x):
        return '{0:4d}'.format(x)
    print_2d_list(l, f)


if __name__ == '__main__':
    p = [0.15, 0.10, 0.05, 0.10, 0.20]
    q = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]
    n = len(p)
    e, w, root = optimal_bst(p, q, n)
    print_float_2d_list(e)
    print_float_2d_list(w)
    print_int_2d_list(root)
