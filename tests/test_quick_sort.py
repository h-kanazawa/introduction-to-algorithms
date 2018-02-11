# -*- coding: utf-8 -*-

from src.quick_sort import *


def test_quick_sort():
    A = [5, 3, 2, 7, 10, 9, 3]
    E = [2, 3, 3, 5, 7, 9, 10]
    quick_sort(A, 1, 7)
    assert A == E


def test_partition_1():
    A = [2, 8, 7, 1, 3, 5, 6, 4]
    E = [2, 1, 3, 4, 7, 5, 6, 8]
    eq = 4
    aq = partition(A, 1, 8)
    assert aq == eq
    assert A == E


def test_partition_2():
    A = [1.1, 10.1, 2, 8, 7, 1, 3, 5, 6, 4, 1.2, 10.2]
    E = [1.1, 10.1, 2, 1, 3, 4, 7, 5, 6, 8, 1.2, 10.2]
    eq = 6
    aq = partition(A, 3, 10)
    assert aq == eq
    assert A == E


def test_partition_3():
    A = [2, 8]
    E = [2, 8]
    eq = 2
    aq = partition(A, 1, 2)
    assert aq == eq
    assert A == E


def test_partition_4():
    A = [8, 2]
    E = [2, 8]
    eq = 1
    aq = partition(A, 1, 2)
    assert aq == eq
    assert A == E


def test_randomized_quick_sort():
    A = [5, 3, 2, 7, 10, 9, 3]
    E = [2, 3, 3, 5, 7, 9, 10]
    quick_sort(A, 1, 7)
    assert A == E
