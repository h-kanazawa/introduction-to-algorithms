# -*- coding: utf-8 -*-

from src.dijkstra import *


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
        s: [(t, 10), (y, 5)],
        t: [(x, 1), (y, 2)],
        x: [(z, 4)],
        y: [(t, 3), (x, 9), (z, 2)],
        z: [(x, 6), (s, 7)]
    }

    return graph, (s, t, x, y, z)


def test_dijkstra():
    g, vs = gen_graph()
    s, t, x, y, z = vs
    dijkstra(g, s)

    assert s.d == 0
    assert t.d == 8
    assert x.d == 9
    assert y.d == 5
    assert z.d == 7

    assert s.π is None
    assert t.π == y
    assert x.π == t
    assert y.π == s
    assert z.π == y
