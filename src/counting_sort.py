# -*- coding: utf-8 -*-

from typing import List


def counting_sort(A: List[float], k: int):
    """Page 160
    """
    C = [0] * (k + 1)

    # Count `i` in A and set it to C[i]
    for j in range(1, len(A) + 1):
        C[A[j - 1]] = C[A[j - 1]] + 1

    # Set C[i] with the number of elements less than i
    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]

    B = [0] * len(A)
    for j in range(len(A), 0, -1):
        B[C[A[j - 1]] - 1] = A[j - 1]
        C[A[j - 1]] = C[A[j - 1]] - 1

    return B


if __name__ == '__main__':
    k = 5
    # A is a list whose all elements are 0 ~ k
    A = [1, 3, 4, 0, 3, 3, 1, 0, 5, 4, 4, 4, 3]
    print(counting_sort(A, k))
