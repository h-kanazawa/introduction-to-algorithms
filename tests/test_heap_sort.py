# -*- coding: utf-8 -*-

from src.heap_sort import *


def test_parent():
    assert parent(2) == 1
    assert parent(3) == 1
    assert parent(4) == 2
    assert parent(5) == 2
    assert parent(6) == 3
    assert parent(10) == 5
    assert parent(101) == 50


def test_left():
    assert left(1) == 2
    assert left(2) == 4
    assert left(43) == 86


def test_right():
    assert right(1) == 3
    assert right(2) == 5
    assert right(43) == 87


def test_max_heapfy_when_parent_is_largest_1():
    H = [3, 1, 2]
    max_heapfy(H, 1, 3)
    assert H == [3, 1, 2]


def test_max_heapfy_when_parent_is_largest_2():
    H = [3, 2, 1]
    max_heapfy(H, 1, 3)
    assert H == [3, 2, 1]


def test_max_heapfy_when_left_is_largest_1():
    H = [1, 3, 2]
    max_heapfy(H, 1, 3)
    assert H == [3, 1, 2]


def test_max_heapfy_when_left_is_largest_2():
    H = [2, 3, 1]
    max_heapfy(H, 1, 3)
    assert H == [3, 2, 1]


def test_max_heapfy_when_right_is_largest_1():
    H = [2, 1, 3]
    max_heapfy(H, 1, 3)
    assert H == [3, 1, 2]


def test_max_heapfy_when_right_is_largest_2():
    H = [1, 2, 3]
    max_heapfy(H, 1, 3)
    assert H == [3, 2, 1]


def test_max_heapfy():
    # See: Page 127
    """
    16
    ├──────┐
    4      10
    ├───┐  ├─┐
    14  7  9 3
    ├─┐ │
    2 8 1
    """
    H = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]

    """
    16
    ├──────┐
    14     10
    ├───┐  ├─┐
    8   7  9 3
    ├─┐ │
    2 4 1
    """
    E = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

    max_heapfy(H, 2, 10)
    assert H == E


def test_build_max_heap():
    # See: Page 129
    A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    build_max_heap(A)
    assert A == [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]


def test_heap_sort():
    A = [5, 3, 2, 7, 10, 9, 3]
    E = [2, 3, 3, 5, 7, 9, 10]
    heap_sort(A)
    assert A == E
