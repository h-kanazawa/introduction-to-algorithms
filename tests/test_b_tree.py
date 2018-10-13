# -*- coding: utf-8 -*-

from src.b_tree import *

def gen_tree_1():
    """
    t = 2

        x3
    x12 3  x4
    1 2    4
    """
    x12 = X(2, [KV(1, 'k1'), KV(2, 'k2')], [], True)
    x4 = X(1, [KV(4, 'k4')], [], True)
    x3 = X(1, [KV(3, 'k3')], [x12, x4], False)

    bt = BTree(2)
    bt.root = x3
    return bt


def gen_tree_2():
    """
    See: page. 414
           GMPX
    ACDE JK NO RSTUV YZ
    """
    xACDE = X(4, [
        KV(1, 'A'),
        KV(3, 'C'),
        KV(4, 'D'),
        KV(5, 'E'),
    ], [], True)

    xJK = X(2, [
        KV(10, 'J'),
        KV(11, 'K'),
    ], [], True)

    xNO = X(2, [
        KV(14, 'N'),
        KV(15, 'O'),
    ], [], True)

    xRSTUV = X(5, [
        KV(18, 'R'),
        KV(19, 'S'),
        KV(20, 'T'),
        KV(21, 'U'),
        KV(22, 'V'),
    ], [], True)

    xYZ = X(2, [
        KV(25, 'Y'),
        KV(26, 'Z'),
    ], [], True)

    xGMPX = X(4, [
        KV(7, 'G'),
        KV(13, 'M'),
        KV(16, 'P'),
        KV(24, 'X'),
    ], [xACDE, xJK, xNO, xRSTUV, xYZ], False)

    bt = BTree(3)
    bt.root = xGMPX
    return bt


def test_init():
    bt = BTree(2)
    assert len(bt.root.c) == 0


def test_search():
    bt = gen_tree_1()

    assert bt.search(1).v == 'k1'
    assert bt.count_disk_read == 1
    assert bt.search(2).v == 'k2'
    assert bt.count_disk_read == 1
    assert bt.search(3).v == 'k3'
    assert bt.count_disk_read == 0
    assert bt.search(4).v == 'k4'
    assert bt.count_disk_read == 1
    assert bt.search(0) == None
    assert bt.count_disk_read == 1
    assert bt.search(5) == None
    assert bt.count_disk_read == 1


def test_split_child():
    bt = gen_tree_2()
    bt.split_child(bt.root, 3)
    assert [kv.v for kv in bt.root.keys] == ['G', 'M', 'P', 'T', 'X']
    assert bt.root.n == 5
    assert [kv.v for kv in bt.root.c[3].keys] == ['R', 'S']
    assert bt.root.c[3].n == 2
    assert [kv.v for kv in bt.root.c[4].keys] == ['U', 'V']
    assert bt.root.c[4].n == 2


