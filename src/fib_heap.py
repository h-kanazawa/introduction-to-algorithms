# -*- coding: utf-8 -*-

from math import floor, log


class X:
    def __init__(self, k, v, degree=0, mark=False, p=None, c=None):
        """[summary]

        Arguments:
            k {int} -- key
            v {any} -- value
            degree {int} -- the number of children
            mark {bool} -- is marked
            p {X} -- parent
            c {X} -- a child
        """
        self.k = k
        self.v = v
        self.d = degree
        self.mark = mark
        self.p = p
        self.c = c
        self.l = self
        self.r = self

    def siblings_r(self):
        """show siblings as list
        clockwise
        """
        xs = [self]
        curr = self.r
        while curr != self:
            xs.append(curr)
            curr = curr.r
        return xs

    def siblings_l(self):
        """show siblings as list
        anticlockwise
        """
        xs = [self]
        curr = self.l
        while curr != self:
            xs.insert(0, curr)
            curr = curr.l
        return xs

    def children(self):
        """show children as list
        """
        if self.c is None:
            return []
        return self.c.siblings_r()

    def add_to_right(self, x):
        x.r = self.r
        x.l = self
        self.r.l = x
        self.r = x

    def add_to_left(self, x):
        x.l = self.l
        x.r = self
        self.l.r = x
        self.l = x

    def link_list(self, x):
        self.r.l = x.l
        x.l.r = self.r
        self.r = x
        x.l = self

    def remove_myself_from_siblings(self):
        if self.r == self:
            return
        self.l.r = self.r
        self.r.l = self.l
        self.l = self
        self.r = self

    def add_child(self, y):
        if self.d == 0:
            self.c = y
        else:
            self.c.add_to_right(y)
        self.d += 1
        y.p = self

    def stringify(self):
        return 'k: {}, v: {}, p, {}: c: {}, l: ({}, {}), r: ({}, {}), degree: {}, mark: {}'.format(
            self.k,
            self.v,
            'None' if self.p is None else '({}, {})'.format(self.p.k, self.p.v),
            'None' if self.c is None else '({}, {})'.format(self.c.k, self.c.v),
            self.l.k,
            self.l.v,
            self.r.k,
            self.r.v,
            self.d,
            self.mark
        )

    def __str__(self):
        return self.stringify()


class FibHeap:
    def __init__(self):
        """make fib heap
        amortized cost: O(1)
        page 424
        """
        self.min = None
        # the number of nodes
        self.n = 0

    def root_list(self):
        if self.min is None:
            return []
        return self.min.siblings_r()

    def insert(self, x):
        """insert
        amortized cost: O(1)
        page 425

        Arguments:
            x {X} -- node
        """

        if self.min is None:
            self.min = x
        else:
            self.min.add_to_right(x)
            if x.k < self.min.k:
                self.min = x
        self.n += 1

    def extract_min(self):
        z = self.min

        if z is None:
            return None

        if z.c is not None:
            # add z.children to root_list
            child = z.c
            z.c = None

            for c in child.siblings_r():
                c.p = None

            z.l.link_list(child)

        # remove z from root_list
        if z == z.r:
            self.min = None
        else:
            self.min = z.r
            z.remove_myself_from_siblings()
            self.consolidate()
        self.n -= 1
        return z

    def consolidate(self):
        Dn = D(self.n)
        A = [None for _ in range(Dn + 1)]
        for w in self.root_list():
            x = w
            d = x.d
            while A[d] is not None:
                # y is a node whose degree is same with x
                y = A[d]
                if x.k > y.k:
                    tmp = x
                    x = y
                    y = tmp
                # at this point, x.k < y.k is guarantieed
                self.link(y, x)
                A[d] = None
                d += 1
            A[d] = x
        self.min = None

        for i in range(Dn + 1):
            if A[i] is not None:
                A[i].l = A[i]
                A[i].r = A[i]
                if self.min is None:
                    self.min = A[i]
                else:
                    self.min.add_to_left(A[i])
                    if A[i].k < self.min.k:
                        self.min = A[i]

    def link(self, y, x):
        y.remove_myself_from_siblings()
        x.add_child(y)
        y.mark = False


def union(H1, H2):
    """union fib heaps

    amortized cost: O(1)

    Arguments:
        H1 {FibHeap}
        H2 {FibHeap}
    """
    H = FibHeap()
    H1.min.link_list(H2.min)
    # link H2 root list to H root list
    if H1.min is None or (H2.min is not None and H2.min.k < H1.min.k):
        H.min = H2.min
    else:
        H.min = H1.min
    H.n = H1.n + H2.n
    return H


def D(n):
    """maximum degree

    Arguments:
        n {float} the number of nodes

    Returns:
        int
    """
    return floor(log(n, 2))


if __name__ == '__main__':
    print('x')
