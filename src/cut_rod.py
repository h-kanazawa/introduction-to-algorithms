# -*- coding: utf-8 -*-

from typing import List


def cut_rod(p: List[float], n: int):
    """
    p is prices. p[i]
    """
    if len(p) < n:
        raise Exception('length of "p" must be no less than "n"')
    if n == 0:
        return 0
    q = float('-inf')
    for i in range(0, n):
        q = max(q, p[i] + cut_rod(p, n - i - 1))
    return q


if __name__ == '__main__':
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    print(cut_rod(p, 10))
