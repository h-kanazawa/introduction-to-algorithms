# -*- coding: utf-8 -*-

from enum import Enum


class Color(Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2


class V:
    def __init__(self):
        self.color = Color.WHITE
        self.d = float('inf')
        self.f = float('inf')
        self.π = None


class G:
    def __init__(self):
        self.Adj = {}

    def V(self):
        return self.Adj.keys()


class DFS:
    def __init__(self, g):
        """Θ(V + E)
        """

        self.g = g
        for u in g.V():
            u.color = Color.WHITE
            u.π = None

        self.time = 0

        for u in g.V():
            if u.color == Color.WHITE:
                self.visit(u)

    def visit(self, u):
        self.time += 1
        u.d = self.time
        u.color = Color.GRAY
        for v in self.g.Adj[u]:
            if v.color == Color.WHITE:
                v.π = u
                self.visit(v)
        u.color = Color.BLACK
        self.time += 1
        u.f = self.time


if __name__ == '__main__':
    print('x')
