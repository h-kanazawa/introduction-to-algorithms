# -*- coding: utf-8 -*-


class V:
    def __init__(self, v):
        self.v = v
        self.d = float('inf')
        self.π = None

    def __lt__(self, other):
        return self.v < other.v

    def __str__(self):
        return 'v:{}, d:{}, π:{}'.format(
            self.v,
            self.d,
            self.π.v if self.π is not None else 'None'
        )


class G:
    def __init__(self):
        self.Adj = {}
        # Each element of Adj is tuple (next vertex, edge weight)

    def V(self):
        return set(self.Adj.keys())

    def E(self):
        edges = set()
        for v in self.V():
            for u, w in self.Adj[v]:
                edges.add(((v, u), w))
        return edges


def initialize_single_source(g, s):
    for v in g.V():
        v.d = float('inf')
        v.π = None
    s.d = 0


def relax(u, v, w_uv):
    if v.d > u.d + w_uv:
        v.d = u.d + w_uv
        v.π = u


def bellman_ford(g, s):
    initialize_single_source(g, s)

    len_gv = len(g.V())
    for i in range(0, len_gv - 1):
        for (u, v), w in g.E():
            relax(u, v, w)

    for (u, v), w in g.E():
        if v.d > u.d + w:
            return False

    return True


if __name__ == '__main__':
    print('x')
