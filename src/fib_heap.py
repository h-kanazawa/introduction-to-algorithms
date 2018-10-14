# -*- coding: utf-8 -*-


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

    def add_to_right(self, x):
        x.r = self.r
        x.l = self
        self.r.l = x
        self.r = x

    def link_list(self, x):
        self.r.l = x.l
        x.l.r = self.r
        self.r = x
        x.l = self

    def stringify(self):
        return 'k: {}, v: {}, p, {} {}: c: {} {}, l: {} {}, r: {} {}, degree: {}, mark: {}'.format(
            self.k,
            self.v,
            self.p.k,
            self.p.v,
            self.c.k,
            self.c.v,
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


def union(H1, H2):
    """union fib heaps

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


if __name__ == '__main__':
    print('x')
