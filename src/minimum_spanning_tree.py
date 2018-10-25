# -*- coding: utf-8 -*-

from operator import itemgetter
from src.disjoint_set import *


class V:
    def __init__(self, v):
        self.v = v


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


if __name__ == '__main__':
    print('x')
