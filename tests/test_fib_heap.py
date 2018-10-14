# -*- coding: utf-8 -*-

from src.fib_heap import *


################################################################
# Tests for X
################################################################


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


def test_remove_myself_from_siblings():
    x1 = X(1, 'x1')
    x2 = X(2, 'x2')
    x3 = X(3, 'x3')
    x4 = X(4, 'x4')
    x5 = X(5, 'x5')
    x1.add_to_right(x4)
    x1.add_to_right(x2)
    x1.add_to_right(x5)
    x1.add_to_right(x3)
    assert x1.siblings_r() == [x1, x3, x5, x2, x4]

    x3.remove_myself_from_siblings()
    assert x3.siblings_r() == [x3]
    assert x1.siblings_r() == [x1, x5, x2, x4]

    x1.remove_myself_from_siblings()
    assert x1.siblings_r() == [x1]
    assert x2.siblings_r() == [x2, x4, x5]


def add_child():
    x1 = X(1, 'x1')
    x2 = X(2, 'x2')
    x3 = X(3, 'x3')
    x1.add_child(x2)
    assert x1.c == x2
    assert x2.p == x1
    assert x1.d == 1

    x1.add_child(x3)
    assert x1.c == x2
    assert x2.p == x1
    assert x3.p == x1
    assert x1.d == 2
    assert x2.siblings_r == [x2, x3]
    assert x2.siblings_l == [x3, x2]


################################################################
# Tests for FibHeap
################################################################


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
    assert fh.min == x2
    assert fh.root_list() == [x2]

    fh.insert(x3)
    assert fh.n == 2
    assert fh.min == x2
    assert fh.root_list() == [x2, x3]

    fh.insert(x1)
    assert fh.n == 3
    assert fh.min == x1
    assert fh.root_list() == [x1, x3, x2]


def test_extract_min_if_heap_is_empty():
    fh = FibHeap()
    z = fh.extract_min()
    assert z == None


def test_extract_min_if_heap_has_one_root_with_no_children():
    x1 = X(1, 'x1')
    fh = FibHeap()
    fh.insert(x1)
    z = fh.extract_min()
    assert z == x1
    assert fh.min == None
    assert fh.root_list() == []


def test_extract_min_with_no_children():
    x1 = X(1, 'x1')
    x2 = X(2, 'x2')
    x3 = X(3, 'x3')
    x4 = X(4, 'x4')
    x5 = X(5, 'x5')

    fh = FibHeap()
    fh.insert(x1)
    fh.insert(x4)
    fh.insert(x2)
    fh.insert(x5)
    fh.insert(x3)
    assert fh.root_list() == [x1, x3, x5, x2, x4]

    z = fh.extract_min()
    """
    expect
    [2]   ...root_list
     ↕↖
    [4↔3]
       ↕
      [5]
    """
    assert z == x1
    assert fh.min == x2
    assert fh.n == 4

    assert x2.d == 2
    assert x2.children() == [x4, x3]
    assert x2.p == None

    assert x3.d == 1
    assert x3.children() == [x5]
    assert x3.p == x2

    assert x4.d == 0
    assert x4.children() == []
    assert x4.p == x2

    assert x5.d == 0
    assert x5.children() == []
    assert x5.p == x3


def test_extract_min_with_children():
    """
    Fig 19.4
    page 428
    """
    x23 = X(23, 'x23')
    x7 = X(7, 'x7')
    x21 = X(21, 'x21')
    x3 = X(3, 'x3')
    x18 = X(18, 'x18')
    x39 = X(39, 'x39')
    x52 = X(52, 'x52')
    x38 = X(38, 'x38')
    x41 = X(41, 'x41')
    x17 = X(17, 'x17')
    x30 = X(30, 'x30')
    x24 = X(24, 'x24')
    x26 = X(26, 'x26')
    x35 = X(35, 'x35')
    x46 = X(46, 'x46')

    x18.mark = True
    x39.mark = True
    x26.mark = True

    x23.add_to_right(x7)
    x7.add_to_right(x21)
    x21.add_to_right(x3)
    x3.add_to_right(x17)
    x17.add_to_right(x24)

    x3.add_child(x18)
    x3.add_child(x38)
    x3.add_child(x52)
    x18.add_child(x39)
    x38.add_child(x41)
    x17.add_child(x30)
    x24.add_child(x26)
    x24.add_child(x46)
    x26.add_child(x35)

    fh = FibHeap()
    fh.insert(x3)
    fh.n = 15

    fh.extract_min()

    print([r.k for r in fh.root_list()])
    assert fh.n == 14
    assert fh.min == x7
    assert fh.root_list() == [x7, x18, x38]

    assert x7.children() == [x23, x24, x17]
    assert x7.d == 3
    assert x7.p is None

    assert x23.children() == []
    assert x23.d == 0
    assert x23.p == x7

    assert x24.children() == [x26, x46]
    assert x24.d == 2
    assert x24.p == x7

    assert x46.children() == []
    assert x46.d == 0
    assert x46.p == x24

    assert x26.children() == [x35]
    assert x26.d == 1
    assert x26.p == x24

    assert x35.children() == []
    assert x35.d == 0
    assert x35.p == x26

    assert x17.children() == [x30]
    assert x17.d == 1
    assert x17.p == x7

    assert x30.children() == []
    assert x30.d == 0
    assert x30.p == x17

    assert x18.children() == [x39, x21]
    assert x18.d == 2
    assert x18.p is None

    assert x39.children() == []
    assert x39.d == 0
    assert x39.p == x18

    assert x21.children() == [x52]
    assert x21.d == 1
    assert x21.p == x18

    assert x52.children() == []
    assert x52.d == 0
    assert x52.p == x21

    assert x38.children() == [x41]
    assert x38.d == 1
    assert x38.p is None

    assert x41.children() == []
    assert x41.d == 0
    assert x41.p == x38


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
