# -*- coding: utf-8 -*-

import random
import time

from typing import List


def quick_sort(A: List[float], p: int, r: int):
    """O(n^2)
    Be careful RecursionError
    """
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


def partition(A: List[float], p: int, r: int):
    """O(n)
    This function is not pure. it has "effect".
    """
    x = A[r - 1]
    i = p - 1
    for j in range(p, r):
        if A[j - 1] <= x:
            i += 1
            # Change A[i] and A[j]
            t = A[i - 1]
            A[i - 1] = A[j - 1]
            A[j - 1] = t

    # Change A[i + 1] and A[r]
    t = A[i]
    A[i] = A[r - 1]
    A[r - 1] = t

    return i + 1


def randomized_quick_sort(A: List[float], p: int, r: int):
    if p < r:
        q = randomized_partition(A, p, r)
        randomized_quick_sort(A, p, q - 1)
        randomized_quick_sort(A, q + 1, r)


def randomized_partition(A: List[float], p: int, r: int):
    k = random.randrange(p, r)
    # Change A[k - 1] and A[r - 1]
    t = A[k - 1]
    A[k - 1] = A[r - 1]
    A[r - 1] = t
    return partition(A, p, r)


def compare(n: int):
    """Compare worst-case runtime with quick_sort and randomized quick_sort.
    """
    A = [x for x in range(0, n)]
    B = [x for x in range(0, n)]
    t0 = time.time()
    quick_sort(A, 1, n)
    t1 = time.time()
    randomized_quick_sort(B, 1, n)
    t2 = time.time()

    ratio = (t1 - t0) / (t2 - t1)
    print('{0}\t{1:.8f}\t{2:.8f}\t{3:.4f}'.format(n, t1 - t0, t2 - t1, ratio))
    # print('---------------------- n: {}'.format(n))
    # print('              quick_sort: {0:.8f}'.format(t1 - t0))
    # print('   randomized_quick_sort: {0:.8f}'.format(t2 - t1))
    # print('ratio(normal/randomized): {0:.4f}'.format(ratio))


def measure():
    """
    result
    n       quick_sort      randomized      quick_sort/randomized
    2       0.00000596      0.00001192      0.5000
    4       0.00000787      0.00001097      0.7174
    8       0.00002003      0.00001788      1.1200
    16      0.00006104      0.00004911      1.2427
    32      0.00024104      0.00009894      2.4361
    64      0.00105405      0.00029588      3.5624
    128     0.00383306      0.00047302      8.1033
    256     0.02108288      0.00108790      19.3794
    512     0.05979800      0.00198293      30.1564
    """
    print('n       quick_sort      randomized      quick_sort/randomized')
    for k in range(1, 10):
        compare(2 ** k)


if __name__ == '__main__':
    measure()
