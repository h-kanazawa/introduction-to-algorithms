# -*- coding: utf-8 -*-

from enum import Enum
from queue import Queue


class Color(Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2


class V:
    def __init__(self):
        self.color = Color.WHITE
        self.d = float('inf')
        self.π = None


class G:
    def __init__(self):
        self.Adj = {}

    def V(self):
        return self.Adj.keys()


class BFS:
    def __init__(self, g, s):
        """O(V + E)
        """
        self.g = g
        for u in g.V():
            if u == s:
                u.color = Color.GRAY
                u.d = 0
                u.π = None
            else:
                u.color = Color.WHITE
                u.d = float('inf')
                u.π = None

        Q = Queue()
        Q.put_nowait(s)

        while Q.empty() is False:
            u = Q.get_nowait()
            for v in self.g.Adj[u]:
                if v.color == Color.WHITE:
                    v.color = Color.GRAY
                    v.d = u.d + 1
                    v.π = u
                    Q.put_nowait(v)
            u.color = Color.BLACK


if __name__ == '__main__':
    print('x')
