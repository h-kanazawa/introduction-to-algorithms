# -*- coding: utf-8 -*-

import time

import numpy as np
from numpy.random import randint


# Θ(n^3)
def product(A, B):
    n = A.shape[0]
    C = np.zeros((n, n))
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                C[i, j] = C[i, j] + A[i, k] * B[k, j]
    return C


# 4.2-2
# The case when n = 2^m (m ∈ natural numbers)
# T(n) = Θ(n^log(2)7) ~= Θ(n^2.807...)
def strassen(A, B):
    n = A.shape[0]

    # Check n is a 2^m (m ∈ natural numbers)
    if n & (n - 1):
        print('Not support n != 2^m (m ∈ natural numbers)')
        return

    if n == 1:
        return np.matrix(A[0, 0] * B[0, 0])

    # Θ(1)
    mid = int(n / 2)
    A11 = A[0: mid, 0: mid]
    A12 = A[0: mid, mid: n]
    A21 = A[mid: n, 0: mid]
    A22 = A[mid: n, mid: n]
    B11 = B[0: mid, 0: mid]
    B12 = B[0: mid, mid: n]
    B21 = B[mid: n, 0: mid]
    B22 = B[mid: n, mid: n]

    # Θ(n^2)
    S1 = B12 - B22
    S2 = A11 + A12
    S3 = A21 + A22
    S4 = B21 - B11
    S5 = A11 + A22
    S6 = B11 + B22
    S7 = A12 - A22
    S8 = B21 + B22
    S9 = A11 - A21
    S10 = B11 + B12

    # 7T(n/2)
    P1 = strassen(A11, S1)
    P2 = strassen(S2, B22)
    P3 = strassen(S3, B11)
    P4 = strassen(A22, S4)
    P5 = strassen(S5, S6)
    P6 = strassen(S7, S8)
    P7 = strassen(S9, S10)

    # Θ(n^2)
    C11 = P5 + P4 - P2 + P6
    C12 = P1 + P2
    C21 = P3 + P4
    C22 = P5 + P1 - P3 - P7

    C1 = np.concatenate((C11, C12), axis=1)
    C2 = np.concatenate((C21, C22), axis=1)
    C = np.concatenate((C1, C2), axis=0)

    return C


def genSquareMatrix(n):
    M = np.zeros((n, n))
    for i in range(0, n):
        for j in range(0, n):
            M[i, j] = randint(-10, 10)
    return M


def compare(n):
    A = genSquareMatrix(n)
    B = genSquareMatrix(n)

    t0 = time.time()
    p0 = product(A, B)
    t1 = time.time()
    p1 = np.dot(A, B)
    t2 = time.time()

    if p0.all() != p1.all():
        print('product(A, B) and np.dot(A, B) are not same!')
        print('product(A, B): {}'.format(p0))
        print(' np.dot(A, B): {}'.format(p1))
        return

    ratio = (t1 - t0) / (t2 - t1)
    # print('             product(A, B): {0:.8f}'.format(t1 - t0))
    # print('              np.dot(A, B): {0:.8f}'.format(t2 - t1))
    # print('product(A, B)/np.dot(A, B): {0:.4f}'.format(ratio))
    return ratio


if __name__ == '__main__':
    tries = 10
    r = [compare(20) for i in range(tries)]
    print('mean: {0:.2f}, max: {1:.2f}, min: {2:.2f}'.format(sum(r) / tries, max(r), min(r)))
