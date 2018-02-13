# -*- coding: utf-8 -*-

import random

from typing import List


def minimum(A: List[float]) -> float:
    if len(A) < 1:
        raise Exception('argument A is empty')
    m = A[0]
    for i in range(1, len(A)):
        if m > A[i]:
            m = A[i]
    return m


def min_and_max(A: List[float]) -> (float, float):
    if len(A) < 1:
        raise Exception('argument A is empty')

    if len(A) % 2 == 0:
        if A[0] > A[1]:
            mi = A[1]
            ma = A[0]
        else:
            mi = A[0]
            ma = A[1]
        ini = 2
    else:
        mi = A[0]
        ma = A[0]
        ini = 1

    for i in range(ini, len(A), 2):
        if A[i] < A[i + 1]:
            if mi > A[i]:
                mi = A[i]
            if ma < A[i + 1]:
                ma = A[i + 1]
        else:
            if mi > A[i + 1]:
                mi = A[i + 1]
            if ma < A[i]:
                ma = A[i]

    return (mi, ma)


if __name__ == '__main__':
    A = [random.randrange(-100, 100) for x in range(9)]
    print((min(A), max(A)))
    print(min_and_max(A))
