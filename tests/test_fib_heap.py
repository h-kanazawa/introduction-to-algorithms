# -*- coding: utf-8 -*-

from src.fib_heap import *


def test_add_to_right_with_1_element():
    # original [x1]
    x1 = X(1, 'x1')

    # add x2
    x2 = X(2, 'x2')
    x1.add_to_right(x2)

    # expect [x1, x2]
    assert x1.siblings_r() == [x1, x2]
    assert x1.siblings_l() == [x2, x1]


def test_add_to_right_with_2_elements():
    # original [x1, x3]
    x1 = X(1, 'x1')
    x3 = X(3, 'x3')
    x1.r = x3
    x1.l = x3
    x3.r = x1
    x3.l = x1

    # add x2
    x2 = X(2, 'x2')
    x1.add_to_right(x2)

    # expect [x1, x2, x3]
    assert x1.siblings_r() == [x1, x2, x3]
    assert x1.siblings_l() == [x2, x3, x1]

def test_add_to_right_with_3_elements():
    # original [x1, x3, x4]
    x1 = X(1, 'x1')
    x3 = X(3, 'x3')
    x4 = X(4, 'x4')
    x1.r = x3
    x1.l = x4
    x3.r = x4
    x3.l = x1
    x4.r = x1
    x4.l = x3

    # add x2
    x2 = X(2, 'x2')
    x1.add_to_right(x2)

    # expect [x1, x2, x3, x4]
    assert x1.siblings_r() == [x1, x2, x3, x4]
    assert x1.siblings_l() == [x2, x3, x4, x1]


def test_link_list():
    # original list [x1, x3, x4]
    x1 = X(1, 'x1')
    x3 = X(3, 'x3')
    x4 = X(4, 'x4')
    x1.r = x3
    x1.l = x4
    x3.r = x4
    x3.l = x1
    x4.r = x1
    x4.l = x3

    # another list [x2, x5]
    x2 = X(2, 'x2')
    x5 = X(5, 'x5')
    x2.r = x5
    x2.l = x5
    x5.r = x2
    x5.l = x2

    x3.link_list(x5)

    # expect [x1, x3, x5, x2, x4]
    assert x1.siblings_r() == [x1, x3, x5, x2, x4]
    assert x1.siblings_l() == [x3, x5, x2, x4, x1]


def test_init():
    fh = FibHeap()
    assert fh.min == None
    assert fh.n == 0


def test_insert():
    x1 = X(1, 'x1')
    x2 = X(2, 'x2')
    x3 = X(3, 'x3')

    fh = FibHeap()
    assert fh.root_list() == []

    fh.insert(x2)
    assert fh.n == 1
    assert fh.min.v == 'x2'
    assert fh.root_list() == [x2]

    fh.insert(x3)
    assert fh.n == 2
    assert fh.min.v == 'x2'
    assert fh.root_list() == [x2, x3]

    fh.insert(x1)
    assert fh.n == 3
    assert fh.min.v == 'x1'
    assert fh.root_list() == [x1, x3, x2]


def test_union():
    x1 = X(1, 'x1')
    x2 = X(2, 'x2')
    x3 = X(3, 'x3')
    x4 = X(4, 'x4')
    x5 = X(5, 'x5')

    # H1 [x1, x4, x3]
    H1 = FibHeap()
    H1.insert(x4)
    H1.insert(x3)
    H1.insert(x1)

    # H2 [x2, x5]
    H2 = FibHeap()
    H2.insert(x5)
    H2.insert(x2)

    # union(H1, H2)
    H = union(H1, H2)
    assert H.root_list() == [x1, x2, x5, x4, x3]
