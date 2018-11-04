# -*- coding: utf-8 -*-

import heapq


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
        # edge weight must not be negative

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
        return True
    return False


def dijkstra(g, s):
    initialize_single_source(g, s)

    S = frozenset()

    # The data structure for Q effects total Dijkstra's computational complexity.
    Q = []
    for v in g.V():
        heapq.heappush(Q, (v.d, v))

    while len(Q) != 0:
        _, u = heapq.heappop(Q)

        S = S | frozenset([u])

        for v, w in g.Adj[u]:
            relaxed = relax(u, v, w)

            # Re-sort Queue
            # (It's better to use a Queue implementation which has light DECREASE-KEY operation)
            if relaxed:
                new_Q = []
                for _, q in Q:
                    heapq.heappush(new_Q, (q.d, q))
                Q = new_Q


if __name__ == '__main__':
    print('x')
