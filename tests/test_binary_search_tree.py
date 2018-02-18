# -*- coding: utf-8 -*-

from src.binary_search_tree import *


def gen_tree_1():
    """
    4
    ├───────┐
    2       -
    ├───┐
    1   3
    ├─┐ ├─┐
    - - - -
    """
    x2 = X(2, '20', None, None, None)
    x1 = X(1, '10', None, None, x2)
    x3 = X(3, '30', None, None, x2)
    x4 = X(4, '40', x2, None, None)
    x2.l = x1
    x2.r = x3
    x2.p = x4
    bst = BinarySearchTree()
    bst.root = x4
    return (bst, x1, x2, x3, x4)


def gen_tree_2():
    """
    4
    ├───────┐
    2       9
    ├───┐   ├─────────┐
    1   3   7         12
    ├─┐ ├─┐ ├─────┐   ├───┐
    - - - - 5     8   10  15
            ├─┐   ├─┐ ├─┐ ├─┐
            - 6   - - - - - -
              ├─┐
              - -
    """
    x1 = X(1, '10', None, None, None)
    x2 = X(2, '20', None, None, None)
    x3 = X(3, '30', None, None, None)
    x4 = X(4, '40', None, None, None)
    x5 = X(5, '50', None, None, None)
    x6 = X(6, '60', None, None, None)
    x7 = X(7, '70', None, None, None)
    x8 = X(8, '80', None, None, None)
    x9 = X(9, '90', None, None, None)
    x10 = X(10, '100', None, None, None)
    x12 = X(12, '120', None, None, None)
    x15 = X(15, '150', None, None, None)

    bst = BinarySearchTree()
    bst.root = x4

    bst.insert(x2)
    bst.insert(x9)

    bst.insert(x1)
    bst.insert(x3)
    bst.insert(x7)
    bst.insert(x12)

    bst.insert(x5)
    bst.insert(x8)
    bst.insert(x10)
    bst.insert(x15)

    bst.insert(x6)

    return (bst, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x12, x15)


def test_inorder_tree_walk():
    bst, x1, x2, x3, x4 = gen_tree_1()
    bst.inorder_tree_walk(x1)
    bst.inorder_tree_walk(x2)
    bst.inorder_tree_walk(x3)
    bst.inorder_tree_walk(x4)
    bst.inorder_tree_walk(None)


def test_search():
    bst, x1, x2, x3, x4 = gen_tree_1()
    for f in [bst.iterative_tree_search, bst.search]:
        assert f(x1, 1) == x1
        assert f(x1, 2) is None
        assert f(x1, 3) is None
        assert f(x1, 4) is None

        assert f(x2, 1) == x1
        assert f(x2, 2) == x2
        assert f(x2, 3) == x3
        assert f(x2, 4) is None

        assert f(x3, 1) is None
        assert f(x3, 2) is None
        assert f(x3, 3) == x3
        assert f(x3, 4) is None

        assert f(x4, 1) == x1
        assert f(x4, 2) == x2
        assert f(x4, 3) == x3
        assert f(x4, 4) == x4


def test_minimum():
    bst, x1, x2, x3, x4 = gen_tree_1()
    assert bst.minimum(x1) == x1
    assert bst.minimum(x2) == x1
    assert bst.minimum(x3) == x3
    assert bst.minimum(x4) == x1


def test_successor():
    bst, x1, x2, x3, x4 = gen_tree_1()
    assert bst.successor(x1) == x2
    assert bst.successor(x2) == x3
    assert bst.successor(x3) == x4
    assert bst.successor(x4) is None


def test_insert():
    bst, x1, x2, x3, x4 = gen_tree_1()
    x0 = X(0, '0', None, None, None)
    bst.insert(x0)
    assert x0 == X(0, '0', None, None, x1)
    assert x1 == X(1, '10', x0, None, x2)
    x5 = X(5, '50', None, None, None)
    bst.insert(x5)
    assert x5 == X(5, '50', None, None, x4)
    assert x4 == X(4, '40', x2, x5, None)


def test_delete_1():
    bst, x1, x2, x3, x4 = gen_tree_1()
    bst.delete(1)
    assert x2 == X(2, '20', None, x3, x4)
    bst.delete(4)
    assert bst.root == X(2, '20', None, x3, None)


def test_delete_2():
    """Case 12.4(c) on Page 246
    """
    bst, x1, x2, x3, x4 = gen_tree_1()
    x35 = X(3.5, '35', None, None, None)
    bst.insert(x35)
    assert x2 == X(2, '20', x1, x3, x4)
    assert x3 == X(3, '30', None, x35, x2)
    assert x35 == X(3.5, '35', None, None, x3)
    bst.delete(3)
    assert x2 == X(2, '20', x1, x35, x4)
    assert x35 == X(3.5, '35', None, None, x2)


def test_delete_3():
    """Case 12.4(d) on Page 246
    Expected Tree after deleted "4"
    5
    ├───────┐
    2       9
    ├───┐   ├───────┐
    1   3   7       12
    ├─┐ ├─┐ ├───┐   ├───┐
    - - - - 6   8   10  15
            ├─┐ ├─┐ ├─┐ ├─┐
            - - - - - - - -
    """
    bst, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x12, x15 = gen_tree_2()
    bst.delete(4)
    assert bst.root == X(5, '50', x2, x9, None)
    assert x2 == X(2, '20', x1, x3, x5)
    assert x9 == X(9, '90', x7, x12, x5)
    assert x7 == X(7, '70', x6, x8, x9)
    assert x6 == X(6, '60', None, None, x7)
