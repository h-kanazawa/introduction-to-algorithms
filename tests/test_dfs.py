# -*- coding: utf-8 -*-

from src.dfs import *


def test_DFS():
    """Figure 22.4, Page 504
    """
    # vertexes
    u = V()
    v = V()
    w = V()
    x = V()
    y = V()
    z = V()

    # glaph
    g = G()
    g.Adj = {
        u: [v, x],
        v: [y],
        w: [y, z],
        x: [v],
        y: [x],
        z: [z]
    }

    dfs = DFS(g)
    for a in g.V():
        assert a.color == Color.BLACK

    assert u.d == 1
    assert v.d == 2
    assert w.d == 9
    assert x.d == 4
    assert y.d == 3
    assert z.d == 10

    assert u.f == 8
    assert v.f == 7
    assert w.f == 12
    assert x.f == 5
    assert y.f == 6
    assert z.f == 11

    assert u.π == None
    assert v.π == u
    assert w.π == None
    assert x.π == y
    assert y.π == v
    assert z.π == w