def test_insert():
    """See page 414
    """
    bt = gen_tree_2()
    assert bt.root.n == 4
    assert [kv.v for kv in bt.root.keys] == ['G', 'M', 'P', 'X']
    assert [kv.v for kv in bt.root.c[0].keys] == ['A', 'C', 'D', 'E']
    assert [kv.v for kv in bt.root.c[1].keys] == ['J', 'K']
    assert [kv.v for kv in bt.root.c[2].keys] == ['N', 'O']
    assert [kv.v for kv in bt.root.c[3].keys] == ['R', 'S', 'T', 'U', 'V']
    assert [kv.v for kv in bt.root.c[4].keys] == ['Y', 'Z']
    assert len(bt.root.c) == 5

    # Insert B
    bt.insert(KV(2, 'B'))
    assert bt.root.n == 4
    assert [kv.v for kv in bt.root.keys] == ['G', 'M', 'P', 'X']
    assert [kv.v for kv in bt.root.c[0].keys] == ['A', 'B', 'C', 'D', 'E']
    assert [kv.v for kv in bt.root.c[1].keys] == ['J', 'K']
    assert [kv.v for kv in bt.root.c[2].keys] == ['N', 'O']
    assert [kv.v for kv in bt.root.c[3].keys] == ['R', 'S', 'T', 'U', 'V']
    assert [kv.v for kv in bt.root.c[4].keys] == ['Y', 'Z']
    assert len(bt.root.c) == 5

    # Insert Q
    bt.insert(KV(17, 'Q'))
    assert bt.root.n == 5
    assert [kv.v for kv in bt.root.keys] == ['G', 'M', 'P', 'T', 'X']
    assert [kv.v for kv in bt.root.c[0].keys] == ['A', 'B', 'C', 'D', 'E']
    assert [kv.v for kv in bt.root.c[1].keys] == ['J', 'K']
    assert [kv.v for kv in bt.root.c[2].keys] == ['N', 'O']
    assert [kv.v for kv in bt.root.c[3].keys] == ['Q', 'R', 'S']
    assert [kv.v for kv in bt.root.c[4].keys] == ['U', 'V']
    assert [kv.v for kv in bt.root.c[5].keys] == ['Y', 'Z']
    assert len(bt.root.c) == 6

    # Insert L
    bt.insert(KV(12, 'L'))
    # depth 0
    assert bt.root.n == 1
    assert bt.root.is_leaf == False
    assert [kv.v for kv in bt.root.keys] == ['P']
    assert len(bt.root.c) == 2

    # depth 1
    assert bt.root.c[0].n == 2
    assert bt.root.c[0].is_leaf == False
    assert [kv.v for kv in bt.root.c[0].keys] == ['G', 'M']
    assert len(bt.root.c[0].c) == 3

    assert bt.root.c[1].n == 2
    assert bt.root.c[1].is_leaf == False
    assert [kv.v for kv in bt.root.c[1].keys] == ['T', 'X']
    assert len(bt.root.c[1].c) == 3

    # depth 2
    bt.root.c[0].c[0].n = 5
    assert bt.root.c[0].c[0].is_leaf == True
    assert [kv.v for kv in bt.root.c[0].c[0].keys] == ['A', 'B', 'C', 'D', 'E']
    assert len(bt.root.c[0].c[0].c) == 0

    bt.root.c[0].c[1].n = 3
    assert bt.root.c[0].c[1].is_leaf == True
    assert [kv.v for kv in bt.root.c[0].c[1].keys] == ['J', 'K', 'L']
    assert len(bt.root.c[0].c[1].c) == 0

    bt.root.c[0].c[2].n = 2
    assert bt.root.c[0].c[2].is_leaf == True
    assert [kv.v for kv in bt.root.c[0].c[2].keys] == ['N', 'O']
    assert len(bt.root.c[0].c[2].c) == 0

    bt.root.c[1].c[0].n = 3
    assert bt.root.c[1].c[0].is_leaf == True
    assert [kv.v for kv in bt.root.c[1].c[0].keys] == ['Q', 'R', 'S']
    assert len(bt.root.c[1].c[0].c) == 0

    bt.root.c[1].c[1].n = 2
    assert bt.root.c[1].c[1].is_leaf == True
    assert [kv.v for kv in bt.root.c[1].c[1].keys] == ['U', 'V']
    assert len(bt.root.c[1].c[1].c) == 0

    bt.root.c[1].c[2].n = 3
    assert bt.root.c[1].c[2].is_leaf == True
    assert [kv.v for kv in bt.root.c[1].c[2].keys] == ['Y', 'Z']
    assert len(bt.root.c[1].c[2].c) == 0


    # Insert F
    bt.insert(KV(6, 'F'))
    assert [kv.v for kv in bt.root.keys] == ['P']
    assert [kv.v for kv in bt.root.c[0].keys] == ['C', 'G', 'M']
    assert [kv.v for kv in bt.root.c[1].keys] == ['T', 'X']
    assert [kv.v for kv in bt.root.c[0].c[0].keys] == ['A', 'B']
    assert [kv.v for kv in bt.root.c[0].c[1].keys] == ['D', 'E', 'F']
    assert [kv.v for kv in bt.root.c[0].c[2].keys] == ['J', 'K', 'L']
    assert [kv.v for kv in bt.root.c[0].c[3].keys] == ['N', 'O']
    assert [kv.v for kv in bt.root.c[1].c[0].keys] == ['Q', 'R', 'S']
    assert [kv.v for kv in bt.root.c[1].c[1].keys] == ['U', 'V']
    assert [kv.v for kv in bt.root.c[1].c[2].keys] == ['Y', 'Z']
