# -*- coding: utf-8 -*-

from src.bellman_ford import *


def gen_graph():
    # vertexes
    s = V('s')
    t = V('t')
    x = V('x')
    y = V('y')
    z = V('z')

    graph = G()

    # edges
    graph.Adj = {
        s: [(t, 6), (y, 7)],
        t: [(x, 5), (z, -4), (y, 8)],
        x: [(t, -2)],
        y: [(x, -3), (z, 9)],
        z: [(s, 2), (x, 7)]
    }

    return graph, (s, t, x, y, z)


def test_bellman_ford():
    g, vs = gen_graph()
    s, t, x, y, z = vs
    result = bellman_ford(g, s)

    assert result is True

    assert s.d == 0
    assert t.d == 2
    assert x.d == 4
    assert y.d == 7
    assert z.d == -2

    assert s.π is None
    assert t.π == x
    assert x.π == y
    assert y.π == s
    assert z.π == t
