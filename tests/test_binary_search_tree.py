# -*- coding: utf-8 -*-

from src.binary_search_tree import *


def gen_tree():
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


def test_inorder_tree_walk():
    bst, x1, x2, x3, x4 = gen_tree()
    bst.inorder_tree_walk(x1)
    bst.inorder_tree_walk(x2)
    bst.inorder_tree_walk(x3)
    bst.inorder_tree_walk(x4)
    bst.inorder_tree_walk(None)


def test_search():
    bst, x1, x2, x3, x4 = gen_tree()
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
    bst, x1, x2, x3, x4 = gen_tree()
    assert bst.minimum(x1) == x1
    assert bst.minimum(x2) == x1
    assert bst.minimum(x3) == x3
    assert bst.minimum(x4) == x1


def test_successor():
    bst, x1, x2, x3, x4 = gen_tree()
    assert bst.successor(x1) == x2
    assert bst.successor(x2) == x3
    assert bst.successor(x3) == x4
    assert bst.successor(x4) is None
