# -*- coding: utf-8 -*-

from typing import List
from math import floor
from copy import deepcopy


# merge sort
def sort(A: List[float]) -> List[float]:
    return _sort(A, 0, len(A) - 1)


def _sort(A: List[float], p: int, r: int):
    if p < r:
        q = floor((p + r) / 2)
        B = _sort(A, p, q)
        C = _sort(B, q + 1, r)
        return merge(C, p, q, r)
    else:
        return A


# p <= p <= r
# A[p..q] and A[q+1..r] have been sorted
def merge(A: List[float], p: int, q: int, r: int) -> List[float]:
    # The number of elements of A[p..q] and A[q+1..r]
    n1 = q - p + 1
    n2 = r - q
    # Create new arraies L[0..n1] and R[0..n2]
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)
    for i in range(0, n1):
        L[i] = A[p + i]
    for j in range(0, n2):
        R[j] = A[q + j + 1]
    L[n1] = float('inf')
    R[n2] = float('inf')

    # Avoid side effect
    B = deepcopy(A)
    # Pick the smaller value from the head of L and R
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            B[k] = L[i]
            i += 1
        else:
            B[k] = R[j]
            j += 1

    return B


if __name__ == '__main__':
    print(sort([5, 1, 4, 2, 3, 1.4, 7.9, 0, -10, -83, 9, 1, 10, -3.3]))
