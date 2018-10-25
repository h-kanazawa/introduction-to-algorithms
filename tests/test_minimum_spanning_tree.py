# -*- coding: utf-8 -*-

from src.minimum_spanning_tree import *


def gen_graph():
    # vertexes
    a = V('a')
    b = V('b')
    c = V('c')
    d = V('d')
    e = V('e')
    f = V('f')
    g = V('g')
    h = V('h')
    i = V('i')

    graph = G()

    # edges
    graph.Adj = {
        a: [(b, 4), (h, 8)],
        b: [(a, 4), (c, 8), (h, 11)],
        c: [(b, 8), (d, 7), (f, 4), (i, 2)],
        d: [(c, 7), (e, 9), (f, 14)],
        e: [(d, 9), (f, 10)],
        f: [(c, 4), (d, 14), (e, 10), (g, 2)],
        g: [(f, 2), (h, 1), (i, 6)],
        h: [(a, 8), (b, 11), (i, 7), (g, 1)],
        i: [(c, 2), (g, 6), (h, 7)],
    }

    return graph


def test_has_weight_error():
    g = gen_graph()
    assert g.has_weight_error() is False


def test_mst_kruskal():
    """Figure 23.1 and 23.4
    """

    g = gen_graph()
    A = mst_kruskal(g)
    actual = set([frozenset([list(a)[0].v, list(a)[1].v]) for a in A])

    # Figure 23.4
    expected1 = set([
        frozenset(['b', 'a']),
        frozenset(['a', 'h']),
        frozenset(['h', 'g']),
        frozenset(['g', 'f']),
        frozenset(['f', 'c']),
        frozenset(['i', 'c']),
        frozenset(['c', 'd']),
        frozenset(['d', 'e']),
    ])

    # Figure 23.1
    expected2 = set([
        frozenset(['b', 'a']),
        frozenset(['b', 'c']),
        frozenset(['h', 'g']),
        frozenset(['g', 'f']),
        frozenset(['f', 'c']),
        frozenset(['i', 'c']),
        frozenset(['c', 'd']),
        frozenset(['d', 'e']),
    ])
    assert actual == expected1 or actual == expected2
