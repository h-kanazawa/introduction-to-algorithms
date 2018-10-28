# -*- coding: utf-8 -*-

import heapq
from operator import itemgetter
from src.disjoint_set import *


class V:
    def __init__(self, v):
        self.v = v
        self.key = float('inf')
        self.π = None

    def __lt__(self, other):
        return self.v < other.v

    def __str__(self):
        return 'v:{}, key:{}, π:{}'.format(
            self.v,
            self.key,
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
                edges.add((frozenset([v, u]), w))
        return edges

    def has_weight_error(self):
        """Find typing error of weight if this function returns true"""
        E_with_w = self.E()
        E_without_w = set([vu for vu, w in E_with_w])
        return len(E_with_w) != len(E_without_w)


def mst_kruskal(G):
    A = set()

    # to get Disjoint Set element of vertex
    v_X_map = {}

    TreeSet = set()
    for v in G.V():
        # make_set
        x = X(v)
        v_X_map[v] = x
        s = Set(x)
        TreeSet.add(s)

    sortedEdges = sorted(list(G.E()), key=itemgetter(1))
    for uv, w in sortedEdges:
        u, v = list(uv)
        uX = v_X_map[u]
        vX = v_X_map[v]

        if uX.find_set() != vX.find_set():
            A.add(frozenset([v, u]))

            # union
            _, should_be_deleted = union(uX, vX)
            TreeSet -= {should_be_deleted}

    return A


def mst_prim(G, r):
    for u in G.V():
        u.key = float('inf')
        u.π = None
    r.key = 0

    Q = []
    for u in G.V():
        heapq.heappush(Q, (u.key, u))

    edges = G.E()
    weightDict = {}
    for edge in edges:
        weightDict[edge[0]] = edge[1]

    while len(Q) != 0:
        _, u = heapq.heappop(Q)
        for v, w in G.Adj[u]:
            vu_set = frozenset([v, u])
            vu_weight = weightDict[vu_set]
            q = [vv for p, vv in Q]
            if v in q and vu_weight < v.key:
                v.π = u
                v.key = weightDict[vu_set]


if __name__ == '__main__':
    print('x')
