# -*- coding: utf-8 -*-

import random
from typing import List


def permute_by_sorting(A: List[float]):
    n = len(A)
    n3 = n ** 3

    # Create a random rank list whose length is n
    R = [0 for i in range(0, n)]
    for i in range(0, n):
        R[i] = random.randrange(1, n3)

    return sorted_by_rank(A, R)


# Ω(n ln(n))
def sorted_by_rank(L: List[float], R: List[int]) -> List[float]:
    return [b[0] for b in sorted(zip(L, R), key=lambda a: a[1])]


# Θ(n)
def randomize_in_place(A: List[float]):
    n = len(A)
    for i in range(0, n):
        # Change A[i] and A[random int from i to n -1]
        j = random.randrange(i, n)
        t = A[j]
        A[j] = A[i]
        A[i] = t

    return A


# 5.3-2
# This algorithm is not random permutation
def permute_without_identity(A: List[float]):
    n = len(A)
    for i in range(0, n - 1):
        # Change A[i] and A[random int from i to n -1]
        j = random.randrange(i + 1, n)
        t = A[j]
        A[j] = A[i]
        A[i] = t

    return A


# 5.3-3
# This algorithm is not random permutation
def permute_with_all(A: List[float]):
    n = len(A)
    for i in range(0, n):
        # Change A[i] and A[random int from i to n -1]
        j = random.randrange(0, n)
        t = A[j]
        A[j] = A[i]
        A[i] = t

    return A


# 5.3-7
# Be careful RecursionError
def random_smple(m: int, n: int) -> List[int]:
    if m > n or m < 0:
        raise Exception('0 <= m <= n')

    if m == 0:
        return []

    S = random_smple(m - 1, n - 1)
    i = random.randrange(1, n + 1)
    if (i in S):
        S.append(n)
    else:
        S.append(i)
    return S


if __name__ == '__main__':
    # A = [0, 1, 2, 3, 4]
    # B = permute_by_sorting(A)
    # print(B)

    print(random_smple(20, 100))
