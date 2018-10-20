# -*- coding: utf-8 -*-

from src.disjoint_set import *

def range_to_set(ns):
    s = None
    for n in ns:
        x = X(n)
        if s is None:
            s = Set(x)
        else:
            temp_s = Set(x)
            union(s.head, x)
    return s


def test_make_set():
    x = X(4)
    s = Set(x)
    assert s.head == s.tail
    assert s.head.set == s
    assert s.head.v == 4
    assert s.w == 1


def test_union():
    x1 = X(4)
    x2 = X(7)
    x3 = X(3)
    s1 = Set(x1)
    s2 = Set(x2)
    s3 = Set(x3)

    su1, _ = union(x1, x2)
    su2, _ = union(x3, x2)
    assert su1.to_v_list() == [4, 7]
    assert su1.w == 2
    assert su1.tail == x2
    assert su2.to_v_list() == [3, 4, 7]
    assert su2.w == 3
    assert su2.tail == x2


def test_weighted_union():
    s1 = range_to_set(range(0, 5))
    s2 = range_to_set(range(6, 10))
    s1_s2, _ = weighted_union(s1.head, s2.head)
    assert s1_s2.to_v_list() == [0, 1, 2, 3, 4, 6, 7, 8, 9]

    s3 = range_to_set(range(0, 5))
    s4 = range_to_set(range(6, 10))
    s4_s3, _ = weighted_union(s4.head, s3.head)
    assert s4_s3.to_v_list() == [0, 1, 2, 3, 4, 6, 7, 8, 9]


def test_exercise_21_2_2():
    xs = [X(i) for i in range(0, 17)]

    all_sets = set()
    for i in range(1, 17):
        all_sets = all_sets | {Set(xs[i])}
    print([a.to_v_list() for a in all_sets])

    for i in range(1, 16, 2):
        _, should_be_deleted = weighted_union(xs[i], xs[i + 1])
        all_sets -= {should_be_deleted}
    print([a.to_v_list() for a in all_sets])

    for i in range(1, 14, 4):
        _, should_be_deleted = weighted_union(xs[i], xs[i + 2])
        all_sets -= {should_be_deleted}
    print([a.to_v_list() for a in all_sets])

    _, should_be_deleted = weighted_union(xs[1], xs[5])
    all_sets -= {should_be_deleted}
    print([a.to_v_list() for a in all_sets])

    _, should_be_deleted = weighted_union(xs[11], xs[13])
    all_sets -= {should_be_deleted}
    print([a.to_v_list() for a in all_sets])

    _, should_be_deleted = weighted_union(xs[1], xs[10])
    all_sets -= {should_be_deleted}
    print([a.to_v_list() for a in all_sets])

    assert xs[2].find_set() == xs[1]
    assert xs[9].find_set() == xs[1]

    # assert False

