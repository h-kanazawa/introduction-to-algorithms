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


# Θ(n^log(2)7) ~= Θ(n^2.807...)
def strassen(A, B):
    # TODO
    return


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
