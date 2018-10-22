# -*- coding: utf-8 -*-

from src.bfs import *


def test_BFS():
    """Figure 22.3, Page 497
    """
    # vertexes
    r = V()
    s = V()
    t = V()
    u = V()
    v = V()
    w = V()
    x = V()
    y = V()

    # glaph
    g = G()
    g.Adj = {
        r: [v, s],
        s: [r, w],
        t: [w, x, u],
        u: [t, x, y],
        v: [r],
        w: [s, t, x],
        x: [w, t, u, y],
        y: [u, x]
    }

    bfs = BFS(g, s)
    for a in g.V():
        assert a.color == Color.BLACK

    assert r.d == 1
    assert s.d == 0
    assert t.d == 2
    assert u.d == 3
    assert v.d == 2
    assert w.d == 1
    assert x.d == 2
    assert y.d == 3

    assert r.π == s
    assert s.π is None
    assert t.π == w
    assert u.π == t
    assert v.π == r
    assert w.π == s
    assert x.π == w
    assert y.π == x
