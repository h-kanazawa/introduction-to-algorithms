# -*- coding: utf-8 -*-

from typing import List


def matrix_chain_order(p: List[int]):
    n = len(p) - 1
    m = [[0 for j in range(n)] for i in range(n)]
    s = [[0 for j in range(n - 1)] for i in range(n - 1)]
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i - 1][j - 1] = float('inf')
            for k in range(i, j):
                q = m[i - 1][k - 1] + m[k][j - 1] + p[i - 1] * p[k] * p[j]
                if q < m[i - 1][j - 1]:
                    m[i - 1][j - 1] = q
                    s[i - 1][j - 2] = k
    return (m, s)


def print_optimal_parens(s, i, j):
    """
    e.g.
    (( A1 ( A2  A3 ))(( A4  A5 ) A6 ))
    """
    if i == j:
        print(' A{} '.format(i), end='')
    else:
        print('(', end='')
        print(print_optimal_parens(s, i, s[i - 1][j - 2]), end='')
        print(print_optimal_parens(s, s[i - 1][j - 2] + 1, j), end='')
        print(')', end='')
    return ''


if __name__ == '__main__':
    """
    Pi-1 x Pi matrix Ai
    A1  * A2  * A3  * ... An
    P0xP1 P1xP2 P2xP3 ... Pn-1xPn
    p = [P0, P1, ..., Pn]
    """
    def g(x):
        return '{0:6d}'.format(x)

    p = [30, 35, 15, 5, 10, 20, 25]
    # p = [5, 10, 3, 12, 5, 50, 6]
    (m, s) = matrix_chain_order(p)

    print('m')
    print('\n'.join(map(lambda a: ' '.join(map(g, a)), m)))
    print('s')
    print('\n'.join(map(lambda a: ' '.join(map(g, a)), s)))

    print_optimal_parens(s, 1, 6)
