# -*- coding: utf-8 -*-

from src.van_emde_boas_tree import *

def test_high():
    # 256
    h = high(2 ** 8)
    assert h(0) == 0
    assert h(15) == 0
    assert h(16) == 1
    assert h(256) == 16
    assert h(261) == 16

    # 128
    h = high(2 ** 7)
    assert h(0) == 0
    assert h(10) == 0
    assert h(11) == 1
    assert h(261) == 23


def test_low():
    # 256
    l = low(2 ** 8)
    assert l(0) == 0
    assert l(15) == 15
    assert l(16) == 0
    assert l(256) == 0
    assert l(261) == 5

    # 128
    l = low(2 ** 7)
    assert l(0) == 0
    assert l(10) == 10
    assert l(11) == 0
    assert l(261) == 8


def test_index():
    # 256
    i = index(2 ** 8)
    assert i(0, 0) == 0
    assert i(1, 1) == 17
    assert i(3, 5) == 53

    # 128
    i = index(2 ** 7)
    assert i(0, 0) == 0
    assert i(1, 1) == 12
    assert i(3, 5) == 38


def test_init():
    vEB = VanEmdeBoas(16)
    assert vEB.summary.u == 4
    assert len(vEB.cluster) == 4
    assert vEB.cluster[3].u ==  4
    assert len(vEB.cluster[3].cluster) == 2
    assert vEB.cluster[3].summary.u == 2

    assert vEB.summary.summary.u == 2
    assert len(vEB.summary.cluster) == 2
    assert vEB.summary.cluster[0].u == 2
    assert vEB.summary.cluster[0].summary == None
    assert vEB.summary.cluster[0].cluster == None


def gen_tree():
    """Page 456 Fig. 20.6
    {2,3,4,5,7,14,15}
    """
    vEB = VanEmdeBoas(16)
    vEB.min = 2
    vEB.max = 15

    vEB.summary.min = 0
    vEB.summary.max = 3
    vEB.summary.summary.min = 0
    vEB.summary.summary.max = 1
    vEB.summary.cluster[0].min = 1
    vEB.summary.cluster[0].max = 1
    vEB.summary.cluster[1].min = 1
    vEB.summary.cluster[1].max = 1

    vEB.cluster[0].min = 3
    vEB.cluster[1].min = 0
    vEB.cluster[2].min = None
    vEB.cluster[3].min = 2

    vEB.cluster[0].max = 3
    vEB.cluster[1].max = 3
    vEB.cluster[2].max = None
    vEB.cluster[3].max = 3

    vEB.cluster[1].summary.min = 0
    vEB.cluster[1].summary.max = 1
    vEB.cluster[3].summary.min = 1
    vEB.cluster[3].summary.max = 1

    vEB.cluster[1].cluster[0].min = 1
    vEB.cluster[1].cluster[0].max = 1
    vEB.cluster[1].cluster[1].min = 1
    vEB.cluster[1].cluster[1].max = 1
    vEB.cluster[3].cluster[1].min = 1
    vEB.cluster[3].cluster[1].max = 1

    return vEB


def test_member():
    vEB = gen_tree()
    assert vEB.member(0) == False
    assert vEB.member(1) == False
    assert vEB.member(2) == True
    assert vEB.member(3) == True
    assert vEB.member(4) == True
    assert vEB.member(5) == True
    assert vEB.member(6) == False
    assert vEB.member(7) == True
    assert vEB.member(8) == False
    assert vEB.member(9) == False
    assert vEB.member(10) == False
    assert vEB.member(11) == False
    assert vEB.member(12) == False
    assert vEB.member(13) == False
    assert vEB.member(14) == True
    assert vEB.member(15) == True


def test_member():
    vEB = gen_tree()
    assert vEB.successor(0) == 2
    assert vEB.successor(1) == 2
    assert vEB.successor(2) == 3
    assert vEB.successor(3) == 4
    assert vEB.successor(4) == 5
    assert vEB.successor(5) == 7
    assert vEB.successor(6) == 7
    assert vEB.successor(7) == 14
    assert vEB.successor(8) == 14
    assert vEB.successor(9) == 14
    assert vEB.successor(10) == 14
    assert vEB.successor(11) == 14
    assert vEB.successor(12) == 14
    assert vEB.successor(13) == 14
    assert vEB.successor(14) == 15
    assert vEB.successor(15) == None
