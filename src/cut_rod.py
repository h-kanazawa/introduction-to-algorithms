# -*- coding: utf-8 -*-

from typing import List


def cut_rod(p: List[float], n: int):
    """
    O(2^n)
    p is prices. p[i]
    15.1
    """
    if len(p) < n:
        raise Exception('length of "p" must be no less than "n"')
    if n == 0:
        return 0
    q = float('-inf')
    for i in range(0, n):
        q = max(q, p[i] + cut_rod(p, n - i - 1))
    return q


def memoized_cut_rod(p: List[float], n: int):
    """O(n^2)
    """
    r = [float('-inf') for i in range(0, n + 1)]
    return memoized_cut_rod_aux(p, n, r)


def memoized_cut_rod_aux(p: List[float], n: int, r: List[float]):
    if r[n] >= 0:
        return r[n]

    if n == 0:
        q = 0
    else:
        q = float('-inf')
        for i in range(0, n):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n - i - 1, r))
    r[n] = q
    return q


def bottom_up_cut_rod(p: List[float], n: int):
    """O(n^2)
    """
    r = [0 for i in range(0, n + 1)]
    for j in range(1, n + 1):
        q = float('-inf')
        for i in range(0, j):
            q = max(q, p[i] + r[j - i - 1])
        r[j] = q
    return r[n]


def extended_bottom_up_cut_rod(p: List[float], n: int):
    r = [0 for i in range(0, n + 1)]
    s = [0 for i in range(0, n)]
    for j in range(1, n + 1):
        q = float('-inf')
        for i in range(0, j):
            if q < p[i] + r[j - i - 1]:
                q = p[i] + r[j - i - 1]
                s[j - 1] = i + 1
        r[j] = q
    return (r, s)


def print_cut_rod_solution(p, n):
    (r, s) = extended_bottom_up_cut_rod(p, n)
    while n > 0:
        print(s[n - 1])
        n = n - s[n - 1]


if __name__ == '__main__':
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    print(extended_bottom_up_cut_rod(p, 10))
    print_cut_rod_solution(p, 9)
