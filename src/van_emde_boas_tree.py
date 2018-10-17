# -*- coding: utf-8 -*-

from math import floor, fmod


def high(u):
    def f(x):
        return floor(x / floor(u ** 0.5))
    return f


def low(u):
    def f(x):
        return fmod(x, floor(u ** 0.5))
    return f


def index(u):
    def f(x, y):
        return x * floor(u ** 0.5) + y
    return f


class VanEmdeBoas:

    def __init__(self, u):
        """van Emde Boas Tree

        Arguments:
            u {int} -- 2 ^ k (k is an integer)
        """
        self.u = u
        self.min = None
        self.max = None

        self.high = high(u)
        self.low = low(u)
        self.index = index(u)

        if u == 2:
            self.summary = None
            self.cluster = None
            return

        # ⊥√u
        fu = floor(u ** 0.5)
        self.summary = VanEmdeBoas(fu)
        self.cluster = [VanEmdeBoas(fu) for i in range(0, fu)]

    def member(self, x):
        if x == self.min or x == self.max:
            return True
        elif self.u == 2:
            return False
        else:
            return self.cluster[self.high(x)].member(self.low(x))

    def successor(self, x):
        """O(loglog(u))
        """
        if self.u == 2:
            if x == 0 and self.max == 1:
                return 1
            else:
                return None
        elif self.min is not None and x < self.min:
            return self.min
        else:
            # max value of cluster having x
            max_low = self.cluster[self.high(x)].max
            if max_low is not None and self.low(x) < max_low:
                offset = self.cluster[self.high(x)].successor(self.low(x))
                return self.index(self.high(x), offset)
            else:
                succ_cluster = self.summary.successor(self.high(x))
                if succ_cluster is None:
                    return None
                else:
                    offset = self.cluster[succ_cluster].min
                    return self.index(succ_cluster, offset)

    def predecessor(self, x):
        """O(loglog(u))
        """
        if self.u == 2:
            if x == 1 and self.min == 0:
                return 0
            else:
                return None
        elif self.max is not None and x > self.max:
            return self.max
        else:
            min_low = self.cluster[self.high(x)].min
            if min_low is not None and self.low(x) > min_low:
                offset = self.cluster[self.high(x)].predecessor(self.low(x))
                return self.index(self.high(x), offset)
            else:
                pred_cluster = self.summary.predecessor(self.high(x))
                if pred_cluster is None:
                    if self.min is not None and x > self.min:
                        return self.min
                    else:
                        return None
                else:
                    offset = self.cluster[pred_cluster].max
                    return self.index(pred_cluster, offset)


if __name__ == '__main__':
    print('x')
