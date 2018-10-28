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

    return graph, (a, b, c, d, e, f, g, h)


def test_has_weight_error():
    g, _ = gen_graph()
    assert g.has_weight_error() is False


def test_mst_kruskal():
    """Figure 23.1 and 23.4
    """

    g, _ = gen_graph()
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


def test_mst_prim():
    """Figure 23.5
    """
    G, vs = gen_graph()
    a, b, c, d, e, f, g, h = vs

    mst_prim(G, a)

    assert a.π is None
    assert b.π == a
    assert c.π == b
    assert d.π == c
    assert e.π == d
    assert f.π == c
    assert g.π == f
    assert h.π == g

    assert a.key == 0
    assert b.key == 4
    assert c.key == 8
    assert d.key == 7
    assert e.key == 9
    assert f.key == 4
    assert g.key == 2
    assert h.key == 1

